// Vidéothèque du landing (`/{locale}/videos`) — ce que dit chaque épisode et où
// il se range. Module SERVEUR: comme features-content, il ne doit jamais entrer
// dans un bundle client (les composants clients reçoivent des props résolues).
//
// CLASSEMENT. Les épisodes se rangent dans les catégories des pages «fonctions»
// (FEATURE_CATEGORIES, mêmes noms courants, même ordre) — pas de second
// classement. Une seule exception, décidée par le propriétaire le 2026-10-03:
// la partie I du script («Знакомство», E01–E03 et la bande-annonce) forme un
// groupe «Découverte» AU-DESSUS des catégories. Ce n'est pas `demarrage`
// («Par où commencer» = reprendre ses fichiers, brancher la comptabilité,
// choisir les modules): découvrir le produit et le mettre en route sont deux
// moments différents.
//
// TEXTES. Ils reprennent la voix CORRIGÉE de l'épisode (noms du code), jamais
// le script: le script a été faux une vingtaine de fois sur la bande-annonce.
// `gains` = les trois lignes «ce que vous y gagnez» de la carte finale de la
// vidéo (copy.json `sNN.b1..b3` de la dernière scène), mot pour mot. La transcription
// vient de `video-transcripts.json`, écrit par l'outil de la série.
//
// Pas d'arabe: la série n'existe pas en arabe (voir videos.ts).

import type { FeatureCategoryId } from './features-content';
import { FEATURE_CATEGORIES, FEATURE_CATEGORY, featureCategoryHeader, featureLabels, featureNav } from './features-content';
import type { ExplorerGroup, ExplorerItem } from './FeatureExplorer';
import transcripts from './video-transcripts.json';
import type { LandingVideo } from './videos';
import {
  TRAILER_EPISODE,
  VIDEO_LOCALES,
  episodeSlug,
  formatDuration,
  landingVideo,
  videoEpisodes,
  videoFiles,
} from './videos';

export type VideoGroupId = 'intro' | FeatureCategoryId;

export interface EpisodeText {
  /** «Épisode 1», «Bande-annonce». */
  kicker: string;
  /** Le titre en question — ce que le visiteur se demande. */
  title: string;
  /** Une phrase: ce qu'on voit dans la vidéo. */
  lead: string;
  /** Libellé accessible du lecteur. */
  aria: string;
  /** Les trois lignes de la carte finale de la vidéo. Absentes: la bande-annonce n'en a pas. */
  gains?: readonly [string, string, string];
}

interface LibraryEntry {
  episode: string;
  group: VideoGroupId;
  text: Record<string, EpisodeText>;
}

/**
 * Dans l'ordre de la série. Un épisode publié (videos.json) sans entrée ici fait
 * échouer le test. L'inverse est permis: une entrée peut précéder la publication
 * — elle reste invisible (pas de carte, 404) tant que le manifeste n'a pas la vidéo.
 */
