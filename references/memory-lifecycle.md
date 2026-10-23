# Memory lifecycle, identity and historical bootstrap

Load before persistent maintenance, identity resolution or historical bootstrap. Use the host's existing structure and authorization; the steps below specify observable behavior, not a required schema or storage implementation. Consult [capabilities](capabilities.md) for actual mode and coordination rules.

## Feed the asynchronous cycle

PREPARE recalls the current relationship before offering a small optional approach or personalized questions and their reasons. Preserve these as preparation suggestions only if useful and authorized; they are unobserved, not a transcript, a script or evidence about the person. DIGEST works afterward from supplied notes or preferably a transcript, compares actual content with prior understanding, applies verified authorized updates and returns implications for the next preparation. Bootstrap contributes dated history to this cycle. No live capture, streaming or infrastructure is required.

Keep provenance explicit:

- **Preparation suggestion:** proposed wording, approach or possible commitment; no evidence it occurred.
- **Actual spoken evidence:** retain the attributed passage and source basis establishing it was said; do not elevate its contents automatically to fact.
- **Human retrospective notes:** attribute to the note author and conversation/date if known; retain recall, selection and paraphrase limits. A note describing speech is not an exact quotation without support.
- **Transcript:** retain speaker attribution, source spans/times and known omissions or ASR uncertainty. Resolve material speaker ambiguity before assigning a claim; missing or mistranscribed content remains uncertain.
- **Commitment:** distinguish a suggestion or request from explicit acceptance. Track who accepted what, with supported owner, conditions and timing. No answer or silence establishes acceptance.

During DIGEST, identify what was actually discussed, what remains unanswered and what diverged from preparation. Never infer that suggested questions were asked or anticipated answers were received. A transcript is preferred for detailed grounding, but usable notes still support a bounded attributed digest. Do not block useful work simply because no transcript exists.

## Maintain an evolving model

Use [Persona output contract](persona-output-contract.md) for stable formatting, named skill attribution, writer handoff and semantic readback acceptance. Preserve one current section within the existing authoritative record.

Use [person-model](person-model.md) for the central evidence-grounded understanding: values/priorities, decision criteria, communication patterns, supported motivations, tensions, competing hypotheses and qualitative confidence/gaps. These remain contextual, revisable hypotheses where inference is involved, not facts. Preserve identity anchors, source history and user edits through every revision.

During PREPARE, tie each optional personalized information-gathering move to a meaningful model uncertainty. Privately record what it could teach, plausible interpretations, disconfirmation and limits; offer natural optional follow-up branches rather than scripts or a required sequence. During DIGEST, compare actual evidence against each relevant hypothesis, including counterevidence and context changes. Strengthen, narrow, weaken, retire or leave a hypothesis unresolved only as the evidence warrants; use qualitative confidence with a reason, not invented numerical certainty. Recompute next-preparation implications from the revised understanding. A successful interaction, agreement or sale does not validate a hypothesis.

## Recall, interpret, change, verify

1. **Recall first.** Retrieve the person's current relevant understanding, aliases, linked evidence, corrections, user edits and commitments before reasoning about new evidence. Inspect source passages; do not reconstruct exact quotations, identifiers or dates from model memory. State incomplete search coverage.
2. **Classify the evidence.** Distinguish self-report, attributed third-party claim, observed behavior in a stated setting, supported external fact, hypothesis and unknown. A quotation proves what was said, not necessarily its truth. A copied summary and its original are one evidentiary origin.
3. **Resolve time and apparent conflict.** Separate event/applicability time, time learned and import time; retain precision and timezone when known. Unknown dates stay unknown. Consider changed circumstances, context-specific preference, source disagreement, mistaken identity, transcription error or incorrect inference. New ingestion alone never wins.
4. **Specify the intended delta.** Identify the existing target, evidence, authorized operation, current-view effect, history to retain, user edits to preserve and dependent views affected. Use [change-proposal](../assets/change-proposal.md) when helpful. Keep incompatible accounts attributed until evidence resolves them.
5. **Apply only authorized supported operations.** Use the smallest change that improves the understanding. If a safe reversible history is unavailable, provide an unapplied proposal for the affected change. Never silently rewrite source text.
6. **Verify the persisted delta.** Inspect the mutation result, then retrieve the authoritative record and affected guidance using supported lookup/search. Compare before and after: intended change present, correction retained, useful history/user edits preserved, no duplicate authoritative identity/evidence/commitment introduced, dependent views current or explicitly stale. A success receipt alone is insufficient retrieval verification.
7. **Report the compact result.** Separate proposed, attempted, confirmed and uncertain operations. Include new evidence, corrected understanding, changed priorities, commitments, unresolved questions and next-conversation implications. Do not claim completion for unchecked propagation.

If a write times out or returns an ambiguous result, inspect the target and operation/source reference before retrying. If inspection cannot determine whether it happened, mark the outcome uncertain and stop that mutation; a blind retry can duplicate it. Resume only after state is established or a supported idempotent mechanism makes the retry safe.

## Choose the operation deliberately

