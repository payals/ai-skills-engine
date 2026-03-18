# Self-Evolution System Documentation

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Pattern Detection](#pattern-detection)
- [Proposal Generation](#proposal-generation)
- [Safety & Rollback](#safety--rollback)
- [Integration](#integration)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Best Practices](#best-practices)

---

## Overview

The Self-Evolution System is an automated workflow that learns from your project's napkin (mistake memory) and tracker (work history) to continuously improve the AI Skills Engine itself.

### Key Features

- **Pattern Recognition**: Automatically detects repeated mistakes, successful approaches, and workflow patterns
- **Smart Proposals**: Generates improvement proposals with impact analysis and scoring
- **Safe Implementation**: Backs up files, requires approval, and tracks effectiveness
- **Self-Monitoring**: Measures whether changes actually improve the system
- **Rollback Support**: Easy restoration if changes don't work out

### Status

**DISABLED BY DEFAULT** - This is an opt-in system that requires explicit activation.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Self-Evolution System                     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────────┐
        │         Pattern Recognition             │
        │  (Analyzes napkin.md + TRACKER.md)      │
        └─────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────────┐
        │       Proposal Generation               │
        │  (Creates improvement proposals)        │
        └─────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────────┐
        │         Impact Simulation               │
        │  (Scores: Value, Risk, Confidence)      │
        └─────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────────┐
        │          User Review                    │
        │  (Accept/Modify/Defer/Reject)           │
        └─────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────────┐
        │         Implementation                  │
        │  (Backup → Change → Verify)             │
        └─────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────────┐
        │      Effectiveness Tracking             │
        │  (Monitor for 7 days, measure impact)   │
        └─────────────────────────────────────────┘
```

### Components

1. **Rule**: `.cursor/rules/self-evolution.mdc` - Defines when and how evolution runs
2. **Scripts**: 
   - `analyze.py` - Pattern detection and analysis
   - `enable.sh` / `disable.sh` - System activation
   - `report.py` - Reporting and status
3. **Configuration**: `config.json` - System settings and thresholds
4. **Storage**:
   - `proposals/` - Generated improvement proposals
   - `backups/` - Pre-change file backups
   - `tracking/` - Effectiveness monitoring data
   - `reports/` - Analysis reports

---

## How It Works

### Phase 1: Pattern Recognition

**Inputs:**
- `.cursor/napkin.md` - Mistake memory
- `TRACKER.md` - Work history
- `.cursor/rules/*.mdc` - Current rules
- `.cursor/skills/INDEX.md` - Skill catalog

**Analysis:**
1. **Frequency Analysis**: Which mistakes repeat? Which approaches consistently work?
2. **Temporal Patterns**: Are recent entries showing new patterns?
3. **Category Clustering**: Do mistakes cluster around specific domains?
4. **Gap Detection**: What problems have no corresponding skills/rules?
5. **Rule Violations**: Are rules being ignored or misunderstood?

**Output**: Pattern report with top repeated mistakes, successful approaches, missing skills, and underperforming rules.

### Phase 2: Proposal Generation

**Triggers:**
- **New Rules**: 3+ napkin entries show same mistake
- **Rule Modifications**: Existing rule violated 2+ times
- **New Skills**: 3+ "What Worked" entries in same domain
- **Skill Modifications**: Skill exists but mistakes still happen
- **Workflow Optimizations**: Tracker shows repeated multi-step sequences

**Scoring System:**
- **Value Score** (0-10): How much does this improve the system?
- **Risk Score** (0-10): How likely is this to cause problems?
- **Effort Score** (0-10): How much work to implement?
- **Confidence Score** (0-10): How certain are we this is correct?

**Thresholds** (configurable):
- Value ≥ 6
- Risk ≤ 4
- Confidence ≥ 7

### Phase 3: User Review

Each proposal includes:
- Pattern that triggered it
- Evidence from napkin/tracker
- Impact analysis with scores
- Implementation preview
- Recommendation (IMPLEMENT/DEFER/REJECT)

**User Options:**
1. **Accept** - Implement immediately
2. **Accept with modifications** - Provide feedback
3. **Defer** - Save to backlog
4. **Reject** - Discard with reason

### Phase 4: Implementation

On acceptance:
1. **Backup**: Create `.cursor/evolution/backups/[timestamp]/`
2. **Implement**: Make the proposed changes
3. **Verify**: Run lints, tests, etc.
4. **Document**: Update evolution log
5. **Notify**: Add entry to napkin

### Phase 5: Effectiveness Tracking

**Monitoring Period**: 7 days (configurable)

**Success Metrics:**
- **For preventive rules**: Did the mistake stop appearing?
- **For automation rules**: Did tracker show time savings?
- **For new skills**: Was the skill used?
- **For workflow optimizations**: Did workflow become more efficient?

**Outcomes:**
- **Success** (metrics met) → Keep change
- **Partial** (some metrics met) → Propose refinement
- **Failure** (metrics not met) → Propose rollback

---

## Installation

### Prerequisites

- Python 3.7+
- Bash shell (for scripts)
- Git (for hooks, optional)

### Setup

1. **System is already included** in AI Skills Engine
2. **Enable the system**:
   ```bash
   ./.cursor/evolution/scripts/enable.sh
   ```

3. **Configure** (optional):
   ```bash
   # Edit configuration
   nano .cursor/evolution/config.json
   ```

4. **Setup Git hooks** (optional):
   ```bash
   cp .cursor/evolution/hooks/post-commit.sample .git/hooks/post-commit
   chmod +x .git/hooks/post-commit
   ```

---

## Configuration

Edit `.cursor/evolution/config.json`:

```json
{
  "enabled": false,
  "mode": "passive",
  "analysis_frequency": "after_substantial_work",
  "min_pattern_frequency": 3,
  "min_value_score": 6,
  "max_risk_score": 4,
  "min_confidence_score": 7,
  "monitoring_period_days": 7,
  "auto_implement": false,
  "backup_before_changes": true,
  "require_user_approval": true,
  "pattern_lookback_days": 30,
  "analysis_triggers": {
    "tracker_min_lines": 10,
    "napkin_min_mistakes": 2,
    "napkin_min_corrections": 1,
    "napkin_min_what_worked": 2,
    "days_between_reviews": 7
  },
  "scoring_thresholds": {
    "value_min": 6,
    "risk_max": 4,
    "confidence_min": 7,
    "masterrule_confidence_min": 9
  }
}
```

### Configuration Options

| Option | Default | Description |
|--------|---------|-------------|
| `enabled` | `false` | Master switch for the system |
| `mode` | `"passive"` | `"passive"` (background) or `"active"` (manual) |
| `min_pattern_frequency` | `3` | Min occurrences to trigger proposal |
| `min_value_score` | `6` | Min value score to present proposal |
| `max_risk_score` | `4` | Max risk score to present proposal |
| `min_confidence_score` | `7` | Min confidence to present proposal |
| `monitoring_period_days` | `7` | Days to track effectiveness |
| `auto_implement` | `false` | Auto-implement without approval |
| `require_user_approval` | `true` | Require approval for changes |
| `pattern_lookback_days` | `30` | How far back to analyze |
| `backup_before_changes` | `true` | Backup files before modifying |

---

## Usage

### Enable/Disable

```bash
# Enable
./.cursor/evolution/scripts/enable.sh

# Disable
./.cursor/evolution/scripts/disable.sh
```

### Manual Analysis

```bash
# Run pattern analysis
./.cursor/evolution/scripts/analyze.py /path/to/project

# View latest report
cat .cursor/evolution/reports/analysis-*.md | tail -100
```

### Generate Reports

```bash
# Full system report
./.cursor/evolution/scripts/report.py /path/to/project

# List pending proposals
./.cursor/evolution/scripts/report.py /path/to/project --pending
```

### In Cursor IDE

```
# Trigger evolution analysis
"Run evolution analysis"
"What patterns do you see?"
"Suggest improvements"
"Evolve the system"

# Check status
"Show evolution status"
"List pending proposals"
"Show evolution report"
```

---

## Pattern Detection

### Napkin Analysis

**My Mistakes** → Preventive Rules
```
Pattern: "PostgreSQL version" appears 3 times
Proposal: Add rule to verify PostgreSQL version before generating docs
```

**User Corrections** → Enforcement Rules
```
Pattern: User corrects "always verify X" 2 times
Proposal: Add verification step to existing workflow rule
```

**What Worked** → Best Practice Skills
```
Pattern: "parallel subagents" appears 4 times
Proposal: Create skill documenting parallel dispatch patterns
```

**Repo Surprises** → Documentation
```
Pattern: "unexpected behavior in X" appears 3 times
Proposal: Add documentation explaining X's behavior
```

**Preferences** → Style Rules
```
Pattern: User prefers "concise output" mentioned 2 times
Proposal: Add rule to keep responses concise
```

### Tracker Analysis

**Repeated Workflows** → Automation Scripts
```
Pattern: 5-step workflow appears 3 times in tracker
Proposal: Create script to automate this workflow
```

**Multi-Step Sequences** → Coordinator Patterns
```
Pattern: Subagent coordination pattern used 4 times
Proposal: Add pattern to coordinator rule
```

**Tool Usage** → Skill Enhancements
```
Pattern: Tool X used successfully 5 times
Proposal: Enhance skill with Tool X best practices
```

---

## Proposal Generation

### Proposal Structure

```markdown
# Self-Evolution Proposal: [Title]

## Pattern Detected
[What pattern triggered this]

## Proposed Change
Type: [New Rule | Rule Mod | New Skill | Skill Mod | Workflow Opt]
Target: [File to modify]
Description: [What will change]

## Evidence
- Napkin: [3+ entries]
- Tracker: [2+ entries]
- Frequency: [X times over Y days]

## Impact Analysis
- Value: 8/10 - [Why valuable]
- Risk: 2/10 - [What could go wrong]
- Effort: 4/10 - [Implementation complexity]
- Confidence: 9/10 - [How certain]

## Implementation Preview
[Show exact changes]

## Recommendation
IMPLEMENT - [Reasoning]
```

### Scoring Guidelines

**Value Score:**
- 9-10: Critical improvement, major impact
- 7-8: Significant improvement
- 5-6: Moderate improvement
- 3-4: Minor improvement
- 1-2: Negligible improvement

**Risk Score:**
- 9-10: High risk of breaking things
- 7-8: Moderate risk
- 5-6: Some risk
- 3-4: Low risk
- 1-2: Minimal risk

**Confidence Score:**
- 9-10: Very confident, strong evidence
- 7-8: Confident, good evidence
- 5-6: Somewhat confident
- 3-4: Low confidence
- 1-2: Very uncertain

---

## Safety & Rollback

### Backup System

Before any change:
```
.cursor/evolution/backups/YYYY-MM-DD-HH-MM/
├── rules/
│   └── modified-rule.mdc
└── skills/
    └── modified-skill/
        └── SKILL.md
```

### Rollback Procedure

```bash
# 1. Find backup
ls .cursor/evolution/backups/

# 2. Restore files
cp -r .cursor/evolution/backups/2026-03-18-14-30/* .

# 3. Update evolution log
# Document rollback and reason

# 4. Update napkin
# Add entry: "2026-03-18 Rolled back [change]: [reason]"
```

### Safety Guardrails

1. **Never auto-implement without approval** (unless configured)
2. **Always backup before changes**
3. **Never modify napkin.md or TRACKER.md** (source data)
4. **Never propose conflicting changes**
5. **Always show impact analysis**
6. **Track effectiveness of all changes**
7. **Provide rollback mechanism**

---

## Integration

### With Napkin

- **Input**: Napkin is source of patterns
- **Output**: Evolution results logged to napkin
- **Safety**: Never modifies napkin structure or history

### With Tracker

- **Input**: Tracker is source of workflow patterns
- **Output**: Evolution milestones logged to tracker
- **Safety**: Never modifies tracker structure or history

### With Rules

- **Can propose**: New rules or modifications
- **Special handling**: Masterrule changes require confidence ≥9
- **Safety**: Always checks for conflicts

### With Skills

- **Can propose**: New skills or enhancements
- **Integration**: Updates INDEX.md when adding skills
- **Tracking**: Monitors skill usage via tracker

### With Coordinator Mode

- **Can propose**: Coordinator pattern improvements
- **Based on**: Subagent success/failure patterns
- **Tracking**: Coordinator effectiveness via tracker

---

## Examples

### Example 1: Preventive Rule from Repeated Mistake

**Napkin Entries:**
```
- 2026-03-15 Used PostgreSQL 17 as latest; user corrected it's PG 18
- 2026-03-18 Assumed latest PG was 17; actually 18 (released Sept 2025)
- 2026-03-20 Generated docs with PG 17; should have been PG 18
```

**Proposal Generated:**
```markdown
# Self-Evolution Proposal: Add PostgreSQL Version Verification Rule

## Pattern Detected
PostgreSQL version mistakes repeated 3 times in 5 days

## Proposed Change
Type: New Rule
Target: .cursor/rules/database-version-check.mdc

Add rule to verify PostgreSQL version against current date before
generating any database-related documentation or architecture.

## Impact Analysis
- Value: 8/10 - Prevents documentation errors
- Risk: 2/10 - Low risk, just adds verification step
- Effort: 3/10 - Simple rule addition
- Confidence: 9/10 - Clear pattern, proven solution

## Recommendation
IMPLEMENT
```

**User Accepts** → Rule created → Tracked for 7 days → Success (no more PG version mistakes)

### Example 2: Skill Enhancement from "What Worked"

**Napkin Entries:**
```
- 2026-03-18 Parallel subagent dispatch for 3 sections worked great
- 2026-03-19 Pre-reading files via explore subagent before dispatch was efficient
- 2026-03-20 Batching 20 rows per subagent prevented context issues
- 2026-03-21 Shell subagent_type failed; coordinator handled directly instead
```

**Proposal Generated:**
```markdown
# Self-Evolution Proposal: Enhance Coordinator Skill with Parallel Patterns

## Pattern Detected
Successful parallel subagent patterns repeated 4 times

## Proposed Change
Type: Skill Modification
Target: .cursor/skills/ai-research/coordinator-mode/SKILL.md

Add section documenting:
- Optimal batch sizes (20 items)
- Pre-reading strategy via explore subagents
- When to use coordinator vs shell subagent

## Impact Analysis
- Value: 7/10 - Codifies successful patterns
- Risk: 1/10 - Just documentation
- Effort: 2/10 - Add section to existing skill
- Confidence: 8/10 - Multiple successful uses

## Recommendation
IMPLEMENT
```

**User Accepts** → Skill enhanced → Tracked for 7 days → Success (pattern used 3 more times)

### Example 3: Workflow Automation from Tracker

**Tracker Entries:**
```
## [2026-03-15] - Phase 4 Row Responses
Steps:
1. Read all solution drafts
2. Dispatch 3 parallel subagents
3. Wait for completion
4. Verify outputs
5. Compile results

## [2026-03-18] - Phase 5 Supplemental Docs
Steps:
1. Read requirements
2. Dispatch 2 parallel subagents
3. Wait for completion
4. Verify outputs
5. Compile results

## [2026-03-20] - Phase 6 PDF Generation
Steps:
1. Read markdown files
2. Convert to PDFs
3. Verify outputs
4. Compile results
```

**Proposal Generated:**
```markdown
# Self-Evolution Proposal: Create Phase Execution Script

## Pattern Detected
5-step execution pattern repeated 3 times across phases

## Proposed Change
Type: Workflow Optimization
Target: .cursor/evolution/scripts/execute-phase.sh

Create script to automate:
- Input reading
- Subagent dispatch
- Completion waiting
- Output verification
- Result compilation

## Impact Analysis
- Value: 6/10 - Saves time on repeated workflows
- Risk: 3/10 - Script could fail, need fallback
- Effort: 5/10 - Moderate script development
- Confidence: 7/10 - Pattern is clear

## Recommendation
IMPLEMENT with testing
```

---

## Troubleshooting

### Issue: No proposals generated

**Possible Causes:**
1. Not enough patterns (need 3+ occurrences)
2. Pattern frequency too low
3. Napkin/tracker not being updated
4. Lookback period too short

**Solutions:**
```bash
# Check current patterns
./.cursor/evolution/scripts/analyze.py /path/to/project

# Adjust thresholds
# Edit config.json: "min_pattern_frequency": 2

# Increase lookback period
# Edit config.json: "pattern_lookback_days": 60
```

### Issue: Proposals have low scores

**Possible Causes:**
1. Pattern evidence is weak
2. Risk is too high
3. Confidence is low

**Solutions:**
- Gather more evidence (more napkin/tracker entries)
- Adjust scoring thresholds in config
- Review proposals manually to understand scoring

### Issue: Changes not being tracked

**Possible Causes:**
1. Tracking file not created
2. Monitoring period hasn't passed
3. No tracker entries showing usage

**Solutions:**
```bash
# Check tracking files
ls .cursor/evolution/tracking/

# Check monitoring period
cat .cursor/evolution/config.json | grep monitoring_period_days

# Ensure tracker is being updated
ls -lt TRACKER.md
```

### Issue: Want to rollback a change

**Solution:**
```bash
# Find backup
ls .cursor/evolution/backups/

# Restore
cp -r .cursor/evolution/backups/2026-03-18-14-30/* .

# Update logs
# Add rollback entry to evolution LOG.md and napkin.md
```

---

## Best Practices

### 1. Start with Passive Mode

Enable the system and let it learn your patterns before making changes.

### 2. Review Proposals Carefully

Don't auto-accept everything. Consider:
- Is the pattern real or coincidence?
- Is the proposed solution appropriate?
- Are there better alternatives?

### 3. Track Effectiveness

Wait for the full monitoring period before deciding on success/failure.

### 4. Adjust Thresholds

Tune configuration based on your project:
- Large projects: Higher frequency thresholds
- Small projects: Lower frequency thresholds

### 5. Keep Napkin Updated

More data = better proposals. Document:
- Mistakes when they happen
- What worked well
- User corrections
- Surprises

### 6. Document Decisions

When accepting/rejecting proposals, add notes explaining why.

### 7. Regular Reviews

Run reports weekly to see trends:
```bash
./.cursor/evolution/scripts/report.py /path/to/project
```

### 8. Use Git Hooks

Automate analysis after commits:
```bash
cp .cursor/evolution/hooks/post-commit.sample .git/hooks/post-commit
chmod +x .git/hooks/post-commit
```

### 9. Backup Before Enabling

Before enabling for the first time:
```bash
git commit -am "Before enabling self-evolution"
```

### 10. Monitor Resource Usage

If analysis is slow:
- Reduce `pattern_lookback_days`
- Increase `min_pattern_frequency`
- Run analysis less frequently

---

## FAQ

**Q: Will this modify my code automatically?**
A: No, unless you set `auto_implement: true`. By default, all changes require approval.

**Q: What if a change breaks something?**
A: All files are backed up. Restore from `.cursor/evolution/backups/`.

**Q: How much overhead does this add?**
A: Minimal. Analysis runs in background and takes 1-2 seconds typically.

**Q: Can I use this with multiple projects?**
A: Yes, each project has independent configuration.

**Q: What if I disagree with a proposal?**
A: Reject it with a reason. The system learns from rejections.

**Q: Can I customize scoring thresholds?**
A: Yes, edit `config.json` to adjust all thresholds.

**Q: Does this work with coordinator mode?**
A: Yes, it can propose coordinator improvements.

**Q: How do I know if it's working?**
A: Run `./cursor/evolution/scripts/report.py` to see status and statistics.

---

## Contributing

Found a bug or have a feature request? Please open an issue in the main repository.

## License

Same as parent project (Apache 2.0).