const LIBRARY: readonly LibraryEntry[] = [
  {
    episode: TRAILER_EPISODE,
    group: 'intro',
    text: {
      fr: {
        kicker: 'Bande-annonce',
        title: 'Qu’est-ce que maTransports, en deux minutes ?',
        lead: 'Un voyage, de la demande jusqu’à l’encaissement : le devis, la mission, le chauffeur sur la route, la facture et la banque.',
        aria: 'Bande-annonce maTransports',
      },
      en: {
        kicker: 'Trailer',
        title: 'What is maTransports, in two minutes?',
        lead: 'One trip, from request to cash: the quote, the mission, the driver on the road, the invoice and the bank.',
        aria: 'maTransports trailer',
      },
      es: {
        kicker: 'Tráiler',
        title: '¿Qué es maTransports, en dos minutos?',
        lead: 'Un viaje, de la solicitud al cobro: el presupuesto, la misión, el conductor en ruta, la factura y el banco.',
        aria: 'Tráiler de maTransports',
      },
      ru: {
        kicker: 'Трейлер',
        title: 'Что такое maTransports — за две минуты?',
        lead: 'Один рейс — от заявки до денег: предложение, рейс, водитель в дороге, фактура и банк.',
        aria: 'Трейлер maTransports',
      },
    },
  },
  {
    episode: '01-e01',
    group: 'intro',
    text: {
      fr: {
        kicker: 'Épisode 1',
        title: 'Comment un seul poste de travail remplace-t-il Excel, WhatsApp et les classeurs ?',
        lead: 'Le menu organisé par métier, vos espaces qui vous suivent, Cmd-K, trois thèmes et cinq langues — et une entreprise de démonstration que vous supprimez en deux clics.',
        aria: 'Épisode 1 — le poste de travail',
        gains: [
          'Un seul poste de travail au lieu des tableaux, des chats et des classeurs — sans installation.',
          'Un menu adapté au métier : chacun voit son travail, pas tout en vrac.',
          'Découvrez le produit sur un exemple vivant et saisissez vos propres missions le jour même.',
        ],
      },
      en: {
        kicker: 'Episode 1',
        title: 'How does one workplace replace Excel, WhatsApp and folders?',
        lead: 'A menu organized by profession, workspaces that follow you, Cmd-K, three themes and five languages — and a demo company you remove in two clicks.',
        aria: 'Episode 1 — the workplace',
        gains: [
          'One workplace instead of spreadsheets, chats and folders — nothing to install.',
          'A menu shaped to each profession: everyone sees their own work, not everything at once.',
          'Learn on a live example and enter your own missions the same day.',
        ],
      },
      es: {
        kicker: 'Episodio 1',
        title: '¿Cómo sustituye un solo puesto de trabajo a Excel, WhatsApp y las carpetas?',
        lead: 'Un menú ordenado por oficios, espacios que le acompañan, Cmd-K, tres temas y cinco idiomas, y una empresa de demostración que se borra en dos clics.',
        aria: 'Episodio 1: el puesto de trabajo',
        gains: [
          'Un solo puesto de trabajo en lugar de hojas de cálculo, chats y carpetas, sin instalar nada.',
          'Un menú adaptado a cada oficio: cada uno ve su trabajo, no todo a la vez.',
          'Aprenda con un ejemplo real y registre sus propias misiones ese mismo día.',
        ],
      },
      ru: {
        kicker: 'Эпизод 1',
        title: 'Как одно рабочее место заменяет Excel, WhatsApp и папки?',
        lead: 'Меню по профессиям, пространства, которые идут за вами, Cmd-K, три темы и пять языков — и демо-компания, которая удаляется в два клика.',
        aria: 'Эпизод 1 — рабочее место',
        gains: [
          'Одно рабочее место вместо таблиц, чатов и папок — без установки.',
          'Меню под профессию: каждый видит свою работу, а не всё подряд.',
          'Можно изучать на живом примере и в тот же день завести свои рейсы.',
        ],
      },
    },
  },
  {
    episode: '02-e02',
    group: 'intro',
    text: {
      fr: {
        kicker: 'Épisode 2',
        title: 'Pourquoi un seul écran appris suffit-il pour tous les autres ?',
        lead: 'Huit règles de l’interface : la fiche s’ouvre à côté de la liste, un tiret n’est pas un zéro, chaque chiffre montre sa source, et on bloque seulement là où l’erreur coûte de l’argent.',
        aria: 'Épisode 2 — huit règles de l’interface',
        gains: [
          'Une formation courte : les mêmes règles d’un écran à l’autre.',
          'Des chiffres fiables, parce que leur origine est visible.',
          'De la liberté là où l’humain décide, et une protection là où l’erreur coûte de l’argent.',
        ],
      },
      en: {
        kicker: 'Episode 2',
        title: 'Why does learning one screen teach you all the others?',
        lead: 'Eight interface rules: the card opens next to the list, a dash is not a zero, every figure shows its source, and the system blocks only where a mistake costs money.',
        aria: 'Episode 2 — eight interface rules',
        gains: [
          'Short training: the same rules from screen to screen.',
          'Figures you can trust, because you can see where they come from.',
          'Freedom where a person decides, and protection where a mistake costs money.',
        ],
      },
      es: {
        kicker: 'Episodio 2',
        title: '¿Por qué basta con aprender una pantalla para saber usarlas todas?',
        lead: 'Ocho reglas de la interfaz: la ficha se abre junto a la lista, un guion no es un cero, cada cifra muestra su origen y el sistema solo bloquea donde un error cuesta dinero.',
        aria: 'Episodio 2: ocho reglas de la interfaz',
        gains: [
          'Una formación corta: las mismas reglas de una pantalla a otra.',
          'Cifras en las que se puede confiar, porque se ve su origen.',
          'Libertad donde decide una persona y protección donde un error cuesta dinero.',
        ],
      },
      ru: {
        kicker: 'Эпизод 2',
        title: 'Почему, освоив один экран, вы понимаете все остальные?',
        lead: 'Восемь правил интерфейса: карточка открывается рядом со списком, прочерк — не ноль, у каждой цифры виден источник, а запрет стоит только там, где ошибка стоит денег.',
        aria: 'Эпизод 2 — восемь правил интерфейса',
        gains: [
          'Короткое обучение: одни и те же правила от экрана к экрану.',
          'Цифры, которым можно доверять: видно, откуда они взялись.',
          'Свобода там, где решает человек, и защита там, где ошибка стоит денег.',
        ],
      },
    },
  },
  {
    episode: '03-e03',
    group: 'intro',
    text: {
      fr: {
        kicker: 'Épisode 3',
        title: 'Comment éviter que chaque tableau donne sa propre version du même chiffre ?',
        lead: 'La mission saisie une seule fois, lue en trois vues, les compteurs et les puces, l’argent par mission, client et corridor, l’export Excel et l’envoi programmé.',
        aria: 'Épisode 3 — le rapport partagé',
        gains: [
          'Plus de « deux versions de la vérité » : un enregistrement, de nombreuses lectures.',
          'Chaque métier voit sa vue, sans tableaux séparés.',
          'Des rapports compréhensibles même par ceux qui n’étaient pas à la réunion.',
        ],
      },
      en: {
        kicker: 'Episode 3',
        title: 'How do you stop every spreadsheet from holding its own version of the same figure?',
        lead: 'A mission entered once and read three ways, the counters and the “To invoice” chip, money by mission, client and corridor, the Excel export and the scheduled delivery.',
        aria: 'Episode 3 — one record, many readings',
        gains: [
          'No more “two versions of the truth”: one record, many readings.',
          'Each profession sees its own view, without separate spreadsheets.',
          'Reports that make sense even to someone who wasn’t at the meeting.',
        ],
      },
      es: {
        kicker: 'Episodio 3',
        title: '¿Cómo evitar que cada hoja de cálculo tenga su propia versión de la misma cifra?',
        lead: 'La misión introducida una vez y leída de tres maneras, los contadores y el chip «Por facturar», el dinero por misión, cliente y corredor, la exportación a Excel y el envío programado.',
        aria: 'Episodio 3: un registro, muchas lecturas',
        gains: [
          'Se acabaron las «dos versiones de la verdad»: un registro, muchas lecturas.',
          'Cada oficio ve su vista, sin hojas de cálculo aparte.',
          'Informes que entiende incluso quien no estuvo en la reunión.',
        ],
      },
      ru: {
        kicker: 'Эпизод 3',
        title: 'Как сделать, чтобы в каждой таблице не жила своя версия одной и той же цифры?',
        lead: 'Рейс, введённый один раз и прочитанный тремя способами, счётчики и чипы, деньги по рейсу, клиенту и коридору, выгрузка в Excel и рассылка по расписанию.',
        aria: 'Эпизод 3 — один ввод, много прочтений',
        gains: [
          'Никаких «двух версий правды»: одна запись — много прочтений.',
          'Каждая профессия видит свой срез без отдельных таблиц.',
          'Отчёты, понятные даже тому, кого не было на совещании.',
        ],
      },
    },
  },
  {
    episode: '04-e04',
    group: 'exploitation',
    text: {
      fr: {
        kicker: 'Épisode 4',
        title: 'Comment suivre tout ce qui roule sans tableau blanc, cahier ni messagerie ?',
        lead: 'Le poste de l’exploitant : quatre filtres, la colonne « Alerte », la fiche de mission à droite, les statuts dans l’ordre et l’écran dans cinq langues.',
        aria: 'Épisode 4 — le poste opérateur',
        gains: [
          'Un seul écran à la place du tableau et du cahier de l’exploitant.',
          'Problèmes, douane et retours à vide : un clic sur un filtre.',
          'De quoi répondre au client sur une seule fiche, sans fouiller les dossiers.',
        ],
      },
      en: {
        kicker: 'Episode 4',
        title: 'How do you follow everything that’s running without a whiteboard, notebook or group chat?',
        lead: 'The dispatcher’s desk: four filters, the Alert column, the mission card on the right, statuses in order, and the screen in five languages.',
        aria: 'Episode 4 — the dispatcher desk',
        gains: [
          'One screen instead of the dispatcher’s whiteboard and notebook.',
          'Problems, customs and empty returns: one click on a filter.',
          'What a client’s call needs, on one card, no digging through folders.',
        ],
      },
      es: {
        kicker: 'Episodio 4',
        title: '¿Cómo seguir todo lo que está en marcha sin pizarra, libreta ni chat de grupo?',
        lead: 'La mesa del operador de tráfico: cuatro filtros, la columna «Alerta», la ficha de la misión a la derecha, los estados en orden y la pantalla en cinco idiomas.',
        aria: 'Episodio 4: la mesa del operador',
        gains: [
          'Una pantalla en lugar de la pizarra y la libreta del operador de tráfico.',
          'Problemas, aduana y retornos en vacío: un clic en un filtro.',
          'Lo que pide la llamada de un cliente, en una sola ficha, sin rebuscar en carpetas.',
        ],
      },
      ru: {
        kicker: 'Эпизод 4',
        title: 'Как видеть всё, что в работе, без доски, тетради и чата?',
        lead: 'Стол координатора: четыре фильтра, колонка «Тревога», карточка рейса справа, статусы по порядку и экран на пяти языках.',
        aria: 'Эпизод 4 — пост оператора',
        gains: [
          'Один экран вместо доски и тетради координатора.',
          'Проблемы, таможня и порожние возвраты — в один клик фильтра.',
          'Ответ на звонок клиента — в одной карточке, без поиска по папкам.',
        ],
      },
    },
  },
  {
    episode: '05-e05',
    group: 'exploitation',
    text: {
      fr: {
        kicker: 'Épisode 5',
        title: 'Que garde une mission une fois partie : qui a conduit, quand, à quel coût ?',
        lead: 'Le dossier de mission : l’attelage et les relais, les pointages envoyés depuis le téléphone du chauffeur, le mode de prix et les champs verrouillés après le départ.',
        aria: 'Épisode 5 — le dossier de mission',
        gains: [
          'L’historique complet de la mission — vos preuves en cas de litige avec le client.',
          'Relais et changement d’équipage sans « deux lignes dans Excel ».',
          'Le passé est protégé : un fait ne se corrige pas après coup.',
        ],
      },
      en: {
        kicker: 'Episode 5',
        title: 'What does a mission keep once it has left: who drove, when, at what cost?',
        lead: 'The mission dossier: the rig and the relays, the timestamps from the driver’s phone, the pricing mode and the fields that close once the mission has left.',
        aria: 'Episode 5 — the mission dossier',
        gains: [
          'The full history of the mission — your evidence in a dispute with a customer.',
          'Relays and crew changes without “two rows in Excel”.',
          'The past is protected: facts aren’t edited after the event.',
        ],
      },
      es: {
        kicker: 'Episodio 5',
        title: '¿Qué conserva una misión una vez en marcha: quién condujo, cuándo y a qué coste?',
        lead: 'El expediente de la misión: el enganche y los relevos, las marcas de hora desde el móvil del conductor, el modo de precio y los campos que ya no se tocan tras la salida.',
        aria: 'Episodio 5: el expediente de la misión',
        gains: [
          'El historial completo de la misión: sus pruebas en un litigio con el cliente.',
          'Relevos y cambios de tripulación sin «dos filas en Excel».',
          'El pasado está protegido: un hecho no se corrige a posteriori.',
        ],
      },
      ru: {
        kicker: 'Эпизод 5',
        title: 'Что остаётся от рейса, когда он уехал: кто вёз, когда и во сколько это обошлось?',
        lead: 'Досье рейса: сцепка и смены, отметки времени с телефона водителя, режим цены и поля, закрытые после выезда.',
        aria: 'Эпизод 5 — досье рейса',
        gains: [
          'Полная история рейса — доказательная база в споре с клиентом.',
          'Смена тягача и водителя — без «двух строк в Excel».',
          'Прошлое защищено: факт не правится задним числом.',
        ],
      },
    },
  },
  {
    episode: '06-e06',
    group: 'exploitation',
    text: {
      fr: {
        kicker: 'Épisode 6',
        title: 'Comment créer une mission en une seule page au lieu de six écrans ?',
        lead: 'La page « Nouvelle mission » : neuf sections, le cadre avant les acteurs, l’encours du client, le conteneur sur image, l’économie ligne par ligne et les deux boutons.',
        aria: 'Épisode 6 — créer une mission',
        gains: [
          'Un formulaire bâti sur vos écrans, pas sur un modèle étranger.',
          'Les acteurs obligatoires suivent l’Import, l’Export ou le National.',
          'Prix convenu = somme des lignes vendues ; la facture les reprend telles quelles.',
        ],
      },
      en: {
        kicker: 'Episode 6',
        title: 'How do you create a mission on one page instead of six screens?',
        lead: 'The “New mission” page: nine sections, the frame before the actors, the client’s outstanding balance, the container picked by picture, the economy line by line and the two buttons.',
        aria: 'Episode 6 — creating a mission',
        gains: [
          'A form built from your screens, not someone else’s template.',
          'Required actors follow Import, Export or Domestic.',
          'Agreed price = sum of the lines sold; the invoice takes them as they are.',
        ],
      },
      es: {
        kicker: 'Episodio 6',
        title: '¿Cómo crear una misión en una sola página en lugar de seis pantallas?',
        lead: 'La página «Nueva misión»: nueve secciones, el marco antes de los actores, el saldo pendiente del cliente, el contenedor elegido por imagen, la economía línea a línea y los dos botones.',
        aria: 'Episodio 6: crear una misión',
        gains: [
          'Un formulario hecho con sus pantallas, no con una plantilla ajena.',
          'Los actores obligatorios cambian según Importación, Exportación o Nacional.',
          'Precio acordado = suma de las líneas vendidas; la factura las toma tal cual.',
        ],
      },
      ru: {
        kicker: 'Эпизод 6',
        title: 'Как создать рейс на одной странице вместо шести экранов?',
        lead: 'Страница «Новый рейс»: девять разделов, рамка раньше участников, задолженность клиента, контейнер по картинке, экономика строка за строкой и две кнопки.',
        aria: 'Эпизод 6 — создание рейса',
        gains: [
          'Форма по вашим экранам, а не по чужому шаблону.',
          'Обязательные участники подстраиваются под импорт, экспорт или внутренний рейс.',
          'Согласованная цена — сумма проданных строк; фактура берёт их как есть.',
        ],
      },
    },
  },
  {
    episode: '07-e07',
    group: 'exploitation',
    text: {
      fr: {
        kicker: 'Épisode 7',
        title: 'Où se tiennent la douane, les scellés, les étapes et l’argent d’une mission ?',
        lead: 'Le dossier d’un import : la douane avec ses termes (DUM, BAD, T1), les scellés du stock, l’ordre et le décalage des étapes, les frais de déplacement et l’estimation des coûts.',
        aria: 'Épisode 7 — douane, scellés et étapes',
        gains: [
          'Douane, scellés et étapes — dans le dossier, pas dans un classeur à part.',
          'Les règles du BAD et du retour à vide tenues par le système, pas par la mémoire.',
          'Une estimation fiable : chaque tarif porte sa source.',
        ],
      },
      en: {
        kicker: 'Episode 7',
        title: 'Where do customs, seals, steps and the money of a mission live?',
        lead: 'An import dossier: customs in your own terms (DUM, BAD, T1), seals from your stock, the order and shifting of the steps, travel allowances and the cost estimate.',
        aria: 'Episode 7 — customs, seals and steps',
        gains: [
          'Customs, seals and steps — inside the dossier, not in a separate folder.',
          'The BAD and empty-return rules are held by the system, not by memory.',
          'An estimate you can trust: every rate carries its source.',
        ],
      },
      es: {
        kicker: 'Episodio 7',
        title: '¿Dónde viven la aduana, los precintos, las etapas y el dinero de una misión?',
        lead: 'El expediente de una importación: la aduana con sus propias palabras (DUM, BAD, T1), los precintos de su stock, el orden de las etapas y su desplazamiento, los gastos de desplazamiento y la estimación de costes.',
        aria: 'Episodio 7: aduana, precintos y etapas',
        gains: [
          'Aduana, precintos y etapas: dentro del expediente, no en una carpeta aparte.',
          'Las reglas del BAD y de la devolución en vacío las mantiene el sistema, no la memoria.',
          'Una estimación fiable: cada tarifa lleva su origen.',
        ],
      },
      ru: {
        kicker: 'Эпизод 7',
        title: 'Где живут таможня, пломбы, этапы и деньги рейса?',
        lead: 'Досье импорта: таможня вашими словами (DUM, BAD, T1), пломбы со склада, порядок и сдвиг этапов, командировочные и оценка затрат.',
        aria: 'Эпизод 7 — таможня, пломбы и этапы',
        gains: [
          'Таможня, пломбы и этапы — внутри досье, а не в отдельной папке.',
          'Правила BAD и возврата пустого держит система, а не память.',
          'Оценка, которой можно верить: у каждой ставки — источник.',
        ],
      },
    },
  },
  {
    episode: '08-e08',
    group: 'exploitation',
    text: {
      fr: {
        kicker: 'Épisode 8',
        title: 'Que faire quand une commande part en plusieurs missions ?',
        lead: 'Le mode « Par commande », la deuxième mission qui reprend le fret non affecté, la fiche de commande recalculée et la ligne du relais Marrakech.',
        aria: 'Épisode 8 — commande et missions',
        gains: [
          'Une commande, autant de missions qu’il faut, sans ressaisir le fret.',
          'Une fiche de commande toujours conforme à ses missions.',
          'Chaque relais de chauffeur, de tracteur ou de remorque, inscrit sur la fiche de la mission.',
        ],
      },
      en: {
        kicker: 'Episode 8',
        title: 'What happens when one order leaves on several missions?',
        lead: 'The “By order” view, the second mission that picks up the unassigned freight, the order card rebuilt from its missions and the relay line in Marrakech.',
        aria: 'Episode 8 — order and missions',
        gains: [
          'One order, as many missions as you need, without re-entering the freight.',
          'An order card that always matches its missions.',
          'Every change of driver, tractor or trailer en route, on the mission card.',
        ],
      },
      es: {
        kicker: 'Episodio 8',
        title: '¿Qué pasa cuando un pedido sale en varias misiones?',
        lead: 'La vista «Por pedido», la segunda misión que recoge la mercancía aún sin asignar, la ficha del pedido recalculada a partir de las misiones y la línea del relevo en Marrakech.',
        aria: 'Episodio 8: pedido y misiones',
        gains: [
          'Un pedido, tantas misiones como necesite, sin volver a introducir la mercancía.',
          'Una ficha de pedido que siempre coincide con sus misiones.',
          'Cada cambio de conductor, tractor o remolque en ruta, en la ficha de la misión.',
        ],
      },
      ru: {
        kicker: 'Эпизод 8',
        title: 'Что делать, когда заказ уезжает несколькими рейсами?',
        lead: 'Режим «По заказам», второй рейс, который сам забирает нераспределённый груз, карточка заказа, собираемая из рейсов, и строка смены в Марракеше.',
        aria: 'Эпизод 8 — заказ и рейсы',
        gains: [
          'Один заказ — сколько угодно рейсов, без повторного ввода груза.',
          'Карточка заказа, которая всегда совпадает с его рейсами.',
          'Каждая смена водителя, тягача и трейлера в пути — в карточке рейса.',
        ],
      },
    },
  },
  {
    episode: '09-e09',
    group: 'direction',
    text: {
      fr: {
        kicker: 'Épisode 9',
        title: 'Un voyage ou deux : comment le décider avec un calcul, pas une impression ?',
        lead: 'Le calcul ouvert depuis la commande : deux scénarios côte à côte, le verdict en une phrase et un chiffre, l’étiquette de chaque hypothèse et le cas où le fret ne tient pas.',
        aria: 'Épisode 9 — un voyage ou deux',
        gains: [
          'Un chiffre à montrer au client qui demande de diviser le lot.',
          'Une décision claire pour un nouvel exploitant, dès le premier jour.',
          'La capacité comparée à vos remorques déclarées, dès la planification.',
        ],
      },
      en: {
        kicker: 'Episode 9',
        title: 'One trip or two: how do you decide with a calculation, not a hunch?',
        lead: 'The calculation opened from the order: two scenarios side by side, the verdict in a sentence and a number, the label on each assumption and the case where the freight doesn’t fit.',
        aria: 'Episode 9 — one trip or two',
        gains: [
          'A figure to show the client who asks you to split the load.',
          'A decision a new dispatcher understands from day one.',
          'Capacity checked against your declared trailers, at planning time.',
        ],
      },
      es: {
        kicker: 'Episodio 9',
        title: '¿Un viaje o dos? ¿Cómo decidirlo con un cálculo y no a ojo?',
        lead: 'El cálculo abierto desde el pedido: dos escenarios uno al lado del otro, el veredicto en una frase y una cifra, la etiqueta de cada hipótesis y el caso en que la carga no cabe.',
        aria: 'Episodio 9: un viaje o dos',
        gains: [
          'Una cifra para mostrar al cliente que pide dividir la carga.',
          'Una decisión que un nuevo planificador entiende desde el primer día.',
          'La capacidad, comparada con sus remolques declarados, ya al planificar.',
        ],
      },
      ru: {
        kicker: 'Эпизод 9',
        title: 'Один рейс или два: как решить расчётом, а не на глаз?',
        lead: 'Расчёт, открытый с заказа: два сценария рядом, вердикт фразой и цифрой, метка у каждого допущения и случай, когда груз не помещается.',
        aria: 'Эпизод 9 — один рейс или два',
        gains: [
          'Цифра, которую можно показать клиенту, просящему разделить партию.',
          'Решение, понятное новому диспетчеру с первого дня.',
          'Вместимость сверена с заявленными трейлерами ещё при планировании.',
        ],
      },
    },
  },
  {
    episode: '10-e10',
    group: 'exploitation',
    text: {
      fr: {
        kicker: 'Épisode 10',
        title: 'Comment répartir le fret d’une commande entre ses missions sans surcharger ?',
        lead: 'L’écran « Groupage » : quatre compteurs, les barres de poids et de volume, le lot déplacé en deux touches avec « Placer ici » et le bouton « Proposer une répartition ».',
        aria: 'Épisode 10 — le groupage',
        gains: [
          'Les lots d\'une commande répartis sur ses missions, tant qu\'elles ne sont pas parties.',
          'Le contrôle de la surcharge en poids et en volume à la fois.',
          'Une proposition de répartition que vous appliquez, ligne par ligne ou en entier.',
        ],
      },
      en: {
        kicker: 'Episode 10',
        title: 'How do you spread an order’s freight across its missions without overloading?',
        lead: 'The Groupage screen: four counters, the weight and volume bars, a lot moved in two taps with “Place here” and the “Propose a distribution” button.',
        aria: 'Episode 10 — groupage',
        gains: [
          'An order\'s lots spread across its missions until they leave.',
          'Overload control by weight and by volume at once.',
          'A distribution proposal you apply — line by line or in full.',
        ],
      },
      es: {
        kicker: 'Episodio 10',
        title: '¿Cómo repartir el flete de un pedido entre sus misiones sin sobrecargar?',
        lead: 'La pantalla «Grupaje»: cuatro contadores, las barras de peso y volumen, el lote movido en dos toques con «Colocar aquí» y el botón «Proponer un reparto».',
        aria: 'Episodio 10: grupaje',
        gains: [
          'Los lotes de un pedido repartidos entre sus misiones mientras no hayan salido.',
          'Control de sobrecarga por peso y por volumen a la vez.',
          'Una propuesta de reparto que aplica usted, línea a línea o entera.',
        ],
      },
      ru: {
        kicker: 'Эпизод 10',
        title: 'Как распределить груз заказа между рейсами и не перегрузить?',
        lead: 'Экран «Сборные грузы»: четыре счётчика, полосы веса и объёма, лот в два касания с «Разместить здесь» и кнопка «Предложить распределение».',
        aria: 'Эпизод 10 — сборные грузы',
        gains: [
          'Лоты заказа — по его рейсам, пока те не уехали.',
          'Контроль перегруза по весу и по объёму одновременно.',
          'Предложение раскладки, которое применяете вы — по строке или целиком.',
        ],
      },
    },
  },
  {
    episode: '11-e11',
    group: 'exploitation',
    text: {
      fr: {
        kicker: 'Épisode 11',
        title: 'Comment retrouver l’histoire d’un conteneur quand un litige commence par son numéro ?',
        lead: 'Le registre des conteneurs et la fiche de la boîte : dimensions, charge utile, propriété et location, reefer, examen CSC, contrôle ISO 6346 et numéro verrouillé.',
        aria: 'Épisode 11 — le registre des conteneurs',
        gains: [
          '« Où est MTRU 482917-2 ? » : une recherche, pas un appel à l’exploitant.',
          'Examen CSC et fin de location, avec compte à rebours.',
          'L’historique de la boîte, une preuve en cas de litige. Sans supplément.',
        ],
      },
      en: {
        kicker: 'Episode 11',
        title: 'How do you find a container’s history when a dispute starts with its number?',
        lead: 'The container registry and the container card: dimensions, payload, ownership and lease, reefer, the CSC exam, the ISO 6346 check and the number that can no longer change.',
        aria: 'Episode 11 — the container register',
        gains: [
          '“Where is MTRU 482917-2?” One search, not a call to dispatch.',
          'CSC exam and off-hire date, with a countdown.',
          'The box’s history: evidence in a dispute. At no extra cost.',
        ],
      },
      es: {
        kicker: 'Episodio 11',
        title: '¿Cómo recuperar el historial de un contenedor cuando un litigio empieza por su número?',
        lead: 'El registro de contenedores y la ficha del contenedor: dimensiones, carga útil, propiedad y alquiler, reefer, examen CSC, comprobación ISO 6346 y el número que ya no se puede cambiar.',
        aria: 'Episodio 11: el registro de contenedores',
        gains: [
          '«¿Dónde está MTRU 482917-2?»: una búsqueda, no una llamada al operador.',
          'Examen CSC y fin del alquiler, con cuenta atrás.',
          'El historial de la caja, una prueba en una disputa. Sin coste extra.',
        ],
      },
      ru: {
        kicker: 'Эпизод 11',
        title: 'Как найти историю контейнера, когда спор начинается с его номера?',
        lead: 'Реестр ящиков и карточка ящика: габариты, грузоподъёмность, владелец и аренда, рефрижератор, осмотр CSC, проверка по ISO 6346 и закрытый номер.',
        aria: 'Эпизод 11 — реестр контейнеров',
        gains: [
          '«Где сейчас MTRU 482917-2?» — один поиск, а не звонок диспетчеру.',
          'Осмотр CSC и конец аренды — с обратным отсчётом.',
          'История ящика — доказательство в споре. Без доплаты.',
        ],
      },
    },
  },
  {
    episode: '12-e12',
    group: 'exploitation',
    text: {
      fr: {
        kicker: 'Épisode 12',
        title: 'Que fait le chauffeur sur son téléphone, sans e-mail ni mot de passe ?',
        lead: 'L’app du chauffeur : le code à six chiffres, la mission sans prix, les boutons de statut, la file hors réseau, la photo du CMR, la signature, le péage et le plein.',
        aria: 'Épisode 12 — l’app du chauffeur',
        gains: [
          'Le journal de mission, sans appeler le chauffeur.',
          'Photo CMR et signature du destinataire, le jour de la livraison.',
          'Tickets et pleins depuis la route, en trésorerie chauffeurs et au journal carburant.',
        ],
      },
      en: {
        kicker: 'Episode 12',
        title: 'What does the driver do on the phone, with no e-mail and no password?',
        lead: 'The driver app: the six-digit code, the mission with no prices, the status buttons, the offline queue, the CMR photo, the signature, the toll receipt and the fill-up.',
        aria: 'Episode 12 — the driver app',
        gains: [
          'The mission log, without calling the driver.',
          'CMR photo and consignee signature on delivery day.',
          'Receipts and fill-ups from the road, in the driver treasury and the fuel journal.',
        ],
      },
      es: {
        kicker: 'Episodio 12',
        title: '¿Qué hace el conductor en su teléfono, sin correo ni contraseña?',
        lead: 'La app del conductor: el código de seis cifras, la misión sin precios, los botones de estado, la cola sin red, la foto del CMR, la firma, el ticket de peaje y el repostaje.',
        aria: 'Episodio 12: la app del conductor',
        gains: [
          'El historial de la misión, sin llamar al conductor.',
          'Foto del CMR y firma del destinatario, el día de la entrega.',
          'Tickets y repostajes desde la carretera, en la tesorería de conductores y el diario de combustible.',
        ],
      },
      ru: {
        kicker: 'Эпизод 12',
        title: 'Что делает водитель в телефоне — без почты и пароля?',
        lead: 'Приложение водителя: шестизначный код, рейс без цен, кнопки статуса, очередь без сети, фото CMR, подпись, чек за дорогу и заправка.',
        aria: 'Эпизод 12 — приложение водителя',
        gains: [
          'Журнал рейса — без звонков водителю.',
          'Фото CMR и подпись получателя — в день доставки.',
          'Чеки и заправки с дороги — в кассе водителей и в топливном журнале.',
        ],
      },
    },
  },
  {
    episode: '13-e13',
    group: 'exploitation',
    text: {
      fr: {
        kicker: 'Épisode 13',
        title: 'Qui vous doit de l’argent, et que devient la fiche d’un client que l’on range ?',
        lead: 'Le fichier clients avec deux colonnes calculées — ce que le client vous a rapporté et ce qu’il vous doit — la fiche avec l’ICE et le délai de paiement, et l’archivage qui garde l’historique.',
        aria: 'Épisode 13 — le fichier clients',
        gains: [
          'Qui vous doit et qui est en retard : visible directement dans la liste des clients.',
          'Les coordonnées du client se saisissent une seule fois.',
          'Un historique que le rangement ne casse pas.',
        ],
      },
      en: {
        kicker: 'Episode 13',
        title: 'Who owes you money, and what happens to a client you tidy away?',
        lead: 'The client directory with two calculated columns — what the client has brought you and what they owe — the card with the ICE and payment terms, and archiving that keeps the history.',
        aria: 'Episode 13 — the client directory',
        gains: [
          'Who owes you and who is late — visible right in the client list.',
          'Client details are entered only once.',
          'A company history that tidying up can’t erase.',
        ],
      },
      es: {
        kicker: 'Episodio 13',
        title: '¿Quién le debe dinero y qué pasa con un cliente que se archiva?',
        lead: 'El fichero de clientes con dos columnas calculadas —lo que el cliente le ha aportado y lo que le debe—, la ficha con el ICE y el plazo de pago, y el archivado que conserva la historia.',
        aria: 'Episodio 13: el fichero de clientes',
        gains: [
          'Quién le debe y quién va con retraso, a la vista en la lista de clientes.',
          'Los datos del cliente se introducen una sola vez.',
          'Una historia de la empresa a salvo de cualquier limpieza.',
        ],
      },
      ru: {
        kicker: 'Эпизод 13',
        title: 'Кто вам должен и что будет с клиентом, которого убирают из справочника?',
        lead: 'Справочник клиентов с двумя вычисляемыми колонками — сколько клиент принёс и сколько должен, карточка с ICE и отсрочкой платежа и архив, который сохраняет историю.',
        aria: 'Эпизод 13 — справочник клиентов',
        gains: [
          'Кто вам должен и кто просрочил — видно прямо в списке клиентов.',
          'Реквизиты клиента вводятся один раз.',
          'История компании, которую не сломать уборкой.',
        ],
      },
    },
  },
  {
    episode: '14-e14',
    group: 'exploitation',
    text: {
      fr: {
        kicker: 'Épisode 14',
        title: 'Comment un devis devient-il une mission sans rien ressaisir ?',
        lead: 'Le registre des devis, « Suggérer les lignes » avec l’origine du prix, l’exonération de TVA à l’export, l’envoi du PDF, le refus avec motif, puis « Créer la mission » en un clic.',
        aria: 'Épisode 14 — le devis',
        gains: [
          'Des devis selon vos tarifs, pas selon la mémoire du commercial.',
          'Le motif de chaque refus est conservé.',
          'Zéro ressaisie : devis → mission → facture.',
        ],
      },
      en: {
        kicker: 'Episode 14',
        title: 'How does a quote become a mission without retyping anything?',
        lead: 'The quote register, “Suggest lines” with the origin of the price, the VAT exemption for export, sending the PDF, a refusal with a reason, then “Create the mission” in one click.',
        aria: 'Episode 14 — the quote',
        gains: [
          'Quotes priced from your tariffs, not from a salesperson’s memory.',
          'The reason for every refusal is kept.',
          'Zero retyping: quote → mission → invoice.',
        ],
      },
      es: {
        kicker: 'Episodio 14',
        title: '¿Cómo se convierte un presupuesto en misión sin teclear nada dos veces?',
        lead: 'El registro de presupuestos, «Sugerir líneas» con el origen del precio, la exención de IVA en la exportación, el envío del PDF, el rechazo con motivo y «Crear la misión» en un clic.',
        aria: 'Episodio 14: el presupuesto',
        gains: [
          'Presupuestos según sus tarifas, no según la memoria del comercial.',
          'El motivo de cada rechazo queda guardado.',
          'Nada se teclea dos veces: presupuesto → misión → factura.',
        ],
      },
      ru: {
        kicker: 'Эпизод 14',
        title: 'Как предложение становится рейсом, и ничего не приходится вводить дважды?',
        lead: 'Реестр предложений, «Подобрать строки» с происхождением цены, освобождение от НДС для экспорта, отправка PDF, отказ с причиной и «Создать рейс» одним кликом.',
        aria: 'Эпизод 14 — предложение',
        gains: [
          'Предложение по вашим тарифам, а не по памяти продавца.',
          'Причина каждого отказа сохранена.',
          'Ноль повторного ввода: предложение → рейс → фактура.',
        ],
      },
    },
  },
  {
    episode: '15-e15',
    group: 'exploitation',
    text: {
      fr: {
        kicker: 'Épisode 15',
        title: 'Comment s’assurer, avant le départ, de ce qui a été convenu avec le client ?',
        lead: 'Le bon de commande : brouillon, « Émettre » qui fige le document, PDF envoyé par e-mail avec l’adresse et la date, acceptation, annulation avec motif, et son numéro dans la facture.',
        aria: 'Épisode 15 — le bon de commande',
        gains: [
          'Fini les discussions sur ce qui avait été convenu.',
          'Un document qui ne change pas après coup.',
          'L’envoi par e-mail depuis le bon, avec l’adresse et la date.',
        ],
      },
      en: {
        kicker: 'Episode 15',
        title: 'How do you pin down what was agreed with the client before the truck leaves?',
        lead: 'The order form: draft, “Issue” that freezes the document, a PDF e-mailed with the address and date, acceptance, cancellation with a reason, and its number in the invoice form.',
        aria: 'Episode 15 — the order form',
        gains: [
          'No more arguing about what was agreed.',
          'A document that does not change after the fact.',
          'E-mail sending from the form, with address and date.',
        ],
      },
      es: {
        kicker: 'Episodio 15',
        title: '¿Cómo asegurar, antes de la salida, lo acordado con el cliente?',
        lead: 'La orden de pedido: borrador, «Emitir» que congela el documento, PDF enviado por correo con la dirección y la fecha, aceptación, anulación con motivo y su número en el formulario de factura.',
        aria: 'Episodio 15: la orden de pedido',
        gains: [
          'Se acabaron las discusiones sobre lo acordado.',
          'Un documento que no cambia a posteriori.',
          'El envío por correo desde la orden, con dirección y fecha.',
        ],
      },
      ru: {
        kicker: 'Эпизод 15',
        title: 'Как до выезда зафиксировать, о чём договорились с клиентом?',
        lead: 'Бон заказа: черновик, «Выдать» замораживает документ, PDF уходит письмом с адресом и датой, принятие, отмена с причиной и номер бона в форме счёта.',
        aria: 'Эпизод 15 — бон заказа',
        gains: [
          'Конец спорам о том, о чём договаривались.',
          'Документ, который не изменится задним числом.',
          'Отправка письмом — прямо из бона, с адресом и датой.',
        ],
      },
    },
  },
  {
    episode: '16-e16',
    group: 'exploitation',
    text: {
      fr: {
        kicker: 'Épisode 16',
        title: 'Où est le CMR signé, et pourquoi la facture ne part-elle pas sans lui ?',
        lead: 'Les six étapes du CMR, le filtre « En retard », la photo du CMR signé envoyée depuis le quai, et la facture de la mission qui ne s’émet pas tant que le CMR n’est pas signé.',
        aria: 'Épisode 16 — le CMR',
        gains: [
          'Chaque CMR en vue : chaque papier a son responsable.',
          'La signature visible sur la photo du quai, avant l’original.',
          'Une protection contre les factures impossibles à défendre.',
        ],
      },
      en: {
        kicker: 'Episode 16',
        title: 'Where is the signed CMR, and why won’t the invoice go out without it?',
        lead: 'The six steps of the CMR, the “Late” filter, the photo of the signed note sent from the dock, and the mission’s invoice that cannot be issued until the CMR is signed.',
        aria: 'Episode 16 — the CMR',
        gains: [
          'Every CMR in sight: every paper has an owner.',
          'The signature visible on the dock photo, before the original.',
          'Protection against invoices you can’t defend.',
        ],
      },
      es: {
        kicker: 'Episodio 16',
        title: '¿Dónde está el CMR firmado y por qué la factura no sale sin él?',
        lead: 'Los seis pasos del CMR, el filtro «Con retraso», la foto del CMR firmado enviada desde el muelle y la factura de la misión, que no se emite mientras el CMR no esté firmado.',
        aria: 'Episodio 16: el CMR',
        gains: [
          'Cada CMR a la vista: cada papel tiene un responsable.',
          'La firma visible en la foto del muelle, antes del original.',
          'Protección contra facturas imposibles de defender.',
        ],
      },
      ru: {
        kicker: 'Эпизод 16',
        title: 'Где подписанный CMR и почему без него не уходит фактура?',
        lead: 'Шесть шагов CMR, фильтр «Просрочено», фото подписанного бланка с рампы и фактура по рейсу, которую нельзя выставить, пока CMR не отмечен подписанным.',
        aria: 'Эпизод 16 — CMR',
        gains: [
          'Каждый CMR на виду: у каждой бумаги есть хозяин.',
          'Подпись видна по фото с рампы, ещё до оригинала.',
          'Защита от фактур, которые невозможно отстоять.',
        ],
      },
    },
  },
  {
    episode: '17-e17',
    group: 'parc',
    text: {
      fr: {
        kicker: 'Épisode 17',
        title: 'Comment savoir au bureau, avant le départ, qu’un papier est expiré ?',
        lead: 'Les papiers du tracteur et du chauffeur, la barre de validité, l’écran « Documents à renouveler », les alertes à trente, quinze et sept jours — et le refus d’affecter un chauffeur dont le permis a expiré.',
        aria: 'Épisode 17 — les documents et échéances',
        gains: [
          'Le papier expiré se voit au bureau, avant le départ, pas sur la route.',
          'La liste des renouvellements de la semaine, sans pointage à la main.',
          'Un chauffeur ou un véhicule avec un document obligatoire expiré ne peut pas être affecté.',
        ],
      },
      en: {
        kicker: 'Episode 17',
        title: 'How do you learn in the office, before departure, that a paper has expired?',
        lead: 'The tractor’s and driver’s papers, the validity bar, the “Documents to renew” screen, alerts at thirty, fifteen and seven days — and the refusal to assign a driver whose licence has expired.',
        aria: 'Episode 17 — documents and deadlines',
        gains: [
          'An expired paper shows up in the office, before departure, not on the road.',
          'This week’s renewals in one list, no manual cross-checking.',
          'A driver or vehicle with an expired required document can’t be assigned.',
        ],
      },
      es: {
        kicker: 'Episodio 17',
        title: '¿Cómo saber en la oficina, antes de salir, que un papel ha caducado?',
        lead: 'Los papeles del tractor y del conductor, la barra de validez, la pantalla «Documentos por renovar», las alertas a treinta, quince y siete días, y el rechazo de asignar a un conductor con el permiso de conducir caducado.',
        aria: 'Episodio 17: documentos y vencimientos',
        gains: [
          'El papel caducado se ve en la oficina, antes de salir, no en la carretera.',
          'Las renovaciones de la semana en una lista, sin cotejo manual.',
          'Un conductor o vehículo con un documento obligatorio caducado no se puede asignar.',
        ],
      },
      ru: {
        kicker: 'Эпизод 17',
        title: 'Как узнать в офисе, до выезда, что бумага просрочена?',
        lead: 'Бумаги тягача и водителя, полоска срока, экран «Документы к продлению», предупреждения за тридцать, пятнадцать и семь дней — и отказ назначить водителя с просроченными правами.',
        aria: 'Эпизод 17 — документы и сроки',
        gains: [
          'Просроченную бумагу видно в офисе — до выезда, а не на дороге.',
          'Список продлений на неделю — без ручной сверки.',
          'С просроченным обязательным документом водителя и машину не назначить.',
        ],
      },
    },
  },
  {
    episode: '18-e18',
    group: 'parc',
    text: {
      fr: {
        kicker: 'Épisode 18',
        title: 'Et si le camion d’un partenaire transporte la marchandise de votre client ?',
        lead: 'La fiche du sous-traitant avec fiabilité, ponctualité et étoiles, le refus d’affecter un camion dont l’assurance a expiré, le partenaire sur le tronçon du voyage et le rapprochement « convenu contre facturé ».',
        aria: 'Épisode 18 — les partenaires',
        gains: [
          'Le camion d’un partenaire avec une assurance expirée n’est pas affecté à votre voyage.',
          'Le prix convenu est rapproché de la facture du partenaire, mois par mois, sans seuil.',
          'Fiabilité et ponctualité tirées des faits, à côté de votre note, pas à sa place.',
        ],
      },
      en: {
        kicker: 'Episode 18',
        title: 'What if a partner’s truck carries your client’s cargo?',
        lead: 'The subcontractor’s record with reliability, punctuality and stars, the refusal to assign a truck with expired insurance, the partner on the trip leg and the “agreed versus billed” reconciliation.',
        aria: 'Episode 18 — partners',
        gains: [
          'A partner’s truck with expired insurance won’t be put on your trip.',
          'The agreed price is checked against the partner’s bill, month by month, with no threshold.',
          'Reliability and punctuality from facts, next to your rating, not instead of it.',
        ],
      },
      es: {
        kicker: 'Episodio 18',
        title: '¿Y si el camión de un socio lleva la carga de su cliente?',
        lead: 'La ficha del subcontratista con fiabilidad, puntualidad y estrellas, el rechazo de asignar un camión con el seguro caducado, el socio en el tramo del viaje y la conciliación «acordado frente a facturado».',
        aria: 'Episodio 18: los socios',
        gains: [
          'Un camión ajeno con el seguro caducado no entra en su viaje.',
          'El precio acordado se concilia con la factura del socio, mes a mes y sin umbral.',
          'Fiabilidad y puntualidad basadas en hechos, junto a su nota y no en su lugar.',
        ],
      },
      ru: {
        kicker: 'Эпизод 18',
        title: 'Что, если груз клиента везёт машина партнёра?',
        lead: 'Карточка субподрядчика с надёжностью, пунктуальностью и звёздами, отказ назначить машину с просроченной страховкой, партнёр на плече рейса и сверка «договорено против выставлено».',
        aria: 'Эпизод 18 — партнёры',
        gains: [
          'Чужая машина с просроченной страховкой не встанет на ваш рейс.',
          'Согласованная цена сверяется со счётом партнёра — по месяцам, без порога.',
          'Надёжность и пунктуальность — по фактам, рядом с вашей оценкой, а не вместо неё.',
        ],
      },
    },
  },
  {
    episode: '19-e19',
    group: 'parc',
    text: {
      fr: {
        kicker: 'Épisode 19',
        title: 'Combien consomme vraiment chaque camion, et comment ne pas compter un plein deux fois ?',
        lead: 'Le journal des pleins, deux lignes rapprochées en un seul plein, un compteur qui ne recule pas, la consommation sur trente et quatre-vingt-dix jours face à la norme, et l’import du relevé de carte avec aperçu.',
        aria: 'Épisode 19 — le carburant',
        gains: [
          'La consommation réelle de chaque camion face à votre norme.',
          'Le relevé de carte rapproché des reçus, et un compteur qui ne recule pas.',
          'Le relevé de carte en un fichier, avec aperçu, sans saisie.',
        ],
      },
      en: {
        kicker: 'Episode 19',
        title: 'How much does each truck really burn, and how do you avoid counting a fill-up twice?',
        lead: 'The fill-up log, two lines matched into a single fill-up, an odometer that never goes back, consumption over thirty and ninety days against the norm, and the card statement import with a preview.',
        aria: 'Episode 19 — fuel',
        gains: [
          'Real consumption for each truck against your norm.',
          'Card statements matched to receipts, and an odometer that never goes back.',
          'The card statement in one file, with a preview, no typing.',
        ],
      },
      es: {
        kicker: 'Episodio 19',
        title: '¿Cuánto consume de verdad cada camión y cómo evitar contar un repostaje dos veces?',
        lead: 'El registro de repostajes, dos líneas conciliadas en un solo repostaje, un cuentakilómetros que no retrocede, el consumo a treinta y noventa días frente a la norma y la importación del extracto de la tarjeta con vista previa.',
        aria: 'Episodio 19: el combustible',
        gains: [
          'El consumo real de cada camión frente a su norma.',
          'El extracto conciliado con los recibos y un cuentakilómetros que no retrocede.',
          'El extracto de la tarjeta en un archivo, con vista previa, sin teclear.',
        ],
      },
      ru: {
        kicker: 'Эпизод 19',
        title: 'Сколько на самом деле расходует каждая машина и как не посчитать заправку дважды?',
        lead: 'Журнал заправок, две строки, сведённые в одну заправку, одометр, который не едет назад, расход за тридцать и девяносто дней против нормы и импорт выписки карты с предпросмотром.',
        aria: 'Эпизод 19 — топливо',
        gains: [
          'Реальный расход каждой машины против вашей нормы.',
          'Сверка выписки карты с чеками и одометр, который не едет назад.',
          'Выписка карты — одним файлом, с предпросмотром, без ручного ввода.',
        ],
      },
    },
  },
  {
    episode: '20-e20',
    group: 'parc',
    text: {
      fr: {
        kicker: 'Épisode 20',
        title: 'Combien coûte un camion à l’arrêt, et quand faut-il le réviser ?',
        lead: 'Les heures d’arrêt sur quatre-vingt-dix jours, l’ordre de réparation avec ou sans immobilisation, le montant tiré de la facture du garage, le plan d’entretien, les pneus et l’onglet « Parc ».',
        aria: 'Épisode 20 — l’entretien',
        gains: [
          'Un chiffre d’arrêt que presque personne n’a.',
          'Le coût des réparations vient des factures du garage, sans double saisie.',
          'Des échéances calculées sur le vrai compteur et les ordres clôturés, pas de mémoire.',
        ],
      },
      en: {
        kicker: 'Episode 20',
        title: 'What does a truck standing still cost, and when is it due for service?',
        lead: 'The downtime hours over ninety days, the work order with or without immobilisation, the amount taken from the garage’s bill, the service schedule, the tyres and the “Fleet” tab.',
        aria: 'Episode 20 — maintenance',
        gains: [
          'A downtime figure almost nobody else has.',
          'Repair costs come from the garage’s bills, never typed twice.',
          'Service due dates from the real odometer and closed orders, not from memory.',
        ],
      },
      es: {
        kicker: 'Episodio 20',
        title: '¿Cuánto cuesta un camión parado y cuándo toca revisarlo?',
        lead: 'Las horas de parada a noventa días, la orden de reparación con o sin inmovilización, el importe sacado de la factura del taller, el plan de mantenimiento, los neumáticos y la pestaña «Flota».',
        aria: 'Episodio 20: el mantenimiento',
        gains: [
          'Una cifra de parada que casi nadie tiene.',
          'El coste de las reparaciones viene de las facturas del taller, sin doble entrada.',
          'Vencimientos calculados con el cuentakilómetros real y las órdenes cerradas, no de memoria.',
        ],
      },
      ru: {
        kicker: 'Эпизод 20',
        title: 'Сколько стоит простой машины и когда ей пора на ТО?',
        lead: 'Часы простоя за девяносто дней, наряд с иммобилизацией или без, сумма из счёта гаража, регламент ТО, шины и вкладка «Парк».',
        aria: 'Эпизод 20 — обслуживание',
        gains: [
          'Цифра простоя, которой почти ни у кого нет.',
          'Затраты на ремонт — из счетов гаража, без второго ввода.',
          'Сроки ТО — от реального одометра и закрытых нарядов, а не по памяти.',
        ],
      },
    },
  },
  {
    episode: '21-e21',
    group: 'parc',
    text: {
      fr: {
        kicker: 'Épisode 21',
        title: 'Combien coûte ce tracteur précis, par mois et au kilomètre ?',
        lead: 'Le prix de revient d’une machine par poste, l’amortissement tiré du prix saisi une fois, la machine rattachée aux lignes des factures fournisseur, et un tiret quand il manque une donnée.',
        aria: 'Épisode 21 — le coût d’une machine',
        gains: [
          'Le coût au kilomètre de chaque tracteur, sous les yeux quand vous chiffrez une mission.',
          'Assurance et leasing rattachés à la machine, pas noyés dans les frais généraux.',
          'Garder ou vendre : une décision sur des chiffres, pas sur une impression.',
        ],
      },
      en: {
        kicker: 'Episode 21',
        title: 'How much does this particular tractor cost, per month and per kilometre?',
        lead: 'A machine’s cost broken down by item, depreciation drawn from the price entered once, the machine tied to supplier bill lines, and a dash when a figure is missing.',
        aria: 'Episode 21 — machine cost',
        gains: [
          'The cost per kilometre of each tractor, in view when you price a trip.',
          'Insurance and leasing tied to the machine, not lost in overheads.',
          'Keep or sell: a decision based on figures, not on gut feeling.',
        ],
      },
      es: {
        kicker: 'Episodio 21',
        title: '¿Cuánto cuesta esta tractora concreta, al mes y por kilómetro?',
        lead: 'El precio de coste de una máquina por partidas, la amortización sacada del precio introducido una vez, la máquina vinculada a las líneas de las facturas de proveedor y un guion cuando falta un dato.',
        aria: 'Episodio 21: el coste de una máquina',
        gains: [
          'El coste por kilómetro de cada tractora, a la vista cuando presupuesta una misión.',
          'Seguro y leasing vinculados a la máquina, no diluidos en los gastos generales.',
          'Conservar o vender: una decisión basada en cifras, no en impresiones.',
        ],
      },
      ru: {
        kicker: 'Эпизод 21',
        title: 'Сколько стоит именно этот тягач — в месяц и за километр?',
        lead: 'Себестоимость машины по статьям, амортизация из цены, введённой один раз, машина на строках счетов поставщика и прочерк, когда не хватает данных.',
        aria: 'Эпизод 21 — себестоимость машины',
        gains: [
          'Цена километра конкретного тягача — на виду, когда считаете смету рейса.',
          'Страховка и лизинг привязаны к машине, а не растворены в накладных.',
          'Решения «держать или продавать» — на цифрах, а не на ощущениях.',
        ],
      },
    },
  },
  {
    episode: '22-e22',
    group: 'direction',
    text: {
      fr: {
        kicker: 'Épisode 22',
        title: 'Que doit-on faire aujourd’hui, sans être noyé sous les notifications ?',
        lead: 'Un fil court d’alertes : vingt et une règles, seuils réglables, facture fournisseur critique au quinzième jour, effets à porter à la banque, une seule alerte vivante par problème.',
        aria: 'Épisode 22 — les alertes',
        gains: [
          'Les rappels ne reposent plus sur la mémoire d’une seule personne.',
          'Un fil sans spam, auquel on fait encore confiance dans un an.',
          'Les risques fournisseurs et effets se voient à l’avance.',
        ],
      },
      en: {
        kicker: 'Episode 22',
        title: 'What needs doing today, without drowning in notifications?',
        lead: 'A short alert feed: twenty-one rules, adjustable thresholds, a supplier bill turning critical on day fifteen, bills of exchange to take to the bank, and one live alert per problem.',
        aria: 'Episode 22 — alerts',
        gains: [
          'Reminders no longer live in one person’s memory.',
          'A feed without spam that people still trust a year on.',
          'Supplier and bill-of-exchange risks show up in advance.',
        ],
      },
      es: {
        kicker: 'Episodio 22',
        title: '¿Qué hay que hacer hoy, sin ahogarse en notificaciones?',
        lead: 'Una lista corta de alertas: veintiuna reglas, umbrales ajustables, factura de proveedor crítica al decimoquinto día, letras que llevar al banco y una sola alerta viva por problema.',
        aria: 'Episodio 22: las alertas',
        gains: [
          'Los recordatorios ya no dependen de la memoria de una sola persona.',
          'Una lista sin spam en la que se sigue confiando dentro de un año.',
          'Los riesgos de proveedores y letras se ven con antelación.',
        ],
      },
      ru: {
        kicker: 'Эпизод 22',
        title: 'Что нужно сделать сегодня — и не утонуть в уведомлениях?',
        lead: 'Короткая лента оповещений: двадцать одно правило, настраиваемые пороги, счёт поставщика, критичный на пятнадцатый день, тратты, которые пора нести в банк, и одно живое оповещение на проблему.',
        aria: 'Эпизод 22 — оповещения',
        gains: [
          'Напоминания больше не держатся в памяти одного человека.',
          'Лента без спама, которой доверяют и через год.',
          'Риски по поставщикам и траттам видны заранее.',
        ],
      },
    },
  },
  {
    episode: '23-e23',
    group: 'finance',
    text: {
      fr: {
        kicker: 'Épisode 23',
        title: 'Comment passe-t-on de la mission terminée à la facture, sans trou de numérotation ?',
        lead: 'On choisit le client, on coche ses missions terminées, le système propose l’exonération de TVA à l’export, attribue le numéro à l’émission, corrige par un avoir et enregistre le règlement comme une ligne de journal.',
        aria: 'Épisode 23 — de la mission à la facture',
        gains: [
          'Des numéros sans trous, une série par année d’émission.',
          'Plusieurs missions, une seule facture.',
          'Le règlement est saisi par le comptable ou le propriétaire, pas par les ventes.',
        ],
      },
      en: {
        kicker: 'Episode 23',
        title: 'How do you go from a finished trip to an invoice with no gap in the numbering?',
        lead: 'You pick the client and tick its completed trips, the system offers the export VAT exemption, assigns the number at issue, corrects with a credit note and records the payment as a journal line.',
        aria: 'Episode 23 — from trip to invoice',
        gains: [
          'Gap-free numbers, one series per year of issue.',
          'Several trips, one invoice.',
          'Payments are recorded by the accountant or the owner, not by sales.',
        ],
      },
      es: {
        kicker: 'Episodio 23',
        title: '¿Cómo se pasa del viaje terminado a la factura, sin huecos en la numeración?',
        lead: 'Se elige el cliente y se marcan sus viajes terminados, el sistema propone la exención de IVA en la exportación, asigna el número al emitir, corrige con un abono y registra el cobro como una línea del registro.',
        aria: 'Episodio 23: de la misión a la factura',
        gains: [
          'Números sin huecos, una serie por año de emisión.',
          'Varios viajes, una sola factura.',
          'Los cobros los registra el contable o el propietario, no ventas.',
        ],
      },
      ru: {
        kicker: 'Эпизод 23',
        title: 'Как из завершённого рейса получить фактуру — и чтобы в нумерации не было дыр?',
        lead: 'Выбираете клиента, отмечаете его завершённые рейсы, система сама предлагает освобождение от НДС на экспорте, присваивает номер при выставлении, ошибку исправляет авуаром, а оплата — строка журнала.',
        aria: 'Эпизод 23 — от рейса до фактуры',
        gains: [
          'Номера без дыр, серия — по году выставления.',
          'Несколько рейсов — одна фактура.',
          'Оплату записывают бухгалтер или владелец, а не отдел продаж.',
        ],
      },
    },
  },
  {
    episode: '24-e24',
    group: 'finance',
    text: {
      fr: {
        kicker: 'Épisode 24',
        title: 'Comment tenir les avances et les notes de frais des chauffeurs sans cahier ?',
        lead: 'L’avance calculée selon le barème, le formulaire à signer, la file des justificatifs avec photo, le remboursement, deux soldes séparés en dirhams et en euros — et le journal, où chaque mouvement est une ligne.',
        aria: 'Épisode 24 — avances et notes de frais',
        gains: [
          'Chaque mouvement est une ligne du journal : le solde se prouve.',
          'Justificatifs photo depuis le téléphone du chauffeur ; tout refus est motivé.',
          'Dirhams et euros : des soldes séparés, sans conversion.',
        ],
      },
      en: {
        kicker: 'Episode 24',
        title: 'How do you keep driver advances and expense claims without a notebook?',
        lead: 'The advance calculated from the scale, the form to sign, the queue of photo receipts, the reimbursement, two separate balances in dirhams and euros — and the ledger, where every movement is a line.',
        aria: 'Episode 24 — advances and expense claims',
        gains: [
          'Every movement is a ledger line: the balance can be proven.',
          'Photo receipts from the driver’s phone; every rejection has a reason.',
          'Dirhams and euros: separate balances, no conversion.',
        ],
      },
      es: {
        kicker: 'Episodio 24',
        title: '¿Cómo llevar los anticipos y los gastos de los conductores sin cuaderno?',
        lead: 'El anticipo calculado según el baremo, el formulario para firmar, la cola de justificantes con foto, el reembolso, dos saldos separados en dírhams y en euros, y el registro, donde cada movimiento es una línea.',
        aria: 'Episodio 24: anticipos y gastos',
        gains: [
          'Cada movimiento es una línea del registro: el saldo se puede demostrar.',
          'Justificantes con foto desde el teléfono del conductor; todo rechazo lleva motivo.',
          'Dírhams y euros: saldos separados, sin conversión.',
        ],
      },
      ru: {
        kicker: 'Эпизод 24',
        title: 'Как вести авансы и отчёты водителей по расходам без тетрадки?',
        lead: 'Аванс по бареме, бланк на подпись, очередь чеков с фото, возмещение, два отдельных баланса — в дирхамах и в евро, — и журнал, где каждое движение — отдельная строка.',
        aria: 'Эпизод 24 — авансы и отчёты по расходам',
        gains: [
          'Каждое движение — строка журнала: сальдо можно доказать.',
          'Чеки с фото — с телефона водителя; отказ — всегда с причиной.',
          'Дирхамы и евро — отдельные балансы, без конвертации.',
        ],
      },
    },
  },
  {
    episode: '25-e25',
    group: 'finance',
    text: {
      fr: {
        kicker: 'Épisode 25',
        title: 'Combien d’argent faudra-t-il décaisser sur les treize prochaines semaines, et quand ?',
        lead: 'L’échéancier des achats par date, la facture rattachée à l’engagement qu’elle réalise, le refus d’un montant inattendu, l’unicité du numéro par fournisseur et le coût réel qui apparaît sur la mission.',
        aria: 'Épisode 25 — l’échéancier des achats',
        gains: [
          'Un échéancier sur 13 semaines, sans double comptage.',
          'Les écarts de facture, acceptés uniquement de façon explicite.',
          'La même facture fournisseur ne se saisit pas deux fois.',
        ],
      },
      en: {
        kicker: 'Episode 25',
        title: 'How much cash will you need to pay out over the next thirteen weeks, and when?',
        lead: 'The purchase schedule by date, the bill attached to the commitment it fulfils, the refusal of an unexpected amount, a bill number unique per supplier, and the real cost showing up on the mission.',
        aria: 'Episode 25 — the purchase schedule',
        gains: [
          'A 13-week payment schedule with nothing counted twice.',
          'Bill differences accepted only explicitly.',
          'The same supplier bill can’t be entered twice.',
        ],
      },
      es: {
        kicker: 'Episodio 25',
        title: '¿Cuánto dinero habrá que desembolsar en las próximas trece semanas, y cuándo?',
        lead: 'El calendario de compras por fecha, la factura vinculada al compromiso que cumple, el rechazo de un importe inesperado, el número único por proveedor y el coste real que aparece en la misión.',
        aria: 'Episodio 25: el calendario de compras',
        gains: [
          'Un calendario de pagos a 13 semanas, sin doble cómputo.',
          'Las diferencias de factura, aceptadas solo de forma explícita.',
          'La misma factura de proveedor no se registra dos veces.',
        ],
      },
      ru: {
        kicker: 'Эпизод 25',
        title: 'Сколько денег понадобится выплатить за ближайшие тринадцать недель — и когда именно?',
        lead: 'Календарь закупок по датам, счёт, привязанный к обязательству, которое он исполняет, отказ при неожиданной сумме, уникальный номер счёта у каждого поставщика и реальная стоимость прямо на рейсе.',
        aria: 'Эпизод 25 — календарь закупок',
        gains: [
          'Платёжный календарь на 13 недель без двойного счёта.',
          'Расхождения со счетами — только с явной отметкой.',
          'Один и тот же счёт поставщика не ввести дважды.',
        ],
      },
    },
  },
  {
    episode: '26-e26',
    group: 'finance',
    text: {
      fr: {
        kicker: 'Épisode 26',
        title: 'Combien d’effets dorment dans votre coffre, et pour quel montant ?',
        lead: 'Le portefeuille d’effets — traites, LCN, chèques différés —, leurs statuts, la couverture croisée des factures, l’escompte avec l’agio, l’effet impayé qui rouvre la facture et le coût sur douze mois.',
        aria: 'Épisode 26 — les effets de commerce',
        gains: [
          'Une réponse exacte : combien d’effets dans le coffre, et pour quel montant.',
          'Des créances qui tiennent compte des effets, correctement.',
          'Le coût réel des agios et des impayés sur douze mois.',
        ],
      },
      en: {
        kicker: 'Episode 26',
        title: 'How many bills of exchange are sitting in your safe, and for how much?',
        lead: 'The bills portfolio — bills of exchange, LCN, post-dated cheques — and their statuses, cross coverage of invoices, discounting with agio, the unpaid bill that reopens the invoice, and the twelve-month cost.',
        aria: 'Episode 26 — bills of exchange',
        gains: [
          'An exact answer: how much paper is in the safe, and for how much.',
          'Receivables that handle bills of exchange correctly.',
          'The real cost of agio and returns over twelve months.',
        ],
      },
      es: {
        kicker: 'Episodio 26',
        title: '¿Cuántos efectos hay en su caja fuerte, y por qué importe?',
        lead: 'La cartera de efectos —letras, LCN, cheques con fecha diferida—, sus estados, la cobertura cruzada de facturas, el descuento con su agio, el efecto impagado que reabre la factura y el coste a doce meses.',
        aria: 'Episodio 26: los efectos de comercio',
        gains: [
          'Una respuesta exacta: cuántos efectos hay en la caja fuerte y por qué importe.',
          'Cuentas por cobrar que tratan bien los efectos.',
          'El coste real del agio y los impagados en doce meses.',
        ],
      },
      ru: {
        kicker: 'Эпизод 26',
        title: 'Сколько векселей лежит у вас в сейфе — и на какую сумму?',
        lead: 'Портфель бумаг — тратты, LCN, чеки с отсрочкой, — их статусы, перекрёстное покрытие фактур, дисконт с агио, возвращённый неоплаченным вексель, который открывает фактуру заново, и стоимость за двенадцать месяцев.',
        aria: 'Эпизод 26 — векселя и чеки с отсрочкой',
        gains: [
          'Точный ответ: сколько бумаг в сейфе и на какую сумму.',
          'Дебиторка, которая учитывает векселя правильно.',
          'Реальная стоимость агио и возвратов за двенадцать месяцев.',
        ],
      },
    },
  },
  {
    episode: '27-e27',
    group: 'finance',
    text: {
      fr: {
        kicker: 'Épisode 27',
        title: 'Comment rapprocher le relevé de la banque en minutes, et non en heures ?',
        lead: 'Import du relevé en CSV ou Excel, doublons marqués, rapprochement automatique de l’évident, vraie écriture au journal des règlements, position à 91 jours et le chiffre « Non rapproché ».',
        aria: 'Épisode 27 — le rapprochement bancaire',
        gains: [
          'Le rapprochement bancaire en quelques minutes au lieu d’heures en fin de mois.',
          'Une position à 91 jours où rien n’est compté deux fois.',
          'Une limite de précision visible : ce qui n’est pas encore expliqué.',
        ],
      },
      en: {
        kicker: 'Episode 27',
        title: 'How do you reconcile the bank statement in minutes, not hours?',
        lead: 'The statement imported as CSV or Excel, duplicates flagged, the obvious matched automatically, a real entry in the payments journal, the 91-day position and the “Unreconciled” figure.',
        aria: 'Episode 27 — bank reconciliation',
        gains: [
          'Statement reconciliation in minutes instead of hours at month-end.',
          'A 91-day position where nothing is counted twice.',
          'A visible limit of accuracy: what’s still unexplained.',
        ],
      },
      es: {
        kicker: 'Episodio 27',
        title: '¿Cómo conciliar el extracto del banco en minutos y no en horas?',
        lead: 'La importación del extracto en CSV o Excel, los duplicados marcados, la conciliación automática de lo evidente, un asiento real en el registro de cobros, la posición a 91 días y la cifra «Sin conciliar».',
        aria: 'Episodio 27: la conciliación bancaria',
        gains: [
          'La conciliación del extracto, en minutos en lugar de horas a final de mes.',
          'Una posición a 91 días en la que nada se cuenta dos veces.',
          'Un límite de precisión visible: lo que aún no tiene explicación.',
        ],
      },
      ru: {
        kicker: 'Эпизод 27',
        title: 'Как свести банковскую выписку за минуты, а не за часы?',
        lead: 'Импорт выписки в CSV или Excel, дубликаты помечены, очевидное сводится само, настоящая запись в журнале оплат, позиция на 91 день и цифра «Не сведено».',
        aria: 'Эпизод 27 — сведение банковской выписки',
        gains: [
          'Сведение выписки — минуты вместо часов в конце месяца.',
          'Позиция на 91 день, в которой ничего не посчитано дважды.',
          'Видимая граница точности: что ещё не объяснено.',
        ],
      },
    },
  },
  {
    episode: '28-e28',
    group: 'finance',
    text: {
      fr: {
        kicker: 'Épisode 28',
        title: 'Quelle semaine l’argent manquera-t-il, et peut-on le voir un mois et demi avant ?',
        lead: 'La prévision sur treize semaines, le seuil à la base des barres, le point bas qui s’ouvre jusqu’aux pièces, le scénario « le débiteur paie un mois plus tard », le bouton « Figer » et l’onglet Précision.',
        aria: 'Épisode 28 — la prévision de trésorerie',
        gains: [
          'Le point de rupture, un mois et demi à l’avance, pas la veille.',
          'Une prévision qu’on peut vérifier pièce par pièce.',
          'Un argument prêt pour la banque : scénarios et historique de précision.',
        ],
      },
      en: {
        kicker: 'Episode 28',
        title: 'Which week will the cash run short, and can you see it a month and a half ahead?',
        lead: 'The thirteen-week forecast, your floor at the base of the bars, the low point that opens down to the documents, the “main debtor pays a month late” scenario, the “Freeze” button and the Accuracy tab.',
        aria: 'Episode 28 — the cash forecast',
        gains: [
          'The shortfall week, a month and a half ahead, not the day before.',
          'A forecast you can check document by document.',
          'A ready-made case for your bank: scenarios and an accuracy record.',
        ],
      },
      es: {
        kicker: 'Episodio 28',
        title: '¿En qué semana faltará el dinero, y se puede ver con mes y medio de antelación?',
        lead: 'La previsión a trece semanas, el umbral en la base de las barras, el punto más bajo que se abre hasta los documentos, el escenario «el principal deudor paga un mes más tarde», el botón «Fijar» y la pestaña Precisión.',
        aria: 'Episodio 28: la previsión de tesorería',
        gains: [
          'La semana crítica, con mes y medio de antelación, no la víspera.',
          'Una previsión que se puede comprobar documento a documento.',
          'Un argumento listo para el banco: escenarios e historial de precisión.',
        ],
      },
      ru: {
        kicker: 'Эпизод 28',
        title: 'В какую неделю не хватит денег — и можно ли увидеть это за полтора месяца?',
        lead: 'Прогноз на тринадцать недель, ваш порог в основании столбцов, низшая точка, которая раскрывается до документов, сценарий «главный должник платит на месяц позже», кнопка «Зафиксировать» и вкладка «Точность».',
        aria: 'Эпизод 28 — прогноз денежных средств',
        gains: [
          'Неделя кассового разрыва — за полтора месяца, а не за день.',
          'Прогноз, который можно разобрать до каждой бумажки.',
          'Готовый аргумент для банка: сценарии и история точности.',
        ],
      },
    },
  },
  {
    episode: '29-e29',
    group: 'finance',
    text: {
      fr: {
        kicker: 'Épisode 29',
        title: 'Que payons-nous lundi, et comment le préparer en quelques minutes ?',
        lead: 'L’écran « Ordres de paiement » : quatre chiffres, la file des factures et engagements, l’ordre en brouillon, l’export vers la banque en ligne, « Sans trace en banque » et la double validation.',
        aria: 'Épisode 29 — les ordres de paiement',
        gains: [
          'Les virements du lundi en quelques minutes, sans ressaisir un RIB.',
          'Une facture n’entre jamais deux fois dans les ordres.',
          'Votre banque reste la vôtre : aucun accès à votre compte.',
        ],
      },
      en: {
        kicker: 'Episode 29',
        title: 'What do we pay on Monday, and how do you prepare it in minutes?',
        lead: 'The “Payment orders” screen: four figures, the queue of bills and commitments, the draft order, the export to your online bank, “No trace at the bank” and double validation.',
        aria: 'Episode 29 — payment orders',
        gains: [
          'Monday’s payments in minutes, without retyping bank details.',
          'One bill never goes into orders twice.',
          'Your bank stays yours: no access to your account needed.',
        ],
      },
      es: {
        kicker: 'Episodio 29',
        title: '¿Qué pagamos el lunes, y cómo prepararlo en unos minutos?',
        lead: 'La pantalla «Órdenes de pago»: cuatro cifras, la cola de facturas y compromisos, la orden en borrador, la exportación a su banca electrónica, «Sin rastro en el banco» y la doble validación.',
        aria: 'Episodio 29: las órdenes de pago',
        gains: [
          'Los pagos del lunes en minutos, sin volver a teclear un RIB.',
          'Una factura nunca entra dos veces en las órdenes.',
          'Su banco sigue siendo solo suyo: no hace falta acceso a su cuenta.',
        ],
      },
      ru: {
        kicker: 'Эпизод 29',
        title: 'Что платим в понедельник — и как подготовить это за несколько минут?',
        lead: 'Экран «Платёжные поручения»: четыре цифры, очередь счетов и обязательств, поручение-черновик, экспорт файла в онлайн-банк, статус «Нет следа в банке» и двойное подтверждение.',
        aria: 'Эпизод 29 — платёжные поручения',
        gains: [
          'Платежи на понедельник — за минуты, без перебивки реквизитов.',
          'Один счёт не попадёт в ордера дважды.',
          'Ваш банк остаётся только вашим: доступ к счёту не нужен.',
        ],
      },
    },
  },
  {
    episode: '30-e30',
    group: 'finance',
    text: {
      fr: {
        kicker: 'Épisode 30',
        title: 'Quelle est vraiment la marge d’une mission, et quel chiffre est un fait ?',
        lead: 'Deux marges par mission — directe et après frais généraux —, les documents derrière chaque chiffre, les règles de répartition visibles avec leurs cinq bases, le bloc « Non facturé » et l’onglet « Par client ».',
        aria: 'Épisode 30 — la marge par mission',
        gains: [
          'La marge de chaque mission, jusqu’à la ligne du document.',
          'On voit quels clients et quelles missions font vraiment vivre l’entreprise.',
          'Les hypothèses sous contrôle, pas cachées dans des formules.',
        ],
      },
      en: {
        kicker: 'Episode 30',
        title: 'What is the real margin of a mission, and which figure is a fact?',
        lead: 'Two margins per mission — direct and after overheads — the documents behind each figure, the visible allocation rules with their five bases, the “Not invoiced” block and the “By client” tab.',
        aria: 'Episode 30 — margin per mission',
        gains: [
          'The margin of every trip, down to the document line.',
          'You see which clients and trips really feed the company.',
          'Assumptions under control, not hidden in formulas.',
        ],
      },
      es: {
        kicker: 'Episodio 30',
        title: '¿Cuál es de verdad el margen de una misión, y qué cifra es un hecho?',
        lead: 'Dos márgenes por misión —directo y tras gastos generales—, los documentos detrás de cada cifra, las reglas de reparto visibles con sus cinco bases, el bloque «Sin facturar» y la pestaña «Por cliente».',
        aria: 'Episodio 30: el margen por misión',
        gains: [
          'El margen de cada misión, hasta la línea del documento.',
          'Se ve qué clientes y qué misiones sostienen de verdad la empresa.',
          'Las hipótesis bajo control, no escondidas en fórmulas.',
        ],
      },
      ru: {
        kicker: 'Эпизод 30',
        title: 'Какова на самом деле маржа рейса — и какая из двух цифр является фактом?',
        lead: 'Две маржи на каждом рейсе — прямая и после накладных расходов, — документы за каждой цифрой, видимые правила распределения с пятью базами, блок «Не выставлено» и вкладка «По клиентам».',
        aria: 'Эпизод 30 — маржа по рейсу',
        gains: [
          'Маржа каждого рейса — до строки документа.',
          'Видно, какие клиенты и рейсы реально кормят компанию.',
          'Допущения под контролем, а не спрятаны в формулах.',
        ],
      },
    },
  },
  {
    episode: '31-e31',
    group: 'direction',
    text: {
      fr: {
        kicker: 'Épisode 31',
        title: 'Le prochain camion sera-t-il rentable, et que disent vraiment vos chiffres ?',
        lead: 'Le conseiller d’achat : un formulaire minimal, le verdict à partir de l’historique, la pastille « utilisation sous 60 % », chaque hypothèse avec sa source, et le cas « remplacer plutôt qu’acheter ».',
        aria: 'Épisode 31 — le prochain camion',
        gains: [
          'Une décision d’achat fondée sur vos données, pas sur une brochure.',
          'Chaque hypothèse avec sa source affichée.',
          'Une alerte quand la flotte est sous-utilisée.',
        ],
      },
      en: {
        kicker: 'Episode 31',
        title: 'Will the next truck pay off, and what do your own figures really say?',
        lead: 'The purchase advisor: a minimal form, the verdict drawn from your history, the “utilization under 60%” pill, every assumption with its source, and the “replace instead of buy” case.',
        aria: 'Episode 31 — the next truck',
        gains: [
          'A buying decision based on your data, not on a brochure.',
          'Every assumption with its source shown.',
          'A warning when the fleet is under-used.',
        ],
      },
      es: {
        kicker: 'Episodio 31',
        title: '¿Será rentable el próximo camión, y qué dicen de verdad sus cifras?',
        lead: 'El asesor de compra: un formulario mínimo, el veredicto a partir del historial, la etiqueta «utilización por debajo del 60 %», cada supuesto con su origen y el caso «sustituir en lugar de comprar».',
        aria: 'Episodio 31: el próximo camión',
        gains: [
          'Una decisión de compra basada en sus datos, no en un folleto.',
          'Cada supuesto con su origen a la vista.',
          'Un aviso cuando la flota está infrautilizada.',
        ],
      },
      ru: {
        kicker: 'Эпизод 31',
        title: 'Окупится ли следующий грузовик — и что на самом деле говорят ваши цифры?',
        lead: 'Советник по покупке: минимальная форма, вердикт по вашей истории, метка «загрузка ниже 60 %», у каждого допущения свой источник и вариант «заменить, а не купить».',
        aria: 'Эпизод 31 — следующий грузовик',
        gains: [
          'Решение о покупке — на ваших данных, а не на брошюре.',
          'Каждое допущение — с подписанным источником.',
          'Предупреждение, если парк недогружен.',
        ],
      },
    },
  },
  {
    episode: '32-e32',
    group: 'direction',
    text: {
      fr: {
        kicker: 'Épisode 32',
        title: 'Comment voir le mois de l’entreprise en une minute ?',
        lead: 'Une bande sombre avec chiffre d’affaires, marge directe, cash et impayés, les « Décisions attendues » issues de vos seuils, les corridors par marge au kilomètre et les rapports Excel.',
        aria: 'Épisode 32 — le tableau de bord du directeur',
        gains: [
          'Le mois de l’entreprise en une minute.',
          'Des décisions qu’on n’oublie pas le jour même.',
          'Les corridors qui nourrissent, et ceux qui mangent la marge.',
        ],
      },
      en: {
        kicker: 'Episode 32',
        title: 'How can you see the company’s month in one minute?',
        lead: 'A dark band with turnover, direct margin, cash and arrears, the “Decisions pending” drawn from your thresholds, the corridors by margin per kilometre and the Excel reports.',
        aria: 'Episode 32 — the director’s dashboard',
        gains: [
          'The company’s month in a minute.',
          'Decisions that aren’t forgotten the same day.',
          'The corridors that feed you, and the ones that eat your margin.',
        ],
      },
      es: {
        kicker: 'Episodio 32',
        title: '¿Cómo ver el mes de la empresa en un minuto?',
        lead: 'Una banda oscura con facturación, margen directo, efectivo e impagados, las «Decisiones pendientes» derivadas de sus umbrales, los corredores por margen por kilómetro y los informes en Excel.',
        aria: 'Episodio 32: el panel del director',
        gains: [
          'El mes de la empresa en un minuto.',
          'Decisiones que no se olvidan el mismo día.',
          'Los corredores que alimentan y los que se comen el margen.',
        ],
      },
      ru: {
        kicker: 'Эпизод 32',
        title: 'Как увидеть месяц компании за одну минуту?',
        lead: 'Тёмная полоса с выручкой, прямой маржой, деньгами и просрочкой, «Ожидают решения» из ваших порогов, коридоры по марже на километр и отчёты в Excel.',
        aria: 'Эпизод 32 — панель директора',
        gains: [
          'Месяц компании — за минуту.',
          'Решения, которые не забываются в тот же день.',
          'Коридоры, которые кормят, и коридоры, которые съедают маржу.',
        ],
      },
    },
  },
  {
    episode: '33-s1',
    group: 'securite',
    text: {
      fr: {
        kicker: 'Sécurité 1',
        title: 'Mes données peuvent-elles se retrouver chez une autre entreprise ?',
        lead: 'L’isolation au niveau de la base, la vérification automatique de toutes les tables, un module arrêté qui ferme les écrans sans effacer les données, et la suppression de la démo qui laisse intact ce que vous avez saisi.',
        aria: 'Sécurité 1 — l’isolation des données',
        gains: [
          'Chaque entreprise est isolée dans la base elle-même : même une erreur du logiciel n’ouvre pas les lignes des autres.',
          'Un module arrêté ferme ses écrans, mais n’efface pas les données.',
          'La suppression de la démo ne touche pas à ce que vous avez saisi.',
        ],
      },
      en: {
        kicker: 'Security 1',
        title: 'Can my data ever end up in another company’s hands?',
        lead: 'Isolation in the database itself, the automatic check of every table, a stopped module that closes its screens without erasing data, and demo removal that leaves what you entered untouched.',
        aria: 'Security 1 — data isolation',
        gains: [
          'Every company is isolated in the database itself: even a software bug won’t open anyone else’s rows.',
          'A stopped module closes its screens but doesn’t erase the data.',
          'Removing the demo leaves what you entered yourself untouched.',
        ],
      },
      es: {
        kicker: 'Seguridad 1',
        title: '¿Pueden mis datos acabar en manos de otra empresa?',
        lead: 'El aislamiento en la propia base, la comprobación automática de todas las tablas, un módulo detenido que cierra sus pantallas sin borrar datos y la eliminación de la demo que respeta lo que usted introdujo.',
        aria: 'Seguridad 1: aislamiento de los datos',
        gains: [
          'Cada empresa está aislada en la propia base: ni un error del programa abre las filas de otros.',
          'Un módulo detenido cierra sus pantallas, pero no borra los datos.',
          'Eliminar la demo no toca lo que usted introdujo.',
        ],
      },
      ru: {
        kicker: 'Безопасность 1',
        title: 'Могут ли мои данные попасть к другой компании?',
        lead: 'Изоляция в самой базе, автоматическая проверка всех таблиц, остановленный модуль, который закрывает экраны, но не стирает данные, и удаление демо, не трогающее введённое вами.',
        aria: 'Безопасность 1 — изоляция данных',
        gains: [
          'Каждая компания изолирована в самой базе данных — даже ошибка в программе не откроет чужие строки.',
          'Остановленный модуль закрывает экраны, но не стирает данные.',
          'Удаление демо-данных не трогает то, что вы ввели сами.',
        ],
      },
    },
  },
  {
    episode: '34-s2',
    group: 'securite',
    text: {
      fr: {
        kicker: 'Sécurité 2',
        title: 'Qui, dans mon équipe, peut voir et faire quoi ?',
        lead: 'Six rôles du directeur au chauffeur : le menu qui suit le rôle, le lien direct qui reste fermé, la facture que le commercial émet mais dont seul le comptable enregistre l’encaissement, et aucun mot de passe partagé.',
        aria: 'Sécurité 2 — les rôles et les droits',
        gains: [
          'Le menu suit le rôle et les modules activés',
          'Émettre et encaisser, préparer et valider : des droits distincts',
          'Chacun choisit son propre mot de passe',
        ],
      },
      en: {
        kicker: 'Security 2',
        title: 'Who on my team can see and do what?',
        lead: 'Six roles from director to driver: the menu that follows the role, the direct link that stays closed, the invoice sales can issue but only the accountant can record a payment on, and no shared passwords.',
        aria: 'Security 2 — roles and permissions',
        gains: [
          'The menu follows the role and the active modules',
          'Issue and collect, prepare and approve: separate rights',
          'Everyone sets their own password',
        ],
      },
      es: {
        kicker: 'Seguridad 2',
        title: '¿Quién de mi equipo puede ver y hacer qué?',
        lead: 'Seis roles del director al conductor: el menú que sigue al rol, el enlace directo que sigue cerrado, la factura que el comercial emite pero cuyo cobro solo registra el contable, y nadie que comparta contraseñas.',
        aria: 'Seguridad 2: roles y permisos',
        gains: [
          'El menú sigue el rol y los módulos activados',
          'Emitir y cobrar, preparar y validar: permisos distintos',
          'Cada uno define su propia contraseña',
        ],
      },
      ru: {
        kicker: 'Безопасность 2',
        title: 'Кто в моей команде что видит и что может делать?',
        lead: 'Шесть ролей от директора до водителя: меню по роли, прямая ссылка, которая не открывается, фактура, которую выставляет менеджер по продажам, а оплату проводит только бухгалтер, и никаких общих паролей.',
        aria: 'Безопасность 2 — роли и права',
        gains: [
          'Меню собирается из роли и подключённых модулей',
          'Выставить и оплатить, подготовить и утвердить — разные права',
          'Пароль каждый задаёт сам',
        ],
      },
    },
  },
  {
    episode: '35-s3',
    group: 'securite',
    text: {
      fr: {
        kicker: 'Sécurité 3',
        title: 'Peut-on modifier un document ou un chiffre après coup ?',
        lead: 'Le bon de commande, la facture et l’avoir qui gardent leur propre copie, les journaux de l’argent qui ne font que s’allonger, des numéros de facture sans trou et un motif pour toute annulation.',
        aria: 'Sécurité 3 — l’inaltérabilité',
        gains: [
          'Les documents émis ne changent pas après coup.',
          'L’argent se corrige par une nouvelle ligne, pas à la gomme.',
          'Factures numérotées sans trous, annulations motivées.',
        ],
      },
      en: {
        kicker: 'Security 3',
        title: 'Can a document or a figure be changed after the fact?',
        lead: 'The order form, invoice and credit note that keep their own copy, money logs that only grow, gap-free invoice numbers and a reason for every cancellation.',
        aria: 'Security 3 — immutability',
        gains: [
          'Issued documents never change after the fact.',
          'Money is corrected with a new line, never an eraser.',
          'Gap-free invoice numbers, cancellations with a reason.',
        ],
      },
      es: {
        kicker: 'Seguridad 3',
        title: '¿Se puede cambiar un documento o una cifra a posteriori?',
        lead: 'La orden de pedido, la factura y el abono que guardan su propia copia, los registros de dinero que solo crecen, números de factura sin huecos y un motivo para cada anulación.',
        aria: 'Seguridad 3: inalterabilidad',
        gains: [
          'Los documentos emitidos no cambian a posteriori.',
          'El dinero se corrige con una línea nueva, no con la goma.',
          'Facturas numeradas sin huecos, anulaciones con motivo.',
        ],
      },
      ru: {
        kicker: 'Безопасность 3',
        title: 'Можно ли задним числом изменить документ или цифру?',
        lead: 'Бон заказа, фактура и авуар с собственной копией, журналы денег, которые только растут, номера фактур без пропусков и причина для каждой отмены.',
        aria: 'Безопасность 3 — неизменяемость',
        gains: [
          'Выпущенные документы не меняются задним числом.',
          'Деньги исправляются новой строкой, а не ластиком.',
          'Номера фактур — без пропусков, отмены — с причиной.',
        ],
      },
    },
  },
  {
    episode: '36-s4',
    group: 'securite',
    text: {
      fr: {
        kicker: 'Sécurité 4',
        title: 'Que voit le chauffeur, et que ne voit-il jamais ?',
        lead: 'L’application du chauffeur comme entrée séparée, sans prix ni portail du bureau, le code de connexion à usage unique, la position jamais demandée et les téléphones, e-mails et cartes carburant masqués.',
        aria: 'Sécurité 4 — le chauffeur et la confidentialité',
        gains: [
          'Le chauffeur voit ses missions et son argent — sans prix ni accès au portail.',
          'Code de connexion : une fois, 24 heures, cinq essais, seule l’empreinte en base.',
          'Téléphones et e-mails masqués dans les journaux et rapports d’erreurs, carte réduite à un masque.',
        ],
      },
      en: {
        kicker: 'Security 4',
        title: 'What does the driver see, and what never reaches him?',
        lead: 'The driver app as a separate entrance with no prices and no office portal, the one-time login code, location never requested, phone numbers and e-mails hidden in logs, and only a mask of the fuel card number.',
        aria: 'Security 4 — the driver and privacy',
        gains: [
          'The driver sees his missions and his money — no prices, no portal access.',
          'Login code: once, 24 hours, five attempts, only a fingerprint stored.',
          'Phones and e-mails hidden in logs and error reports, fuel card kept as a mask.',
        ],
      },
      es: {
        kicker: 'Seguridad 4',
        title: '¿Qué ve el conductor y qué no ve nunca?',
        lead: 'La aplicación del conductor como entrada separada, sin precios ni portal de oficina, el código de acceso de un solo uso, la ubicación que nunca se pide, teléfonos y correos ocultos en los registros y solo una máscara del número de la tarjeta de combustible.',
        aria: 'Seguridad 4: el conductor y la privacidad',
        gains: [
          'El conductor ve sus misiones y su dinero, sin precios ni acceso al portal.',
          'Código de acceso: una vez, 24 horas, cinco intentos, solo la huella en la base.',
          'Teléfonos y correos ocultos en registros e informes de errores, la tarjeta solo como máscara.',
        ],
      },
      ru: {
        kicker: 'Безопасность 4',
        title: 'Что видит водитель, а чего не увидит никогда?',
        lead: 'Приложение водителя как отдельный вход — без цен и без офисного портала, одноразовый код входа, геолокация, которую не запрашивают, и скрытые телефоны, почта и топливные карты.',
        aria: 'Безопасность 4 — водитель и приватность',
        gains: [
          'Водитель видит свои рейсы и свои деньги — без цен и без доступа к порталу.',
          'Код входа: один раз, 24 часа, пять попыток, в базе — только отпечаток.',
          'Телефоны и почта скрыты в журналах и отчётах об ошибках, карта — только маской.',
        ],
      },
    },
  },
  {
    episode: '37-s5',
    group: 'securite',
    text: {
      fr: {
        kicker: 'Sécurité 5',
        title: 'Qui décide quand l’argent, les documents et les e-mails sortent ?',
        lead: 'Aucun paiement envoyé ni accès à votre banque, un fichier que vous chargez vous-même, un stockage fermé sans lien public, des PDF assemblés dans le produit et un e-mail désactivé tant que vous ne l’activez pas.',
        aria: 'Sécurité 5 — l’argent, les documents et les e-mails',
        gains: [
          'Le produit ne paie pas et n’entre pas dans votre banque : vous chargez le fichier, le relevé reconnaît le paiement.',
          'Documents en stockage fermé, PDF assemblés dans le produit.',
          'Les e-mails en votre nom ne partent que si vous avez coché la case.',
        ],
      },
      en: {
        kicker: 'Security 5',
        title: 'Who decides when money, documents and emails leave the system?',
        lead: 'No payment sent and no access to your bank, a file you upload yourself, closed storage with no public links, PDFs assembled in the product, and an email that stays off until you switch it on.',
        aria: 'Security 5 — money, documents and emails',
        gains: [
          'The product doesn’t pay or log into your bank: you upload the file, the statement recognises the payment.',
          'Documents in closed storage, PDFs assembled inside the product.',
          'Emails in your name go out only once you tick the box.',
        ],
      },
      es: {
        kicker: 'Seguridad 5',
        title: '¿Quién decide cuándo salen el dinero, los documentos y los correos?',
        lead: 'Ningún pago enviado ni acceso a su banco, un fichero que sube usted mismo, almacenamiento cerrado sin enlaces públicos, PDF generados en el producto y un correo desactivado hasta que usted lo active.',
        aria: 'Seguridad 5: dinero, documentos y correos',
        gains: [
          'El producto no paga ni entra en su banco: usted sube el fichero y el extracto reconoce el pago.',
          'Documentos en almacenamiento cerrado, PDF generados dentro del producto.',
          'Los correos en su nombre solo salen si usted marca la casilla.',
        ],
      },
      ru: {
        kicker: 'Безопасность 5',
        title: 'Кто решает, когда наружу уходят деньги, документы и письма?',
        lead: 'Ни одного отправленного платежа и никакого доступа к вашему банку, файл, который загружаете вы, закрытое хранилище без публичных ссылок, PDF внутри продукта и письмо, выключенное, пока вы сами его не включите.',
        aria: 'Безопасность 5 — деньги, документы и письма',
        gains: [
          'Продукт не платит и не входит в ваш банк: файл загружаете вы, оплату признаёт выписка.',
          'Документы — в закрытом хранилище, PDF собираются внутри продукта.',
          'Письма от вашего имени уходят, только когда вы сами поставили галочку.',
        ],
      },
    },
  },
  {
    episode: '38-s6',
    group: 'securite',
    text: {
      fr: {
        kicker: 'Sécurité 6',
        title: 'Que se passe-t-il si la liaison avec TinyCIO ou le réseau tombe ?',
        lead: 'Un portail qui continue sans TinyCIO, les événements en file d’attente, la dépense du ferry envoyée à terre, une seule ligne malgré une réponse perdue et un relevé rechargé sans doublons.',
        aria: 'Sécurité 6 — la résilience',
        gains: [
          'Les données de votre entreprise sont séparées de toutes les autres et restent les vôtres.',
          'Rien n’est corrigé en silence : chaque modification a un auteur.',
          'Ni argent, ni documents, ni e-mails — sans une action de votre part.',
        ],
      },
      en: {
        kicker: 'Security 6',
        title: 'What happens when the link to TinyCIO or the network goes down?',
        lead: 'A portal that keeps running without TinyCIO, queued events, a ferry expense sent once ashore, a single record despite a lost reply, and a statement reloaded without duplicates.',
        aria: 'Security 6 — resilience',
        gains: [
          'Your company’s data is kept apart from everyone else’s and stays yours.',
          'Nothing is corrected silently: every change has an author.',
          'No money, no documents, no emails go out without your action.',
        ],
      },
      es: {
        kicker: 'Seguridad 6',
        title: '¿Qué pasa si se corta la conexión con TinyCIO o la red?',
        lead: 'Un portal que sigue sin TinyCIO, eventos en cola, el gasto del ferry enviado al llegar a tierra, un solo registro pese a una respuesta perdida y un extracto recargado sin duplicados.',
        aria: 'Seguridad 6: resiliencia',
        gains: [
          'Los datos de su empresa están separados de todos los demás y siguen siendo suyos.',
          'Nada se corrige en silencio: cada cambio tiene autor.',
          'Ni dinero, ni documentos, ni correos, sin una acción suya.',
        ],
      },
      ru: {
        kicker: 'Безопасность 6',
        title: 'Что будет, если пропадёт связь с TinyCIO или сеть?',
        lead: 'Портал, который работает без TinyCIO, события в очереди, расход с парома, ушедший на берегу, одна запись при потерянном ответе и повторная выписка без дублей.',
        aria: 'Безопасность 6 — устойчивость',
        gains: [
          'Данные вашей компании отделены от всех остальных и остаются вашими.',
          'Ничего не исправляется молча: у каждого изменения есть автор.',
          'Ни денег, ни документов, ни писем — без вашего действия.',
        ],
      },
    },
  },
  {
    episode: '39-e33',
    group: 'demarrage',
    text: {
      fr: {
        kicker: 'Épisode 33',
        title: 'Faut-il changer de comptable pour utiliser maTransports ?',
        lead: 'Les rapports en Excel, les factures et bons de commande en PDF, les paiements en fichier pour votre banque en ligne, le relevé rapproché et les limites : pas de grand livre, pas de connexion bancaire directe.',
        aria: 'Épisode 33 — la comptabilité et la banque',
        gains: [
          'Pas besoin de changer de comptable.',
          'Rapports, documents et paiements en fichiers prêts.',
          'Des frontières honnêtes : nous ne vendons pas ce que vous avez déjà.',
        ],
      },
      en: {
        kicker: 'Episode 33',
        title: 'Do I have to change accountants to use maTransports?',
        lead: 'Reports in Excel, invoices and purchase orders as PDF, payments as a file for your online banking, the statement reconciled, and the limits: no general ledger, no direct bank connection.',
        aria: 'Episode 33 — accounting and the bank',
        gains: [
          'No need to change accountants.',
          'Reports, documents and payments as ready-made files.',
          'Honest boundaries: we don’t sell what you already have.',
        ],
      },
      es: {
        kicker: 'Episodio 33',
        title: '¿Hay que cambiar de contable para usar maTransports?',
        lead: 'Los informes en Excel, las facturas y órdenes de compra en PDF, los pagos en un fichero para su banca electrónica, el extracto conciliado y los límites: sin libro mayor ni conexión bancaria directa.',
        aria: 'Episodio 33: contabilidad y banco',
        gains: [
          'No hace falta cambiar de contable.',
          'Informes, documentos y pagos en ficheros listos.',
          'Límites honestos: no vendemos lo que usted ya tiene.',
        ],
      },
      ru: {
        kicker: 'Эпизод 33',
        title: 'Нужно ли менять бухгалтера, чтобы работать в maTransports?',
        lead: 'Отчёты в Excel, фактуры и заказы в PDF, платежи файлом для клиент-банка, сверка выписки и границы: ни главной книги, ни прямого подключения к банку.',
        aria: 'Эпизод 33 — бухгалтерия и банк',
        gains: [
          'Бухгалтера менять не нужно.',
          'Отчёты, документы и платежи — готовыми файлами.',
          'Честные границы: мы не продаём то, что у вас уже есть.',
        ],
      },
    },
  },
  {
    episode: '40-e34',
    group: 'demarrage',
    text: {
      fr: {
        kicker: 'Épisode 34',
        title: 'Combien coûte maTransports, et comment se calcule le prix ?',
        lead: 'Un prix en trois parties — le poste de travail, le module payant et le camion actif — avec le socle de base, l’essai de quatorze jours, un exemple chiffré et le démarrage accompagné.',
        aria: 'Épisode 34 — le prix',
        gains: [
          'Vous ne payez que ce que vous utilisez.',
          'Chaque module disponible : 14 jours gratuits, les données restent.',
          'Un prix transparent, qui se calcule sur un coin de table.',
        ],
      },
      en: {
        kicker: 'Episode 34',
        title: 'How much does maTransports cost, and how is the price worked out?',
        lead: 'A price in three parts — the workstation, the paid module and the active truck — with the base set, the fourteen-day trial, a worked example and the guided launch.',
        aria: 'Episode 34 — the price',
        gains: [
          'You pay only for what you use.',
          'Any available module: 14 days free, your data stays.',
          'A transparent price you can work out on a napkin.',
        ],
      },
      es: {
        kicker: 'Episodio 34',
        title: '¿Cuánto cuesta maTransports y cómo se calcula el precio?',
        lead: 'Un precio en tres partes —el puesto de trabajo, el módulo de pago y el camión activo—, con el paquete básico, la prueba de catorce días, un ejemplo con cifras y el arranque acompañado.',
        aria: 'Episodio 34: el precio',
        gains: [
          'Paga solo por lo que utiliza.',
          'Cada módulo disponible: 14 días gratis, los datos se quedan.',
          'Un precio transparente que se calcula en una servilleta.',
        ],
      },
      ru: {
        kicker: 'Эпизод 34',
        title: 'Сколько стоит maTransports и как считается цена?',
        lead: 'Цена из трёх частей — рабочее место, платный модуль и активная машина — плюс базовый набор, четырнадцать дней пробного периода, пример с цифрами и запуск с сопровождением.',
        aria: 'Эпизод 34 — цена',
        gains: [
          'Платите только за то, чем пользуетесь.',
          'Любой доступный модуль — 14 дней бесплатно, данные остаются.',
          'Прозрачная цена, которую можно посчитать на салфетке.',
        ],
      },
    },
  },
  {
    episode: '41-e35',
    group: 'demarrage',
    text: {
      fr: {
        kicker: 'Épisode 35',
        title: 'Qu’est-ce qui ne fonctionne pas encore dans maTransports ?',
        lead: 'Ce qui est encore en développement, dit franchement : carte et géolocalisation, messagerie avec le chauffeur, paie et remboursements, heures de conduite, réception des demandes et CMR électronique.',
        aria: 'Épisode 35 — ce qui est en développement',
      },
      en: {
        kicker: 'Episode 35',
        title: 'What doesn’t work yet in maTransports?',
        lead: 'What is still in development, said plainly: map and geotracking, chat with the driver, payroll and reimbursements, driving hours, request intake and electronic CMR.',
        aria: 'Episode 35 — what is in development',
      },
      es: {
        kicker: 'Episodio 35',
        title: '¿Qué todavía no funciona en maTransports?',
        lead: 'Lo que todavía está en desarrollo, dicho con claridad: mapa y geolocalización, chat con el conductor, nóminas y reembolsos, horas de conducción, recepción de solicitudes y CMR electrónico.',
        aria: 'Episodio 35: lo que está en desarrollo',
      },
      ru: {
        kicker: 'Эпизод 35',
        title: 'Что в maTransports пока не работает?',
        lead: 'То, что ещё в разработке, сказано прямо: карта и геотрекинг, чат с водителем, зарплата и возмещения, часы вождения, приём заявок и электронный CMR.',
        aria: 'Эпизод 35 — что в разработке',
      },
    },
  },
  {
    episode: '42-e36',
    group: 'demarrage',
    text: {
      fr: {
        kicker: 'Épisode 36',
        title: 'Comment charger ma flotte et mon historique d’un seul coup ?',
        lead: 'Sept étapes d’inscription, puis l’import d’un fichier Excel ou CSV : colonnes reconnues, aperçu ligne par ligne avant tout enregistrement, missions passées clôturées et ce que le fichier n’apporte pas.',
        aria: 'Épisode 36 — importer votre parc',
        gains: [
          'Un aperçu avant écriture — rien sans votre clic.',
          'Flotte, chauffeurs et missions passées depuis votre fichier.',
          'L\'import d\'un nouveau parc, à tout moment.',
        ],
      },
      en: {
        kicker: 'Episode 36',
        title: 'How do I bring in my fleet and history in one go?',
        lead: 'Seven sign-up steps, then importing an Excel or CSV file: recognised columns, a line-by-line preview before anything is saved, past missions closed, and what the file does not bring.',
        aria: 'Episode 36 — importing your fleet',
        gains: [
          'A preview before anything is written — nothing without your click.',
          'Fleet, drivers and past missions from your file.',
          'Import a new fleet at any time.',
        ],
      },
      es: {
        kicker: 'Episodio 36',
        title: '¿Cómo cargo mi flota y mi historial de una sola vez?',
        lead: 'Siete pasos de registro y luego la importación de un archivo Excel o CSV: columnas reconocidas, vista previa fila por fila antes de guardar, misiones pasadas cerradas y lo que el archivo no trae.',
        aria: 'Episodio 36: importar su flota',
        gains: [
          'Vista previa antes de escribir: nada sin su clic.',
          'Flota, conductores y misiones pasadas desde su archivo.',
          'Importar una flota nueva en cualquier momento.',
        ],
      },
      ru: {
        kicker: 'Эпизод 36',
        title: 'Как загрузить парк и историю рейсов одним файлом?',
        lead: 'Семь шагов регистрации и импорт файла Excel или CSV: распознанные колонки, построчный предпросмотр до записи, закрытые прошлые рейсы и то, чего файл не принесёт.',
        aria: 'Эпизод 36 — импорт вашего парка',
        gains: [
          'Предпросмотр до записи — ничего без вашего клика.',
          'Парк, водители и прошлые рейсы — из вашего файла.',
          'Импорт нового парка — в любой момент.',
        ],
      },
    },
  },
];

