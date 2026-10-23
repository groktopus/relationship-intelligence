# Contributing

Discuss substantial new methods or behavior changes in an issue before expanding the skill. Keep improvements focused on the evolving person model and asynchronous PREPARE/DIGEST cycle.

## Change process

1. Explain the concrete problem, intended behavior and evidence that would distinguish an improvement.
2. Keep SKILL.md concise. Put substantive methods in selectively routed references and preserve working relative links.
3. For research claims, cite primary sources where available. Record access depth, study design/population, results, alternatives, conflicting/null findings and transfer limits. Distinguish practitioner doctrine from empirical validation and proposed integration.
4. Use synthetic fixtures and examples. Do not commit real transcripts, relationship profiles, contact records, credentials, source manuscripts or local recovery files. Inspect staged content and history; .gitignore does not remove tracked data.
5. Run the focused checks and affected behavioral scenarios. Submit a pull request describing the final change, observed verification and remaining limitations.

## Checks

From the canonical skill directory:

```sh
python3 scripts/validate_repository.py
python3 scripts/test_synthetic_host.py
```

The validator checks structure; it does not establish semantic quality. Use the finite cases in evals/evals.json and the evaluation reference for affected behavior. Record exact inputs, artifact revision, host capabilities, actual outputs and PASS/FAIL/NOT TESTED/BLOCKED. Keep generated outputs outside the source tree.

Do not turn synthetic tools or predetermined fixtures into claims about real connectors or provider accuracy. Provider interface, failure behavior, calibration, latency/cost and causal relationship outcomes require distinct evidence. Preserve errors and initial results when a focused corrective round is necessary.

## Attribution and license

Preserve source citations and relevant notices. Contributions are submitted under this repository's Apache License 2.0. Do not add third-party material unless its license permits distribution and the required attribution is included. No contributor agreement or signing workflow is required by this repository.

For vulnerabilities, use SECURITY.md rather than a public issue containing exploit details.
