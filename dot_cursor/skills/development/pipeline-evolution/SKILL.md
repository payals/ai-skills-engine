---
name: pipeline-evolution
description: Harvest insights from completed pipeline runs and promote them into the pipeline's control plane files and phase prompts. Use when the user says "evolve", "evolve pipeline", "pipeline evolution", "self-improve", or after Phase 5/6 completes.
---

# Pipeline Evolution

Systematically extract lessons from a completed (or partially completed) pipeline run and promote them into the pipeline's persistent "DNA" — control plane files, phase prompts, and orchestrator checks — so the next run benefits automatically.

## When to Use

- After Phase 5 or 6 completes (richest insight set from QA + battle test)
- Before `reset-all` (harvest insights before scratchpad gets wiped)
- Between RFP runs (adapting the pipeline for a different RFP)
- When the user explicitly requests pipeline evolution

## Insight Sources

Read ALL of the following. Skip any that don't exist yet.

| Source | What it contains |
|---|---|
| `99_scratchpad/pipeline_memory.md` | Operational log per phase — `[FIX]`, `[WARN]`, `[NOTE]` entries |
| `99_scratchpad/discovered_facts.md` | Domain knowledge discovered during execution |
| `99_scratchpad/phase_handoff_notes.md` | Phase-to-phase context, especially "Surprises" and "Watch out for" |
| `.cursor/napkin.md` | Agent-level memory: mistakes, corrections, surprises, preferences |
| `10_battle_test/battle_test_summary.md` | Battle test verdict and must-fix list |
| `09_reviews_and_qa/*/review_findings.md` | Expert reviewer findings |
| `pipeline/phase_log.md` | Phase completion timestamps and issue counts |
| `pipeline/evolution/promotion_history.md` | Previously promoted insights (dedup check) |
| `pipeline/evolution/evolution_log.md` | Prior evolution session summaries (context for what was already done) |

## Promotion Targets — What Can Be Evolved

Evolution ONLY modifies pipeline DNA files. It never touches source documents, generated content, requirements engine outputs, or research evidence.

| Insight Type | Target File |
|---|---|
| Claim correction | `00_control_plane/claim_validation_rules.md` |
| Style / writing rule | `00_control_plane/response_style_guide.md` |
| Architecture decision | `00_control_plane/technology_stack_decisions.md` |
| Process improvement | `pipeline/prompts/phase*.md` (relevant phase) |
| QA check to add | `pipeline/prompts/phase5_qa.md` |
| Orchestrator verification | `pipeline/orchestrate.sh` (check functions) |
| Agent behavior only | `.cursor/napkin.md` (stays there, not promoted) |

## The 4-Step Workflow

Execute these steps in order. Do not skip steps.

### Step 1: Harvest

Read every insight source listed above. For each actionable item, extract:

- **Source file** and line/bullet where it appears
- **Type**: one of `bug_fix`, `style_rule`, `claim_correction`, `architecture_decision`, `process_improvement`, `performance_insight`
- **Severity**: `critical`, `high`, `medium`, `low`
- **Raw text**: the original insight verbatim

Check each item against `pipeline/evolution/promotion_history.md`. If the same insight (or a substantially similar one) was already promoted, skip it.

Write all NEW items to `pipeline/evolution/pending_insights.md` under the current date heading, using this format:

```markdown
## YYYY-MM-DD Harvest

| # | Type | Severity | Source | Raw Insight |
|---|---|---|---|---|
| 1 | bug_fix | critical | pipeline_memory.md Phase 3 | [FIX] PostgreSQL version corrected: PG 17 → PG 18... |
| 2 | process_improvement | high | phase_handoff_notes.md P4→P5 | Consistency check needed: parallel subagents may use inconsistent terminology... |
```

Report the harvest count to the user: "Harvested N new insights (X critical, Y high, Z medium, W low). M duplicates skipped."

### Step 2: Consolidate