/** Les épisodes de la vidéothèque, dans l'ordre de la série. */
export const LIBRARY_EPISODES: readonly string[] = LIBRARY.map((e) => e.episode);

export function libraryGroup(episode: string): VideoGroupId | undefined {
  return LIBRARY.find((e) => e.episode === episode)?.group;
}

export function episodeText(episode: string, locale: string): EpisodeText | undefined {
  return LIBRARY.find((e) => e.episode === episode)?.text[locale];
}

/** La voix de l'épisode, paragraphe par paragraphe, sans repères de synchronisation. */
export function episodeTranscript(episode: string, locale: string): readonly string[] | undefined {
  return (transcripts as Record<string, Record<string, string[]>>)[episode]?.[locale];
}

// ── Chrome de la vidéothèque ─────────────────────────────────────────────────
// Ici et non dans les messages: même raison que TRAILER dans videos.ts.

export interface LibraryLabels {
  /** Menu du haut, fil de retour. */
  nav: string;
  kicker: string;
  title: string;
  lead: string;
  /** Bouton du premier écran de l'accueil; `{min}` = durée de la bande-annonce arrondie. */
  heroCta: (min: number) => string;
  /** Lien de la section bande-annonce vers la vidéothèque. */
  allVideos: string;
  gains: string;
  transcript: string;
  /** Nom de la langue de la piste de sous-titres, dans cette langue. */
  captions: string;
  intro: { label: string; hint: string };
  /** Fil d'Ariane: premier maillon. */
  home: string;
  prev: string;
  next: string;
  /** Lien sous la vidéo du haut d'une page «fonctions». */
  episodePage: string;
}

