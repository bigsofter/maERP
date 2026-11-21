#!/usr/bin/env python3
"""Отправка задачи разработки в портал TinyCIO (POST /api/devcost/tasks).

  push.py send TASK.json      — записать задачу (сначала дотправляет очередь)
  push.py flush               — дотправить очередь
  push.py list [--product P] [--from D] [--to D]  — что уже записано (сверка)
  push.py targets             — маршруты «продукт × заказчик»
  push.py target-put JSON     — завести маршрут на нового заказчика
  push.py product             — продукт текущего репозитория
  push.py agent my-tasks                      — «Мои задачи» владельца + тикеты на John Dow
  push.py agent ticket N                      — карточка, лента, шаги, вложения, учёт времени
  push.py agent take|steps|note|handover|resume|complete N [BODY.json|-]
        BODY: {"note","john_steps":[{title,description,minutes}],"owner_steps":[…],"to_status"}

TASK.json: {product?, billto?, executor?, date, title, subtasks:[{task,hours,descr,category,role}], source?, ref?}
product по умолчанию — из корня репозитория, ref — product:date:sha1(product|billto|date|title)[:16].
Токен: DEVCOST_TOKEN в ~/.config/tinycio/devcost.env (или env), адрес — DEVCOST_URL (https://my.tinycio.com).
Сеть/5xx/404 → задача ложится в ~/.config/tinycio/devcost-outbox/, повтор безопасен (ref).
Только stdlib.
"""
import datetime
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

CFG = pathlib.Path.home() / ".config" / "tinycio"
OUTBOX = CFG / "devcost-outbox"
REJECTED = OUTBOX / "rejected"
LOG = CFG / "devcost-log.jsonl"

# Корень репозитория (имя папки основного checkout) → продукт портала.
PRODUCTS = {
    "maOptique": "maOptique",
    "maTransports": "maTransports",
    "shukranpay": "ShukranPay",
    "MaRessources": "maRessources",
    "maBoutique": "maBoutique",
    "maERP": "maERP",
}
NOT_COUNTED = {"tinycio", "chatben"}  # в учёт не входят


def env():
    file_vals = {}
    f = CFG / "devcost.env"
    if f.exists():
        for line in f.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                file_vals[k.strip()] = v.strip().strip('"').strip("'")
    # Файл конфигурации главнее окружения: .envrc/CI репозитория не подменят адрес и токен.
    vals = {**dict(os.environ), **{k: v for k, v in file_vals.items()}}
    return vals.get("DEVCOST_URL", "https://my.tinycio.com").rstrip("/"), vals.get("DEVCOST_TOKEN", "")