Group related pending insights into **evolution candidates**. Multiple insights about the same issue become a single candidate.

For each candidate, determine:

- **Title**: concise name (e.g., "Add PG version verification to Phase 2")
- **Related insights**: which harvest items it consolidates (by number)
- **Target file(s)**: which DNA file(s) to modify
- **Proposed change**: the specific text to add, modify, or remove — written as a concrete edit instruction
- **Confidence**: `auto` (safe mechanical change — typo fix, adding a known-good check) or `review` (judgment call — changing architecture defaults, modifying style rules, altering QA criteria)

Write candidates to `pipeline/evolution/pending_insights.md` under a `### Candidates` sub-heading:

```markdown
### Candidates

| # | Title | Insights | Target | Confidence |
|---|---|---|---|---|
| C1 | Add PG version verification to Phase 2 | 1, 7 | pipeline/prompts/phase2_research.md | auto |
| C2 | Enforce CL2-CL3 async replication terminology | 3, 4, 9 | claim_validation_rules.md, phase5_qa.md | auto |
| C3 | Soften CL0 SLA from 99.99% to 99.95% | 5 | technology_stack_decisions.md | review |
```

### Step 3: Promote

Present candidates to the user in two groups:

**Auto-apply candidates** (confidence = `auto`):
Show a numbered summary table. State: "I will apply these unless you object. Reply 'skip N' to exclude any."

**Review candidates** (confidence = `review`):
For each, show:
1. The candidate title and rationale
2. The exact proposed edit (old text → new text, or new text to insert)
3. Which file and approximate location

Wait for user confirmation before proceeding. The user may approve all, approve selectively, or reject.

If the user does not respond or says "go ahead" / "apply all" / "looks good", proceed with all approved candidates.

### Step 4: Apply

For each approved candidate:

1. **Edit the target file** using the proposed change
2. **Log the promotion** by appending to `pipeline/evolution/promotion_history.md`:

```markdown
### YYYY-MM-DD — [Candidate Title]
- **Source insights**: [list of harvest items]
- **Target**: [file path]
- **Change**: [one-line summary of what was edited]
- **Confidence**: auto|review
```

3. **Append to the ledger** (`pipeline/evolution/ledger.md`):

```markdown
- YYYY-MM-DD | [Candidate Title] | [target file] | [one-line summary]
```

4. **Clear applied items** from `pending_insights.md` (remove the harvest rows and candidate rows that were applied; leave any unapplied ones for next time)

5. **Write an evolution log entry** to `pipeline/evolution/evolution_log.md`:

```markdown
## Run N — YYYY-MM-DD

- **Pipeline run harvested from**: Phases 1-6 completed YYYY-MM-DD (or partial: Phases 1-5)
- **Insights harvested**: X total (A critical, B high, C medium, D low)
- **Duplicates skipped**: M
- **Candidates formed**: Y
- **Candidates applied**: Z (list titles)
- **Candidates deferred/skipped**: W (list titles and reason — user rejected, deferred to next run, etc.)
- **Files modified**: [list of target files that were edited]
- **User decisions**: [any notable approvals, rejections, or modifications the user requested]
```

After all edits, report to the user:
- How many candidates were applied
- Which files were modified
- Any candidates that were skipped or deferred

## Rules

- NEVER modify source documents, generated content, requirements outputs, or research evidence
- NEVER apply a `review`-confidence candidate without user approval
- NEVER duplicate a promotion that already exists in `promotion_history.md`
- If `pipeline/evolution/` directory or its files don't exist, create them with the seed templates before starting
- Keep ledger entries to one line each — the ledger is a quick-scan changelog, not a narrative
- When editing phase prompts, add new instructions in the appropriate section (don't dump everything at the top)
- When adding to claim_validation_rules.md, follow the existing format (rule name + explanation + examples)
- When adding to response_style_guide.md, follow the existing section structure
