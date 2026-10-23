# Relationship Intelligence

A standalone agent skill for developing deep, evolving understanding of the people you build relationships with: values, motivations, decision criteria, contextual patterns, tensions and shared history.

**PREPARE** a human for an upcoming conversation using recalled evidence, competing explanations and personalized natural questions that could refine the model. **DIGEST** the actual transcript or notes afterward, correct or enrich the model, and change the next preparation. This is an asynchronous learning cycle, not a live conversation manager or a generic CRM.

The concise [core](SKILL.md) selectively loads sixteen substantive references, eleven method contracts and six templates. Methods include interviewing and reflection, negotiation and value discovery, strategic elicitation, behavioral observation, consumer-depth research and psycholinguistics. The references retain source depth, conflicting findings and applicability limits. This evidence-informed composite is not a validated psychological instrument or proof of causal relationship/sales benefit.

## Install

Tell your agent:

> Read https://github.com/groktopus/relationship-intelligence and its README.md and SKILL.md. Install the complete skill in my chosen harness and project or user scope. Preserve any existing local changes, then verify discovery and demonstrate PREPARE and DIGEST with synthetic material.

The repository root is the canonical `relationship-intelligence` skill directory. Keep **the entire directory**, including `references/` and `assets/`; copying only SKILL.md breaks selective loading. No specific connector, memory service, model provider, runtime package or installation script is required. Reading SKILL.md in place is possible, but does not establish persistent discovery.

### Choose one scope

These locations were verified against the linked official documentation on October 23, 2026. Paths below are generic installation conventions, not personal environment dependencies.

| Harness | Project directory | Personal directory | Evidence |
| --- | --- | --- | --- |
| [Codex](https://developers.openai.com/codex/skills) | `.agents/skills/relationship-intelligence` | `~/.agents/skills/relationship-intelligence` | Actual project-scoped discovery/use tested with Codex 0.162.1. |
| [Claude Code](https://code.claude.com/docs/en/skills) | `.claude/skills/relationship-intelligence` | `~/.claude/skills/relationship-intelligence` | Documented conventions; execution blocked by authentication in testing. |
| [GitHub Copilot](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) | `.github/skills/relationship-intelligence` | `~/.copilot/skills/relationship-intelligence` | Documented, not runtime-tested; supported scopes depend on the Copilot surface. |
| [OpenCode](https://opencode.ai/docs/skills/) | `.opencode/skills/relationship-intelligence` | `~/.config/opencode/skills/relationship-intelligence` | Documented, not runtime-tested; Claude/agent-compatible locations also supported. |
| [Gemini CLI](https://geminicli.com/docs/cli/skills/) | `.gemini/skills/relationship-intelligence` | `~/.gemini/skills/relationship-intelligence` | Documented, not runtime-tested; `.agents/skills` aliases also supported. |
| [Cursor](https://cursor.com/docs/context/skills) | `.cursor/skills/relationship-intelligence` | `~/.cursor/skills/relationship-intelligence` | Documented, not runtime-tested; `.agents/skills` also supported. |

A personal installation on your machine is not automatically available to cloud agents or remote workers. Use the active surface's documented project distribution or synchronization mechanism. Avoid duplicate same-name installations in overlapping scopes.

### Git installation examples

For a **Codex project**, run at the target project's root:

```sh
mkdir -p .agents/skills
git clone https://github.com/groktopus/relationship-intelligence.git .agents/skills/relationship-intelligence
```

For **personal Claude Code** use:

```sh
mkdir -p "$HOME/.claude/skills"
git clone https://github.com/groktopus/relationship-intelligence.git "$HOME/.claude/skills/relationship-intelligence"
```

For another harness, substitute its chosen directory from the table. Git refuses to clone over an existing directory; inspect it instead of overwriting it. Alternatively download the source archive and place the complete canonical directory there. A supported local symlink to one maintained checkout is another option; verify your harness follows it.

Codex also documents `$skill-installer` for downloading skills from repositories. Gemini CLI documents `gemini skills install https://github.com/groktopus/relationship-intelligence.git --scope workspace`. Use the native manager's own confirmation and upgrade behavior; this repository provides no universal installer.

### Verify after installation

Confirm the chosen directory contains SKILL.md, references and assets. Ask the harness to list or load `relationship-intelligence`, then run a small synthetic PREPARE/DIGEST example and confirm the selected references can be read. Codex detects changes automatically; restart it if the skill does not appear. Gemini CLI documents `/skills reload`; for other harnesses use their documented refresh behavior or a fresh session. Installation locations alone do not prove runtime compatibility.

## Upgrade

Ask your agent:

> Inspect my installed Relationship Intelligence location, revision and local changes. Fetch the repository updates, summarize the relevant changes, preserve my edits, update the complete skill, and verify discovery plus PREPARE/DIGEST again. Do not assume that an earlier copy was Git-installed.

For a Git-installed skill, change into its installed directory and run:

```sh
git status --short
git rev-parse HEAD
git fetch origin
git log --oneline HEAD..origin/main
git diff --stat HEAD..origin/main
```

Review the changes. If the worktree is clean and you want the latest main branch:

```sh
git pull --ff-only
git rev-parse HEAD
```

If there are local edits or branches have diverged, stop and reconcile them; do not reset or overwrite them. For reproducible use, record the chosen published commit rather than assuming main will stay unchanged. A symlinked installation upgrades by updating its source checkout.

For an archive/copy installation, preserve the old copy and local edits, compare against a fresh source archive, then replace the **complete skill directory** with the reviewed version. Do not overlay only SKILL.md or leave obsolete reference files mixed with a new version. If a harness manager installed the skill, use its documented replacement/upgrade mechanism rather than assuming `git pull` applies.

After any upgrade, refresh discovery as above, confirm the installed revision and repeat the synthetic smoke. Relationship memory belongs to the host's memory facilities, not this distribution; keep it separate from skill code and upgrades.

## Use

- “Prepare for my next conversation with this collaborator. What hypotheses and gaps matter, and what could a natural question teach us?”
- “Digest this transcript. Which interpretations gained support, weakened or changed, and how should next preparation differ?”
- “Bootstrap people I already know from these selected historical sources, resolving aliases and preserving coverage gaps.”
- “Correct this relationship record and report what was actually updated.”

Examples illustrate requests to the agent, not fixed questions to ask people. Supplied text supports a useful no-persistence mode. Existing graph, temporal, search and linked-note capabilities can support richer recall and coordinated revision. Read-only/write-only gaps remain explicit. Optional decision models use the same evidence semantics as the complete language-model path; numerical equivalence is not assumed.

## Verification and contribution

[Release evidence](docs/release-evidence.md) distinguishes structural checks, observed synthetic behavior, mock host mechanics, actual harness discovery and provider qualification. All 22 cases have supporting observations within their declared setups; grouped/nonblinded contexts are disclosed. Provider-internal isolation and real-provider failure compatibility remain untested. No broad compatibility, calibrated accuracy or business-effect claim follows.

See [CONTRIBUTING.md](CONTRIBUTING.md), [AGENTS.md](AGENTS.md), [traceability](docs/traceability.md) and [evaluation](references/evaluation.md). Python is required for development checks only. For security reports see [SECURITY.md](SECURITY.md).

## License

[Apache License 2.0](LICENSE) for original skill content and development tools. Linked research remains under its authors' respective rights; source manuscripts are not redistributed.