const LABELS: Record<string, LibraryLabels> = {
  fr: {
    nav: 'Vidéos',
    kicker: 'Vidéos',
    title: 'Le produit en vidéo, un sujet à la fois',
    lead: 'Une à deux minutes par épisode, avec la voix et les titres dans votre langue.',
    heroCta: (m) => `Voir la vidéo · ${m} min`,
    allVideos: 'Toutes les vidéos',
    gains: 'Ce que vous y gagnez',
    transcript: 'Transcription',
    captions: 'Français',
    intro: { label: 'Découverte', hint: 'Ce qu’est le produit et comment il est fait — à regarder en premier.' },
    home: 'Accueil',
    prev: 'Épisode précédent',
    next: 'Épisode suivant',
    episodePage: 'Page de l’épisode',
  },
  en: {
    nav: 'Videos',
    kicker: 'Videos',
    title: 'The product on video, one topic at a time',
    lead: 'One to two minutes per episode, with the voice and the titles in your language.',
    heroCta: (m) => `Watch the video · ${m} min`,
    allVideos: 'All videos',
    gains: 'What you get',
    transcript: 'Transcript',
    captions: 'English',
    intro: { label: 'First look', hint: 'What the product is and how it is built — watch these first.' },
    home: 'Home',
    prev: 'Previous episode',
    next: 'Next episode',
    episodePage: 'Episode page',
  },
  es: {
    nav: 'Vídeos',
    kicker: 'Vídeos',
    title: 'El producto en vídeo, un tema cada vez',
    lead: 'De uno a dos minutos por episodio, con la voz y los títulos en su idioma.',
    heroCta: (m) => `Ver el vídeo · ${m} min`,
    allVideos: 'Todos los vídeos',
    gains: 'Lo que usted gana',
    transcript: 'Transcripción',
    captions: 'Español',
    intro: { label: 'Primer contacto', hint: 'Qué es el producto y cómo está hecho: para ver primero.' },
    home: 'Inicio',
    prev: 'Episodio anterior',
    next: 'Episodio siguiente',
    episodePage: 'Página del episodio',
  },
  ru: {
    nav: 'Видео',
    kicker: 'Видео',
    title: 'Продукт на видео, тема за темой',
    lead: 'Одна-две минуты на эпизод, голос и титры — на вашем языке.',
    heroCta: (m) => `Смотреть видео · ${m} мин`,
    allVideos: 'Все видео',
    gains: 'Что вы получаете',
    transcript: 'Расшифровка',
    captions: 'Русский',
    intro: { label: 'Знакомство', hint: 'Что это за продукт и как он устроен — с этого стоит начать.' },
    home: 'Главная',
    prev: 'Предыдущий эпизод',
    next: 'Следующий эпизод',
    episodePage: 'Страница эпизода',
  },
};

