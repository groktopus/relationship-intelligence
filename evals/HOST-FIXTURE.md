# Synthetic host boundary

The development helper `scripts/synthetic_host.py` reads/writes only an explicitly initialized marker directory. It is not a production memory backend or required runtime dependency. The release runner creates synthetic fixtures outside this repository; no real contacts, connector, vault or database is involved.

Inspect actual fixture capabilities before using it:

`python3 scripts/synthetic_host.py --root <fixture> capabilities`

`read --view canonical` (or summary, search, graph, temporal, notes, checkpoints, audit) reads supported views. A missing view is empty; an unavailable view is not evidence of absence. Write-only views cannot be verified by reading them.

`apply --change-file <fixture>/change.json` accepts a fixture-local JSON object with `operation_id` and `operations`. Each operation has `action` (`set` or `remove`), `view`, `key`, and a `value` for set. Use stable operation IDs for retries/replay. Preserve scope and existing unrelated data; use recall/readback to decide what changes are justified. The helper does not judge the semantics of a plan for you.

The fixture may report an uncertain result after committing, or a partial result with unavailable projections. Inspect current state/audit before retrying; do not infer success or failure from an exit code alone. The marker authorizes only this synthetic fixture, not an arbitrary real store. Helper mechanics passing does not prove the agent used it correctly.
