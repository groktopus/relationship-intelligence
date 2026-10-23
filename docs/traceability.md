# Requirements, artifacts, and verification

Candidate: 0.2.0. Design revision 6 is superseded for product orientation: the evolving person model is central; PREPARE and DIGEST form its asynchronous learning cycle. Methods review C remains the evidence basis. This checklist records coverage, not a claim that static wording proves behavior. Bind final verdicts to the content hash in release evidence. The finite suite has 22 cases; no open-ended gauntlet.

| Requirement | Artifacts | Release cases |
|---|---|---|
| R-00 Deep evolving person model / discriminating PREPARE / evidence-driven DIGEST | references/person-model.md; assets/hypothesis-card.md; preparation-brief.md; conversation-digest.md | 1,2,3,9,10,15 |
| R-01 Standalone/harness routing, concise core, license | README.md; SKILL.md; LICENSE; conditional references | 17; trigger cases |
| R-02 Authorized capabilities and honest fallback | references/capabilities.md; references/memory-lifecycle.md; assets/change-proposal.md | 11,12,13,14 |
| R-03 Bootstrap/canonical identity/deduplication/reversibility | references/memory-lifecycle.md; assets/bootstrap-checkpoint.md | 6,7,8,9 |
| R-04 Recall/add/modify/correct/supersede/remove/verify | SKILL.md; references/memory-lifecycle.md; assets/change-proposal.md | 7,8,9,10,11,12,13 |
| R-05 Evidence/context/alternatives/changed guidance | references/context-and-revision.md; assets/relationship-brief.md; evidence index | 2,3,6,9,10,16 |
| R-06 Adaptive elicitation without scripts/quotas | references/focus-and-elicitation.md; SKILL.md | 1,2,3,4 |
| R-07 Reflection/summary/pause/no inquiry | references/listening-and-pacing.md; references/calm-disagreement.md | 1,3,4,18 |
| R-08 Interests/tradeoffs/value/disagreement | references/negotiation-and-value.md | 4,5,18 |
| R-09 Optional bounded decisions and complete LLM fallback | references/decision-judgments.md | 2,14,15 |
| R-10 Evidence attribution, source-as-data and context-appropriate reporting | SKILL.md; capabilities; decision judgments; brief asset | 4,5,11,14,16 |
| R-11 Honest qualification/finite iteration/separate causal outcomes | references/evaluation.md; docs/release-evidence.md | all 22; especially17,18 |

## Design acceptance scenarios retained

All 28 design scenarios map into the 22 finite release cases: aliases/collisions(6), replay/resume(8), common-origin copies(8,15), late import(9), undo identity(7), disagreement/correction(3,10), sources/alternatives(2,3,5), changed guidance(3,9), no persistence(12), access gaps(12,13,14), injection/audience(16), notes-only(10,13), coordinated rich views(10,13), verification modes(11,12,13), removal(11), LLM fallback(14), independent/dependent batch(15), complete contracts(18), rubric no-fit(2,14), bounded evaluation(18), value development(4), harness discovery(17), requested advice(1), no inquiry(1,4), protected negotiation terms(5), conflicting claims(5), selective loading(17,18), and no offline-to-causal overclaim(18).

Every method MC-01 through MC-11 retains version, uncertainty, context, evidence needs, possible moves, alternatives, disconfirmation, stopping and source depth in its routed reference. Evidence records distinguish empirical results, methodological/practitioner guidance, correction/debate, and our extrapolation. No methods acquire validation merely by inclusion.

## Verification boundaries

- Static validator: structure, local links, metadata, counts, private-artifact exclusions. Not semantic quality.
- Behavioral exercises: observed outputs and, where applicable, synthetic host operations. Not actual connector compatibility.
- Harness discovery: separate real CLI check if available; unavailable/authentication-limited paths are BLOCKED or NOT TESTED, not passed by documentation.
- Optional live-provider comparison: separate from generic skill readiness; external pilot data/results stay outside the repository. No private data or credentials in distributable.
- Causal outcomes: not evaluated by these release cases.


## Expanded field requirements

- Strategic elicitation: references/strategic-elicitation.md; source records SE-01–06, doctrine versus empirical support, prompting context; cases 2, 3 and 18.
- Behavioral observation: references/behavioral-observation.md; source records BO-01–07, modality and context comparisons, mixed/null results; case 2 modality variant and case 18 review.
- Consumer-depth methods: references/consumer-depth-research.md; laddering, depth episodes, projective attribution, demand effects and coding; case 15 construct-fit variant and case 18 review.
- Psycholinguistics: references/psycholinguistics.md; seven sources, held-out and cross-language limits, contextual alternatives; case 2 modality variant and case 18 review.
- Purpose/context/anchors/markers/rubric fit: references/inquiry-design.md; MED-01/02; cases 2 and 15 variants and case 18 review.

Observed statuses and limitations are in release-evidence.md. These mappings establish where a requirement is taught and exercised, not proof of a validated psychological instrument.


## Corrected asynchronous cases 19–22

- 19: preparation suggestions versus supported conversation evidence; missing notes do not establish nonoccurrence.
- 20: contrary post-conversation evidence revises priorities and next inquiry with temporal/context scope.
- 21: partial paraphrases, uncertain attribution and fuller transcript corrections preserve source lineage.
- 22: recalled preparation, actual transcript digestion, verified coordinated memory delta and fresh-context next preparation; honest portable fallback.

Repeated-evidence case 2 and contrary-criteria case 4 have separately observed added variants. The original committed 18-case observations remain historical evidence; they are not silently relabeled as 22-case coverage.

## Persona preservation revision 0.3.0

Requirement: one attributed H1 Persona section, stable contract 1.0.0 H2 ordering, substantive observation-to-hypothesis derivation, alternatives, time and adaptive inquiry. Artifacts: references/persona-output-contract.md and assets/persona-section-example.md; core and memory lifecycle route to them. Offline regression: scripts/test_persona_handoff.py checks content loss, chronology substitution, false persistence and conflicting authorities. Actual harness roundtrip evidence is recorded separately; structural checks do not establish semantic quality.

## Semantic completeness refinement (local proposal)

Evidence-proportional depth, individual review regardless of queue size, source coverage versus unperformed analysis, cross-conversation connections, contextual exceptions and temporal correction route through `references/persona-semantic-quality.md`, the core synthesis route and the existing Persona output contract. `evals/persona-semantic-quality.json` supplies seven synthetic contrast cases: rich skeletal/grounded, sparse bounded/padded, template-only, honestly incomplete analysis and useful narrative with pooled confidence. `scripts/test_persona_semantic_fixtures.py` verifies fixture integrity only; actual semantic review must record outputs and reasons separately. Format, analytical acceptance and persistence fidelity remain distinct gates.