/** `undefined` hors des langues de la série (l'arabe): pas de lien, pas de page. */
export function libraryLabels(locale: string): LibraryLabels | undefined {
  return VIDEO_LOCALES.includes(locale) ? LABELS[locale] : undefined;
}

/** Ancre de la vidéothèque — les groupes portent `videos-<id>` (FeatureExplorer). */
export const LIBRARY_ANCHOR = 'videos';

export function episodeHref(episode: string, locale: string): string {
  return `/${locale}/videos/${episodeSlug(episode)}`;
}

/** Lien «Vidéos» du menu: absent en arabe et tant que rien n'est publié. */
export function videoNav(locale: string): { href: string; label: string } | undefined {
  const l = libraryLabels(locale);
  if (!l || videoEpisodes().length === 0) return undefined;
  return { href: `/${locale}/videos`, label: l.nav };
}

/** «Découverte» en tête, puis les catégories des pages «fonctions», dans leur ordre. */
const GROUP_ORDER: readonly VideoGroupId[] = ['intro', ...FEATURE_CATEGORIES];

/**
 * Les épisodes publiés ET décrits dans cette langue, groupés pour
 * FeatureExplorer. Un groupe vide ne paraît pas (même règle que featureNav).
 */
export function libraryGroups(locale: string, host?: string): ExplorerGroup[] {
  const l = libraryLabels(locale);
  if (!l) return [];
  return GROUP_ORDER.map((id) => {
    const header = id === 'intro' ? { id, ...l.intro } : featureCategoryHeader(id, locale);
    const items = LIBRARY.filter((e) => e.group === id).flatMap((e) => {
      const video = landingVideo(e.episode, locale, host);
      const t = e.text[locale];
      if (!video || !t) return [];
      return [
        {
          href: episodeHref(e.episode, locale),
          slug: episodeSlug(e.episode),
          label: t.kicker,
          title: t.title,
          lead: t.lead,
          poster: video.poster,
          duration: formatDuration(video.duration),
        },
      ];
    });
    return { ...header, items };
  }).filter((g) => g.items.length > 0);
}

