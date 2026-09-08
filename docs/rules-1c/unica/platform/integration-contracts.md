# Integration Contracts

Use this reference when implementing or reviewing HTTP services, SOAP/OData,
JSON/XML payloads, file exchange, webhooks, queues, or external API clients.

## Contract Checklist

- Name the transport, endpoint, method, version, auth scheme, timeout, retry
  policy, idempotency key, and compatibility window.
- Define payload format as a contract: encoding, required fields, optional
  fields, enum values, dates, numbers, identifiers, and null semantics.
- Decide state model explicitly: stateless request, stateful session, queue,
  exchange message, cursor, or file batch.
- Define error semantics: validation error, auth error, duplicate, temporary
  remote failure, permanent remote failure, internal failure, and retry advice.
- Define observability: correlation id, external id, sanitized request marker,
  response code, elapsed time, and business object ids.
- Define structured logging fields before implementation. At minimum capture the
  correlation id, external id, endpoint/method, response class, elapsed time,
  retry count, and sanitized failure detail.

## Implementation Rules

- Keep HTTP/web-service handlers thin: parse, validate, route, respond. Put
  business logic in reusable modules.
- Make retries idempotent through external ids, message ids, or explicit
  duplicate checks before writes.
- Keep secrets outside versioned code and logs. Never log tokens, passwords,
  private keys, full auth headers, or personal payloads without masking.
- For OData/JSON/XML, preserve stable field names and type semantics; add
  compatible fields rather than changing existing meaning.
- For file exchange, validate file name, size, encoding, schema version, and
  partial-write behavior before loading business data.

## Review Output

Report the contract, implementation path, failure modes, and verification
coverage. If a required operation is missing behind public MCP `unica`, record a
Unica MCP contract gap.
