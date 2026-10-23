# Persona output contract — 1.0.0

Load when creating, bootstrapping, revising or handing off a persistent person model. This contract fixes the presentation and preservation boundary; the methods still determine the substance. A chronology, a set of preferences or filled headings alone is not a person model.

## One canonical section

Maintain one `# Persona` section in the existing authoritative person record. Do not replace the whole note, change its unrelated headings/frontmatter, or create another authoritative profile to satisfy this format. Recall existing content, identity, user edits and later corrections first. If an existing persona has another heading, reconcile/migrate that section once; never leave two contradictory current personas. If a single managed boundary cannot be identified reliably, leave the change proposed with its target and content.

The first paragraph names **Relationship Intelligence**, links to its [core](https://github.com/groktopus/relationship-intelligence/blob/main/SKILL.md) and [update contract](https://github.com/groktopus/relationship-intelligence/blob/main/references/persona-output-contract.md), and records contract version **1.0.0**. This concise attribution tells a later reader how the section was derived and should evolve. Keep execution logs, write receipts and staging paths outside the persona prose.

Use these exact H2 headings in this order, with no further H1 inside the section:

1. `## Integrated understanding`
2. `## Evidence and temporal scope`
3. `## Confidence and alternatives`
4. `## Communication implications`
5. `## Adaptive questions and model updates`

Use connected paragraphs; H3 hypothesis subheadings and compact lists are optional. There is no length or hypothesis-count quota. Keep every section even when the truthful content is a specific unknown or limited account; do not pad sparse evidence into apparent depth. Other H1 sections elsewhere in the host note remain untouched. The managed Persona ends at the next H1 or end of record.

## Substance and derivation

**Integrated understanding:** Explain the useful pattern, not just what happened. Connect attributed observations to plausible values, motivations, decision processes, working patterns and tensions. State what is directly expressed versus inferred. Scope the explanation to the observed relationship, role, period and circumstances. A limited model may say one event suggests a particular decision criterion while broader motivations remain unknown. Do not force every dimension or turn a population association into an individual finding.

**Evidence and temporal scope:** Use resolvable source references and precise passages/times where available. Identify source kind, actual attribution, date precision and relevant omissions. Distinguish event dates, import dates and unknown dates. Each material hypothesis must have a traceable supporting basis; multiple exports of one event are not independent support. Cite relevant contrary evidence. Summarize what new evidence changed or why no revision is justified. Historical imports cannot silently supersede newer applicable evidence.

**Confidence and alternatives:** Explain the strength of each consequential inference, why it is supported and what remains uncertain. Retain a plausible situational or competing account and counterevidence where present. Use qualitative confidence with reasons, not a global numerical personality score. Directly stated preference can be well-supported while its generalization remains tentative. Corrections govern the working interpretation rather than being appended beside a stale story.

**Communication implications:** Explain how the current understanding changes useful collaboration or preparation. Distinguish a stated preference from a suggested adaptation. Give practical advice when requested; do not turn every interaction into inquiry. A new interest or benefit is a possibility to explore against priorities, costs and alternatives, not an assumed outcome.

**Adaptive questions and model updates:** Select consequential gaps from this person's actual history. For each useful optional question/reflection, state what it could distinguish, plausible interpretations, what would disconfirm or narrow the leading account, and how guidance would change. Suggested wording is unobserved preparation, not a script or evidence it occurred. Recall prior answers; do not repeat them without a reason. If no inquiry is useful, say what practical action or new evidence would permit a future revision instead.

See [person model](person-model.md) for deeper reasoning, [memory lifecycle](memory-lifecycle.md) for changes and identity handling, and [synthetic example](../assets/persona-section-example.md) for the format. Examples demonstrate derivation; do not copy them as conversation scripts.

Analytical acceptance is governed separately by the [semantic quality contract](persona-semantic-quality.md). Pass that source-aware review before treating a formatted proposal as complete; save fidelity cannot compensate for underanalysis.

## Handoff and semantic persistence acceptance

Send the writer the actual proposed Persona prose, target canonical reference, supporting evidence, intended revisions and content to preserve. Explicitly retain interpretations as interpretations; a facts-only rule must not discard them. The writer recalls current state and reconciles the model, including stronger later evidence and user edits, rather than blindly appending the proposal.

Before a save, establish the intended managed section and preserve the outside-note content. After a supported write, retrieve the canonical record and inspect the actual Persona section. Compare it with the intended reconciled model:

- Is the explanation present, with evidence-to-hypothesis derivation rather than only chronology?
- Did confidence, alternatives, contextual qualifications and corrections survive?
- Are the consequential gaps and answer-dependent revisions present, rather than generic questions?
- Is there one current authoritative persona, with unrelated note content and user edits preserved?
- Does retrieval return that model from the intended record?

Report proposed, attempted, uncertain and confirmed operations separately. No readback means no verified save; a write receipt or format check is insufficient. Read-only/no-memory operation supplies this same useful model as an explicitly unapplied delta. Write-only access cannot prove recall, deduplication or maintained memory. Reconcile uncertain outcomes before retrying.

The optional offline `scripts/check_persona_handoff.py` checks a proposed section's structure and exact retained content against supplied readback and authority metadata. It neither reads a live store nor judges psychological quality; the semantic questions above still require actual review. Run its synthetic regression tests with `python3 scripts/test_persona_handoff.py`. No connector or provider is required.

## Versioning

The section records the contract that produced it. Future contract revisions must document meaningful format changes and preserve substantive user edits, evidence and corrections during migration. A version upgrade alone supplies no new evidence about the person. Keep the stable guidance link and record the new version only when the section has actually been reconciled to it.