/** Le bouton «Essayer 14 jours» de la page d'épisode — le même que celui des pages «fonctions». */
export function trialCta(locale: string): string {
  return featureLabels(locale).cta;
}

// ── «Vidéos sur ce sujet» des pages «fonctions» ──────────────────────────────

/**
 * Épisodes qui montrent L'ÉCRAN que vend la page, en tête du bloc; le reste de
 * la catégorie suit dans l'ordre de la série. Une page absente d'ici prend sa
 * catégorie telle quelle.
 */
export const PAGE_EPISODES: Record<string, readonly string[]> = {
  exploitation: ['04-e04', '05-e05', '06-e06', '07-e07'],
  conteneurs: ['11-e11'],
  'documents-de-transport': ['16-e16', '15-e15', '14-e14'],
  carburant: ['19-e19'],
  entretien: ['20-e20', '21-e21'],
  facturation: ['23-e23'],
  tresorerie: ['28-e28', '29-e29', '27-e27', '26-e26'],
  'caisse-chauffeurs': ['24-e24'],
  marges: ['30-e30'],
};

/** Au-delà, le bloc renvoie au groupe de la vidéothèque. */
const RELATED_MAX = 6;

const RELATED_LABELS: Record<string, { title: string; all: string }> = {
  fr: { title: 'Vidéos sur ce sujet', all: 'Toutes les vidéos de la catégorie' },
  en: { title: 'Videos on this topic', all: 'All videos in this category' },
  es: { title: 'Vídeos sobre este tema', all: 'Todos los vídeos de la categoría' },
  ru: { title: 'Видео по теме', all: 'Все видео этой категории' },
};