| Operation | Use and preservation rule |
| --- | --- |
| Add | Retain useful new evidence or a commitment with origin, attribution and time. Avoid retaining every conversational detail. |
| Modify | Refresh the contextual current understanding when supported facts, goals or priorities change; preserve relevant prior states and user edits. |
| Correct | Remove an erroneous inference from current guidance, attach the correction and identify affected derived views. Preserve appropriate correction/source history. |
| Supersede | Mark an older claim as historical in its applicable context and replace its current implication; do not erase evidence of what was previously said. |
| Deduplicate | Link repeated exports, quoted chains, cross-posts and copied summaries to their common origin. Retain distinct revisions and contexts. Copies do not increase corroboration. |
| Merge/split identity | Require evidence and safe reversibility; preserve original source associations, rationale and downstream effects. Recompute summaries without moving another person's claims or losing edits. |
| Remove | Require applicable authorization and retention rules. Remove the selected material and dependent derived content/index entries where supported; do not reintroduce it through a later import or retained excerpt. Keep only a permitted minimal deletion marker if needed for that purpose. |

Removal overrides routine source-history preservation for the material covered by the deletion/retention instruction. Do not preserve deleted content under the label of an audit trail. Describe unavailable propagation precisely and exclude affected residual projections from current guidance.

## Canonical identity without name-based merging

Use the host's stable reference for one actual person. Retain preferred/current names and source-supported nicknames or spelling variants as aliases. Names, semantic similarity and fuzzy matches generate candidates only.

Inspect already verified anchors with their source and verification context: a stable profile reference, attributed business contact or user-confirmed identity, alongside relevant organizational and conversational context. Do not collect additional personal data merely to force resolution. Shared inboxes, recycled addresses, changed roles and common names can defeat an apparent match. Identity persists beyond an old job/account; a role is not a person.

Keep ambiguous records separate or unresolved with candidate links. Merge only when the evidence supports it and the host can safely undo the decision. Before merging, record original associations, rationale and affected summaries/projections using existing mechanisms. A split restores those associations, corrects misattributions and refreshes guidance while preserving user edits. If reversibility cannot be supported, propose the merge or repair rather than performing it automatically.

**Synthetic identity example:** “Jordan Lee” and “J. Lee” appear in selected notes. Search and read their contexts first. A user-confirmed alias and verified profile reference support one identity; a similar name at another organization remains separate. A shared team address is insufficient. If a later correction reveals two people, restore each source to its original person, remove mixed claims from both current summaries, preserve the correction and verify both retrievals and any linked views.

## Bounded, resumable historical bootstrap

Bootstrap covers selected people already known to the user and selected authorized sources. It does not authorize importing all contacts, searching unrelated accounts or creating access. Establish a concrete people/group scope, source set, event-date range, destination, batch bound and stopping point from the request; resolve a material ambiguity before expanding the pass.

1. Recall existing records and confirmed checkpoints first. Check recent corrections and user-maintained notes before opening the archive.
2. Select a small batch within scope. Use stable source references and content/version fingerprints where supported to distinguish unchanged imports, revised exports and new content. Do not invent unavailable fingerprints or persistent state.
3. Read the batch, track examined coverage and attribution, resolve only supported identities, and identify duplicate origins before proposing changes. Preserve event dates separately from import dates; export timestamps do not establish meeting dates.
4. Apply the lifecycle above to authorized changes. Historical evidence enters history first; compute current guidance using applicable dates, corrections and context. Older material imported today cannot silently displace a later valid correction.
5. Save a checkpoint only for confirmed work using existing host conventions. Record uncertain operations separately and reconcile them before continuing that portion. Use [bootstrap-checkpoint](../assets/bootstrap-checkpoint.md) as a portable aid, not a mandated store format.
6. Resume from the last confirmed boundary. Recheck changed source versions and uncertain outcomes. Rerunning unchanged completed material should create no duplicate people, evidence or commitments. Stop at the requested scope/budget; report the remaining work.

Checkpoint coverage must distinguish examined, skipped, inaccessible, unsearched and partial material, including missing attachments or truncated transcripts. A completed batch is not a complete relationship history. With no persistence, provide a portable checkpoint and disclose that durable resumption and deduplication are not guaranteed. With read-only access, checkpoint analysis/proposals without presenting them as applied updates. With write-only access, disclose that existing state and duplicate prevention cannot be verified; do not claim a bootstrapped maintained library.

## Synthetic temporal correction walk-through

In January, Casey states that exploring partnerships is a priority and requests a short comparison before meetings. In April, Casey says delivery stability takes priority through June. A January archive arrives in May.

Recall April's current view and source before processing January. Add the January source to the historical context only if it is not already present. Keep April's delivery priority current, with the format preference scoped to its evidence rather than turned into a trait. If Casey later corrects “June” to “August,” replace the current timing implication, preserve the correction, refresh dependent views and retrieve the changed guidance. The next move should acknowledge delivery needs and defer partnership exploration appropriately. Reimporting a quoted copy of April adds no corroboration. One delayed reply supplies no enduring personality conclusion.
