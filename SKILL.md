---
name: relationship-intelligence
description: >-
  Develop deep, evolving understanding of people the user builds relationships
  with. Use to form evidence-grounded psychological hypotheses, prepare
  personalized conversations that refine them, digest transcripts or notes,
  reconcile changing priorities, and bootstrap or maintain relationship memory.
license: Apache-2.0
metadata:
  version: "0.2.0"
---

# Relationship Intelligence

Build a rich, revisable model of the people the user knows: their values, motivations, priorities, decision criteria, contextual patterns, tensions and shared history. Help the user structure upcoming conversations to deepen that understanding, then learn from what actually happened. Preparation and digestion are an asynchronous learning cycle, not a live conversation manager.

The methods are an evidence-informed composite. Operationalize uncertainty through competing explanations, grounded observations, consequential gaps and correction. Seek progressively more useful understanding rather than elaborate labels.

## Start with the person model

Read [person model](references/person-model.md) for hypothesis formation, discriminating inquiry and longitudinal revision. Recall the relevant existing model, original evidence, recent corrections and prior answers before reasoning. Identify the person through supported identity anchors; retain ambiguous candidates separately. Distinguish direct statements, observed behavior, attributed claims and interpretations. Preserve event time and context; repeated copies or judgments over one passage are one observation.

Model depth means explaining patterns and tensions, not accumulating facts. Connect evidence to plausible motivations, values and decision processes; compare situational explanations and counterexamples. State qualitative confidence with reasons. Identify a gap that could materially change understanding or guidance.

## PREPARE the human

1. Establish the upcoming conversation's purpose and relevant shared history. Recall what is already known and what has changed.
2. Select the most consequential uncertainty or competing hypotheses. Explain why learning the distinction matters.
3. Choose appropriate methods below. Offer a small set of optional personalized questions, reflections or approaches, not a script or question quota. Give requested practical advice directly.
4. For each move, explain privately what it could teach, plausible answer interpretations, disconfirming evidence, limits and natural follow-up branches. Generate wording from this person's language, actual history and current context; do not copy examples as routine scripts.
5. Include practical implications: how different findings could change collaboration, a proposal, timing or the next conversation. Interests can develop through exploring real possibilities; test a benefit against costs, alternatives and competing priorities, including a no-fit conclusion.

Use [preparation brief](assets/preparation-brief.md) selectively. A useful question can feel like genuine curiosity because it follows something real worth understanding. Its value is the distinction it could illuminate, not an impressive psychological label.

## DIGEST the conversation

Use the actual transcript or written notes. Separate speakers, quoted wording, paraphrases, uncertain attribution and later recollection. Preparation suggestions are not evidence that something was asked or said.

Compare new observations with the recalled model. Explain which hypotheses gained support, weakened, narrowed, were overturned or remain unresolved. Incorporate corrections, contextual exceptions and changed priorities. Enrich the account of motivations, decision criteria and tensions where evidence supports it. Translate the revision into changed guidance and the next consequential gap, rather than merely summarizing a meeting.

Use [conversation digest](assets/conversation-digest.md) or [hypothesis card](assets/hypothesis-card.md) where useful. An answer can support several interpretations. If a rubric does not fit the wording or context, interpret qualitatively or retain unknown; do not invent a score.

## Select methods, not scripts

Load only the references needed. Each contract states purpose, context, evidence, alternatives, possible moves, disconfirmation, stopping and source depth.

- Meaning or useful learning focus: [focus and elicitation](references/focus-and-elicitation.md), MC-01/02.
- Understanding, multiple concerns, pacing, reflection, summary or no inquiry: [listening and pacing](references/listening-and-pacing.md), MC-03/04/05.
- Competing explanations, metaphor corrections, contextual patterns or evolving priorities: [context and revision](references/context-and-revision.md), MC-06/11.
- Interests versus positions, tradeoffs, potential value and information under incentives: [negotiation and value](references/negotiation-and-value.md), MC-07/08/09.
- Preparing for or interpreting tense disagreement: [calm disagreement](references/calm-disagreement.md), MC-10.
- Evidence quality, contested findings or transfer limits: [evidence index](references/evidence-index.md).

For deeper investigations, route by the kind of evidence and learning opportunity:

- Conversational information gathering and correction effects: [strategic elicitation](references/strategic-elicitation.md). Distinguish professional doctrine from tested findings and account for interviewer-created responses.
- Demeanor, baseline comparisons, forensic interviewing or modality: [behavioral observation](references/behavioral-observation.md). Use only observations the source actually contains; evaluate competing causes of change.
- How concrete choices connect to consequences and values: [consumer-depth research](references/consumer-depth-research.md). Use adaptive laddering or depth inquiry, keeping elicited meaning separate from inferred traits.
- Patterns in language across adequate text: [psycholinguistics](references/psycholinguistics.md). Check corpus, context, validation and individual calibration before transferring population associations.
- Question purpose, real contextual anchors, observation markers and response-rubric fit: [inquiry design](references/inquiry-design.md). Preserve the chain from competing explanations to evidence and revision; adapted wording does not inherit validation automatically.

## Recall and evolve memory

Before bootstrap, identity resolution or persistent modification, read [capabilities](references/capabilities.md) and [memory lifecycle](references/memory-lifecycle.md). Use existing host capabilities progressively: graph for connected context, temporal records for change, search for relevant evidence, linked notes for readable knowledge. No particular backend or schema is required.

Bootstrap from selected historical sources with bounded coverage, resumable checkpoints and idempotent imports. Resolve aliases with evidence beyond name similarity. Preserve source associations through reversible merges or splits. Recall before adding; selectively modify, correct, supersede, deduplicate or remove as the task requires. Preserve user edits and source history while updating dependent views.

Verify persisted changes and retrieval where supported. Inspect uncertain writes before retrying. Read-only or no-memory operation still produces useful understanding and an explicitly unapplied delta. Write-only access cannot establish recalled context, deduplication or verified maintenance. Report exact capability gaps and residual changes.

## Optional decision assistance

Read [decision judgments](references/decision-judgments.md) when response-level classification helps. The main language model is a complete path; a suitable available decision model is optional. Use the same evidence packet, question/answer/context separation, versioned decision contracts, grounded spans and unknown meanings. Independently specified typed judgments may share a batch; dependent judgments require staging. Multiple judgments of one answer are not independent corroboration.

The main agent synthesizes the result into contextual hypotheses and alternatives. Qualify each model path separately; numerical equivalence, psychological validity, speed and accuracy are not assumed. If a provider fails or a contract is unsuitable, continue the useful language-model path without forcing scores.

## Deliver the learning

Give the user a purpose-specific result: the evolving understanding with evidence, consequential uncertainty, optional personalized preparation or retrospective revisions, implications for the next interaction, and proposed or verified memory changes. Use [relationship brief](assets/relationship-brief.md), [change proposal](assets/change-proposal.md) or [bootstrap checkpoint](assets/bootstrap-checkpoint.md) when helpful.

Stop when the selected purpose is met or further useful evidence is unavailable. For qualification, read [evaluation](references/evaluation.md). Offline contract performance and actual relationship or sales outcomes require distinct evidence.