export interface RelatedVideos {
  title: string;
  all: string;
  /** Le groupe de la vidéothèque (`/fr/videos#videos-finance`). */
  allHref: string;
  items: ExplorerItem[];
}

/**
 * Le bloc d'une page «fonctions»: les épisodes publiés de sa catégorie, ceux
 * de son écran d'abord. Affiche LOCALE (`public/videos/`), pas Bunny: la page
 * est figée au build (`force-static`) et ne connaît pas le domaine du visiteur.
 * `undefined` en arabe et tant que la catégorie n'a aucun épisode publié.
 */
/** Épisodes publiés de la catégorie d'une page «fonctions», ceux de son écran d'abord. */
function pageEpisodes(slug: string, locale: string): string[] {
  const category = FEATURE_CATEGORY[slug];
  if (!category || !libraryLabels(locale)) return [];
  const first = PAGE_EPISODES[slug] ?? [];
  const inCategory = LIBRARY.filter((e) => e.group === category).map((e) => e.episode);
  // Un épisode «de l'écran» hors de la catégorie de la page est refusé par le test.
  return [...first, ...inCategory.filter((ep) => !first.includes(ep))].filter(
    (ep) => landingVideo(ep, locale) && episodeText(ep, locale),
  );
}

export interface HeroVideo {
  episode: string;
  href: string;
  text: EpisodeText;
  /** Affiche LOCALE: la page est figée au build (voir relatedVideos). */
  video: LandingVideo;
  captions: string;
}

