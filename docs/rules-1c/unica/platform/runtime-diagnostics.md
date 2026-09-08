# Runtime Diagnostics

Use this reference when a platform failure must be explained from runtime
evidence, not from a final exception message alone.

## Evidence Model

- Start with the timeline: startup, first request/job, first error, retries,
  rollback, and cleanup.
- Preserve identifiers: timestamp with timezone, infobase, user, session,
  connection, process id, transaction id, background job id, HTTP path, and
  correlation id.
- Separate evidence sources: journal registration, technological log, launch
  output, client/server process state, web-client URL, temporary files, and
  DBMS trace.
- Prefer the first causative event over later consequences such as repeated
  retries, transaction rollback, or generic session termination.
- Structured logging is evidence only when fields can be correlated: event name,
  timestamp, metadata object, reference, correlation id, tenant/external id,
  retry count, and sanitized error detail.

## Analysis Rules

- If a failure appears during startup, confirm platform version, client mode,
  infobase type, cluster or standalone mode, ports, credentials, and source-set
  path before proposing a code fix.
- If a failure appears under HTTP or web-client load, connect the request path
  to handler metadata and module code before interpreting the log message.
- If a failure appears in a background job, record the job name, schedule,
  parameters, user context, retry count, and lock state.
- If DBMS evidence exists, keep query text, lock/deadlock participants, wait
  event, table/index names, and transaction boundaries together.
- If the evidence fragment has no first error, state the missing evidence and
  request the preceding interval instead of guessing.

## Output Pattern

1. Timeline with only key events.
2. Root-cause hypothesis tied to concrete evidence.
3. Affected metadata/module paths.
4. Verification step that can prove or disprove the hypothesis.
5. Missing evidence or Unica MCP contract gap, if public MCP `unica` cannot
   retrieve the required artifact.