def agent_token():
    """Агентский токен (право agent) — отдельно от токена учёта часов: им действуют от имени владельца."""
    f = CFG / "devcost.env"
    if f.exists():
        for line in f.read_text().splitlines():
            if line.strip().startswith("DEVCOST_AGENT_TOKEN="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return ""


def repo_name(cwd=None):
    try:
        d = subprocess.run(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"], cwd=cwd,
                           capture_output=True, text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""
    p = pathlib.Path(d)
    return (p.parent if p.name == ".git" else p).name


def detect_product():
    name = repo_name()
    if name in NOT_COUNTED or name.lower() in NOT_COUNTED:
        return None, name
    return PRODUCTS.get(name), name


ALLOWED_HOSTS = {"my.tinycio.com"}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    """Редиректы не идём: urllib унёс бы Authorization на чужой хост."""

    def redirect_request(self, *a, **k):
        return None


OPENER = urllib.request.build_opener(NoRedirect)


def check_url(url):
    u = urllib.parse.urlparse(url)
    local = u.hostname in ("127.0.0.1", "localhost")
    if not ((u.scheme == "https" and u.hostname in ALLOWED_HOSTS) or (local and u.scheme in ("http", "https"))):
        sys.exit(f"DEVCOST_URL {url!r}: только https://my.tinycio.com (или localhost для тестов) — токен не отправлен")


def call(method, path, body=None, query=None, token=None):
    url, default_token = env()
    token = token if token is not None else default_token
    if not token:
        # Без токена — как без сети: задача ляжет в очередь и уйдёт после выпуска токена.
        return 0, {"error": "нет DEVCOST_TOKEN в ~/.config/tinycio/devcost.env"}
    check_url(url)
    full = url + path + ("?" + urllib.parse.urlencode(query) if query else "")
    data = json.dumps(body, ensure_ascii=False).encode() if body is not None else None
    req = urllib.request.Request(full, data=data, method=method,
                                 headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"})
    try:
        with OPENER.open(req, timeout=30) as r:
            return r.status, json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read() or b"{}")
        except ValueError:
            return e.code, {"error": e.reason}
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        return 0, {"error": str(e)}


def retryable(code):
    return code == 0 or code == 404 or code == 429 or code >= 500


def normalize(task):
    t = dict(task)
    if not t.get("product"):
        prod, name = detect_product()
        if not prod:
            sys.exit(f"продукт не определён по репозиторию «{name}» — укажите product в задаче")
        t["product"] = prod
    t.setdefault("billto", "TinyCIO")
    t.setdefault("executor", "john_dow")
    t.setdefault("date", datetime.date.today().isoformat())
    if not t.get("ref"):
        key = f"{t['product']}|{t['billto']}|{t['date']}|{t['title'].strip()}"
        t["ref"] = f"{t['product']}:{t['date']}:{hashlib.sha1(key.encode()).hexdigest()[:16]}"
    return t


def queue(t, why):
    OUTBOX.mkdir(parents=True, exist_ok=True)
    f = OUTBOX / (t["ref"].replace("/", "_").replace(":", "_") + ".json")
    f.write_text(json.dumps(t, ensure_ascii=False, indent=1))
    print(f"в очередь ({why}): {f}")


def send_one(t, from_queue=None):
    code, resp = call("POST", "/api/devcost/tasks", t)
    if code in (200, 201):
        with LOG.open("a") as lf:
            lf.write(json.dumps({"at": datetime.datetime.now().isoformat(timespec="seconds"), "ref": t["ref"],
                                 "number": resp.get("number"), "hours": resp.get("hours"), "product": t["product"],
                                 "billto": t["billto"], "title": t["title"]}, ensure_ascii=False) + "\n")
        state = "записана" if resp.get("created") else "уже была"
        print(f"тикет {resp.get('number')} — {state}, {resp.get('hours')} ч · {t['product']} × {t['billto']} · {t['title']}")
        if resp.get("finance_error"):
            print("  ! " + resp["finance_error"])
            if from_queue is None:
                queue(t, "реестр не обновлён")
                return True
        if from_queue is not None:
            from_queue.unlink(missing_ok=True)
        return True
    if retryable(code):
        if from_queue is None:
            queue(t, f"{code or 'сеть'}: {resp.get('error')}")
            return True  # отложена — дойдёт при следующем send/flush, коммит не держим
        print(f"очередь: {t['ref']} — снова {code or 'сеть'}, оставлена")
        return False
    print(f"ОТКАЗ {code}: {resp.get('error')} · {t.get('title')}")
    if from_queue is not None:
        REJECTED.mkdir(parents=True, exist_ok=True)
        from_queue.rename(REJECTED / from_queue.name)
        print(f"  перенесена в {REJECTED / from_queue.name}")
    return False


def fetch_bytes(path, token, query):
    """GET байтов (вложение тикета) — (код, байты); без редиректов, только разрешённый хост."""
    url, _ = env()
    check_url(url)
    req = urllib.request.Request(url + path + "?" + urllib.parse.urlencode(query), method="GET",
                                 headers={"Authorization": "Bearer " + token})
    try:
        with OPENER.open(req, timeout=120) as r:
            return r.status, r.read(30 << 20)
    except urllib.error.HTTPError as e:
        return e.code, b""
    except (urllib.error.URLError, TimeoutError, OSError):
        return 0, b""


def ticket_dump(number, token):
    """Карточка целиком (поля, свойства стадий, лента, шаги, учёт времени) → ticket.json и ВСЕ вложения
    (скрины, файлы, голосовые с расшифровкой, PDF-инструкции) → ~/.cache/tinycio/tickets/<N>/.
    Печатает пути: агент открывает их Read (картинки и PDF Read показывает)."""
    q = urllib.parse.quote(number, safe="")
    code, resp = call("GET", "/api/devcost/agent/tickets/" + q, token=token)
    if code != 200:
        print(json.dumps(resp, ensure_ascii=False, indent=1))
        return 2
    d = pathlib.Path.home() / ".cache" / "tinycio" / "tickets" / number.replace("/", "_")
    d.mkdir(parents=True, exist_ok=True)
    (d / "ticket.json").write_text(json.dumps(resp, ensure_ascii=False, indent=1))
    t = resp.get("ticket") or {}
    print(f"{t.get('number')} · {t.get('status')}/{t.get('state')} · {t.get('client_name', '')} · {t.get('title', '')}")
    print(f"карточка целиком (поля, свойства, лента, шаги): {d / 'ticket.json'}")
    seen = set()
    for i, it in enumerate(resp.get("attachments") or []):
        fid, href = it.get("file_id") or "", it.get("href") or ""
        key = fid or href
        if not key or key in seen:
            continue
        seen.add(key)
        name = re.sub(r"[^\w.\-]+", "_", it.get("file_name") or it.get("type") or "file")[:80]
        if "." not in name:
            ext = {"image/jpeg": ".jpg", "image/png": ".png", "application/pdf": ".pdf", "audio/ogg": ".ogg",
                   "video/mp4": ".mp4"}.get(it.get("mime_type") or "", "")
            if not ext and (it.get("type") == "photo" or it.get("kind") == "photo"):
                ext = ".jpg"
            name += ext
        out = d / f"{i + 1:02d}_{name}"
        code, data = fetch_bytes(f"/api/devcost/agent/tickets/{q}/file", token, {"file_id": fid} if fid else {"href": href})
        if code == 200 and data:
            out.write_bytes(data)
            line = f"  файл: {out}"
        else:
            line = f"  файл не скачан ({code}): {it.get('file_name') or key}"
        if it.get("transcript"):
            line += f" · расшифровка: {it['transcript'][:200]}"
        print(line)
    tl = resp.get("timeline") or []
    print(f"лента: {len(tl) if isinstance(tl, list) else '?'} записей — читай ticket.json → timeline (сообщения, авторы, вложения, статусы)")
    return 0


def flush():
    if not OUTBOX.exists():
        return
    for f in sorted(OUTBOX.glob("*.json")):
        send_one(json.loads(f.read_text()), from_queue=f)


def main(argv):
    if not argv:
        sys.exit(__doc__)
    cmd = argv[0]
    CFG.mkdir(parents=True, exist_ok=True)
    if cmd == "send":
        task = normalize(json.loads(pathlib.Path(argv[1]).read_text() if len(argv) > 1 and argv[1] != "-" else sys.stdin.read()))
        flush()
        sys.exit(0 if send_one(task) else 2)
    if cmd == "flush":
        flush()
        return
    if cmd == "list":
        q = {}
        it = iter(argv[1:])
        for a in it:
            q[a.lstrip("-")] = next(it)
        code, resp = call("GET", "/api/devcost/tasks", query=q)
        print(json.dumps(resp, ensure_ascii=False, indent=1))
        sys.exit(0 if code == 200 else 2)
    if cmd == "targets":
        code, resp = call("GET", "/api/devcost/targets")
        for t in resp.get("targets", []):
            print(f"{t['product']:13} × {t['billto']:12} → клиент {t['client_id']}, объект {t['service_object_id']}, инициатива {t['initiative_id']}")
        sys.exit(0 if code == 200 else 2)
    if cmd == "target-put":
        code, resp = call("PUT", "/api/devcost/targets", json.loads(argv[1]))
        print(code, json.dumps(resp, ensure_ascii=False))
        sys.exit(0 if code == 200 else 2)
    if cmd == "agent":
        if len(argv) < 2:
            sys.exit(__doc__)
        act = argv[1]
        at = agent_token()
        if not at:
            sys.exit("нет DEVCOST_AGENT_TOKEN в ~/.config/tinycio/devcost.env — попросите владельца: devcost_setup.sh agent-token")
        if act == "my-tasks":
            code, resp = call("GET", "/api/devcost/agent/my-tasks", token=at)
        elif act == "ticket" and len(argv) > 2:
            sys.exit(ticket_dump(argv[2], at))
        elif act in ("take", "steps", "note", "handover", "resume", "complete") and len(argv) > 2:
            body = {}
            if len(argv) > 3:
                body = json.loads(sys.stdin.read() if argv[3] == "-" else pathlib.Path(argv[3]).read_text())
            code, resp = call("POST", f"/api/devcost/agent/tickets/{urllib.parse.quote(argv[2], safe='')}/{act}", body, token=at)
        else:
            sys.exit(__doc__)
        print(json.dumps(resp, ensure_ascii=False, indent=1))
        if code == 0:
            print("портал недоступен или нет токена — действие НЕ выполнено (в очередь не ставится)", file=sys.stderr)
        sys.exit(0 if code == 200 else 2)
    if cmd == "product":
        prod, name = detect_product()
        print(prod or f"(не учитывается: {name})")
        return
    sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