/**
 * La vidéo du haut d'une page «fonctions»: le premier épisode de son écran
 * (PAGE_EPISODES), sinon le premier de sa catégorie. Le visiteur n'a pas à
 * descendre jusqu'au bloc du bas pour voir le produit en mouvement.
 */
export function heroVideo(slug: string, locale: string): HeroVideo | undefined {
  const ep = pageEpisodes(slug, locale)[0];
  if (!ep) return undefined;
  const video = landingVideo(ep, locale)!;
  const files = videoFiles(ep, locale)!;
  return {
    episode: ep,
    href: `${episodeHref(ep, locale)}?from=${slug}`,
    text: episodeText(ep, locale)!,
    video: { ...video, poster: files.image },
    captions: files.captions,
  };
}

/**
 * Le bloc «Vidéos sur ce sujet» d'une page «fonctions»: les épisodes publiés de
 * sa catégorie, ceux de son écran d'abord, SANS celui du haut de page (il est
 * déjà dans le Hero). Affiche LOCALE (`public/videos/`), pas Bunny: la page est
 * figée au build (`force-static`) et ne connaît pas le domaine du visiteur.
 * Les liens portent `?from=<page>`: le fil d'Ariane de l'épisode ramène ici.
 * `undefined` en arabe et quand il ne reste rien à montrer.
 */
export function relatedVideos(slug: string, locale: string): RelatedVideos | undefined {
  const l = RELATED_LABELS[locale];
  const category = FEATURE_CATEGORY[slug];
  if (!l || !category) return undefined;
  const items = pageEpisodes(slug, locale)
    .slice(1)
    .map((ep) => {
      const video = landingVideo(ep, locale)!;
      const t = episodeText(ep, locale)!;
      return {
        href: `${episodeHref(ep, locale)}?from=${slug}`,
        slug: episodeSlug(ep),
        label: t.kicker,
        title: t.title,
        poster: videoFiles(ep, locale)!.image,
        duration: formatDuration(video.duration),
      };
    });
  if (items.length === 0) return undefined;
  return { ...l, allHref: `/${locale}/videos#${LIBRARY_ANCHOR}-${category}`, items: items.slice(0, RELATED_MAX) };
}

// ── Navigation d'une page d'épisode ──────────────────────────────────────────

/** «Épisode 27 — la banque» → «la banque»: le libellé court de l'index latéral. */
export function episodeShort(t: EpisodeText): string {
  const m = /\s[—:]\s(.+)$/.exec(t.aria) ?? /:\s(.+)$/.exec(t.aria);
  return m ? m[1] : t.title;
}

/** Les épisodes visibles dans cette langue, dans l'ordre de la série. */
function visibleEpisodes(locale: string): string[] {
  return LIBRARY.filter((e) => landingVideo(e.episode, locale) && e.text[locale]).map((e) => e.episode);
}

/** Précédent et suivant dans l'ordre de la série (pas de la catégorie). */
export function adjacentEpisodes(episode: string, locale: string): { prev?: string; next?: string } {
  const list = visibleEpisodes(locale);
  const i = list.indexOf(episode);
  if (i < 0) return {};
  return { prev: list[i - 1], next: list[i + 1] };
}

export interface IndexGroup {
  id: VideoGroupId;
  label: string;
  items: { episode: string; href: string; kicker: string; short: string }[];
}

/** L'index latéral de la page d'épisode: les groupes de la vidéothèque, en court. */
export function libraryIndex(locale: string): IndexGroup[] {
  const l = libraryLabels(locale);
  if (!l) return [];
  const visible = visibleEpisodes(locale);
  return GROUP_ORDER.map((id) => ({
    id,
    label: id === 'intro' ? l.intro.label : featureCategoryHeader(id, locale).label,
    items: LIBRARY.filter((e) => e.group === id && visible.includes(e.episode)).map((e) => ({
      episode: e.episode,
      href: episodeHref(e.episode, locale),
      kicker: e.text[locale].kicker,
      short: episodeShort(e.text[locale]),
    })),
  })).filter((g) => g.items.length > 0);
}

/** Libellé court d'une page «fonctions» pour le fil d'Ariane (`?from=`). */
export function fromPage(slug: string | undefined, locale: string): { href: string; label: string } | undefined {
  if (!slug || !FEATURE_CATEGORY[slug]) return undefined;
  const item = featureNav(locale)?.items.find((i) => i.href === `/${locale}/${slug}`);
  return item ? { href: item.href, label: item.label } : undefined;
}
