# Sales and Cold-Calling Toolkit for Claude

Open-source Claude skills, plugins and agents that teach Claude (Claude Code, Claude.ai, Cowork) to prospect, cold call, handle objections, run discovery and apply named sales methodologies (SPIN, Challenger, Sandler, MEDDIC/MEDDPICC, Voss-style negotiation).

Each repo under `repos/<owner>__<repo>/` is a shallow snapshot taken on 2026-10-22 with its `.git` folder removed, so these are plain files. They are **untrusted third-party content**. Nothing has been run or installed. Read any `scripts/`, `*.py`, `*.ts` or hook files before you use them. The Markdown skills need no code to work.

Total size: about 47 MB, 10 repos.

## Start here (ranked for cold calling)

1. **`TheCraigHewitt__skills/sales/cold-call/SKILL.md`** is the most complete cold-call skill in the set (about 500 lines). It covers benchmarks, call timing by persona, openers, gatekeepers, voicemail and dial blocks. Its sibling skills `objection-handling`, `discovery-call`, `call-debrief`, `outbound-sequence` and `sales-context` work as a group.
2. **`mbfinotti__sales-skills/skills/cold-call-opener/`**, together with `sales-objection-handling`, `sales-discovery-questions` and `sales-call-review`, is carefully sourced. It reports Gong and Cognism data honestly, interviews you before drafting, and produces testable opener variants. It also covers DNC scrubbing.
3. **`anthropics__knowledge-work-plugins/sales/`** is Anthropic's official sales plugin. It has `handle-objection`, `call-prep`, `call-summary`, `draft-outreach` and `account-research`, and `small-business/skills/call-list` is also useful. It's the best-maintained option and is designed to plug into CRM connectors.
4. **`guia-matthieu__clawfu-skills/skills/sales/`** gives deep, methodology-specific skills: `spin-selling`, `challenger-sale`, `sandler-system`, `meddic-scorecard` and `never-split-difference` (Chris Voss). Also see `validation/objection-mapping` and `sdr-automation/`.
5. **`gtmagents__gtm-agents/plugins/sales-prospecting/`** and **`plugins/sales-calls/`** are full Claude Code plugins with agents, commands and skills. They cover cold-outreach, objection-handling, discovery-calls, the meddic-checklist and call-analysis-framework. `plugins/sales-coaching/` adds reinforcement drills.
6. **`louisblythe__Sales-Skills/skills/`** has 122 small, focused skills: `objection-handling`, `objection-recognition`, `building-rapport`, `voicemail-drop-optimization`, `callback-scheduling`, `micro-commitment-stacking`, `dynamic-script-generation`, `asking-effective-questions` and `discovery`.
7. **[Cold-IQ/ColdIQ-s-GTM-Skills](https://github.com/Cold-IQ/ColdIQ-s-GTM-Skills)** (*link only, not downloaded: the repo has no license*), `skills/cold-call-scripts/` (with `references/objections.md`) contains a 5-step one-minute script and a no-show script. `sdr-master-prompts`, `sdr-outbound-rules` and `buying-signals-6` are also useful. Note that these skills include a "ColdIQ first" block that pushes ColdIQ's paid MCP/API, so delete that block if you don't use ColdIQ.
8. **`OneWave-AI__claude-skills/`** includes `sales-methodology-implementer` (MEDDIC, BANT, Sandler, Challenger, SPIN), `objection-pattern-detector`, `sales-call-prep-assistant`, `prospect-panel-simulator` (for role-play) and `sales-coaching-plan-generator`.
9. **`zubair-trabzada__ai-sales-team-claude/`** is a Claude Code "sales team" with 14 skills and 5 parallel agents. Use `skills/sales-objections`, `sales-prep`, `sales-qualify` (BANT and MEDDIC) and `sales-outreach`. It's more about research and pipeline work than live calls.
10. **`vonarmen-wq__forward-deployed-selling/`** is a single-skill enterprise sales methodology (`SKILL.md` plus `references/`). It suits large, multi-stakeholder deals and is less relevant to cold calls.

## Repo table

Star counts and licenses come from the GitHub API on 2026-10-22.

| Repo | Stars | License | Useful for | Most important files |
|---|---|---|---|---|
| [TheCraigHewitt/skills](https://github.com/TheCraigHewitt/skills) | 163 | MIT | Cold calls, objections, discovery and debriefs for founders and SDRs | `sales/cold-call/SKILL.md`, `sales/objection-handling/`, `sales/discovery-call/`, `sales/call-debrief/`, `sales/sales-context/` |
| [mbfinotti/sales-skills](https://github.com/mbfinotti/sales-skills) | 2 | MIT | Evidence-based cold-call openers, rebuttals, call review, MEDDPICC | `skills/cold-call-opener/`, `skills/sales-objection-handling/`, `skills/sales-discovery-questions/`, `skills/sales-call-review/`, `skills/meddpicc-scorecard/` |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | 31.5k | Apache-2.0 | Official Anthropic sales plugin: objections, call prep and summaries, outreach | `sales/skills/handle-objection/`, `sales/skills/call-prep/`, `sales/skills/call-summary/`, `sales/skills/draft-outreach/`, `small-business/skills/call-list/` |
| [guia-matthieu/clawfu-skills](https://github.com/guia-matthieu/clawfu-skills) | 150 | MIT | Named methodologies: SPIN, Challenger, Sandler, MEDDIC, Voss negotiation | `skills/sales/spin-selling/`, `skills/sales/challenger-sale/`, `skills/sales/sandler-system/`, `skills/sales/never-split-difference/`, `skills/validation/objection-mapping/` |
| [gtmagents/gtm-agents](https://github.com/gtmagents/gtm-agents) | 428 | Apache-2.0 | Claude Code plugins with agents for prospecting, sales calls and coaching | `plugins/sales-prospecting/`, `plugins/sales-calls/`, `plugins/sales-coaching/`, `plugins/sales-enablement/` |
| [louisblythe/Sales-Skills](https://github.com/louisblythe/Sales-Skills) | n/a (not in API search) | MIT (stated in README, no LICENSE file) | 122 granular conversational-selling skills | `skills/objection-handling/`, `skills/objection-recognition/`, `skills/building-rapport/`, `skills/voicemail-drop-optimization/`, `skills/discovery/` |
| [Cold-IQ/ColdIQ-s-GTM-Skills](https://github.com/Cold-IQ/ColdIQ-s-GTM-Skills) | 305 | **None** (no license file, so all rights reserved; use for personal reference only) | Cold-call scripts, SDR prompts, triggers, cold email | `skills/cold-call-scripts/` (+ `references/objections.md`), `skills/sdr-master-prompts/`, `skills/sdr-outbound-rules/`, `skills/gtm-plays-11/` |
| [OneWave-AI/claude-skills](https://github.com/OneWave-AI/claude-skills) | 367 | MIT | Methodology implementer, objection patterns, prospect role-play | `sales-methodology-implementer/`, `objection-pattern-detector/`, `sales-call-prep-assistant/`, `prospect-panel-simulator/` |
| [zubair-trabzada/ai-sales-team-claude](https://github.com/zubair-trabzada/ai-sales-team-claude) | 1.5k | MIT | Multi-agent prospect research, qualification, objection prep | `skills/sales-objections/`, `skills/sales-prep/`, `skills/sales-qualify/`, `sales/` (orchestrator) |
| [vonarmen-wq/forward-deployed-selling](https://github.com/vonarmen-wq/forward-deployed-selling) | 75 | Apache-2.0 | Enterprise deal methodology (stakeholders, deal velocity) | `SKILL.md`, `foundations.md`, `references/stakeholder-profiles.md`, `references/movements.md` |

No high-quality NEPQ-specific repo turned up. NEPQ-style questioning (problem awareness, consequence and commitment questions) overlaps most with the SPIN and Sandler skills in clawfu-skills and with `louisblythe__Sales-Skills/skills/asking-effective-questions`.

## Using these with Claude

**Claude Code (personal, all projects):** copy individual skill folders. A folder is anything that contains a `SKILL.md`.

```bash
mkdir -p ~/.claude/skills
cp -r sales-tools/repos/TheCraigHewitt__skills/sales/cold-call ~/.claude/skills/
cp -r sales-tools/repos/mbfinotti__sales-skills/skills/cold-call-opener ~/.claude/skills/
cp -r sales-tools/repos/guia-matthieu__clawfu-skills/skills/sales/spin-selling ~/.claude/skills/
```

**Claude Code (one project only):** copy the same folders into `<project>/.claude/skills/` instead.

**Plugins:** `anthropics__knowledge-work-plugins/sales` and `vonarmen-wq__forward-deployed-selling` have `.claude-plugin/plugin.json`. `gtmagents__gtm-agents` ships a root `.claude-plugin/marketplace.json` that covers its `plugins/*`. In Claude Code, add a local marketplace or plugin path with `/plugin marketplace add <path>`, then install with `/plugin`. You can also copy just their `skills/` subfolders into `.claude/skills/` and their `agents/*.md` into `.claude/agents/`.

**Claude.ai / Claude Desktop:** zip a single skill folder (with `SKILL.md` at the root of the zip) and upload it under Settings > Capabilities > Skills. Alternatively, paste the `SKILL.md` body into a Project's instructions.

Tips:
- Install a few complementary skills rather than everything. Many repos have overlapping skills (for example, five different "objection-handling" skills), and similar descriptions make Claude pick inconsistently.
- Several skills read a shared context file first, such as `.agents/sales-context.md` in TheCraigHewitt's set. Fill it in once with your ICP, offer and proof points, and every script improves.
- For call practice, ask Claude to role-play a skeptical prospect using `prospect-panel-simulator` (OneWave) or the objection lists. Then grade the transcript with `sales-call-review` (mbfinotti) or `call-debrief` (Craig Hewitt).
- Cold-calling rules vary by jurisdiction (TCPA, DNC lists, GDPR, recording consent). The mbfinotti opener skill covers DNC scrubbing, but check local law.
