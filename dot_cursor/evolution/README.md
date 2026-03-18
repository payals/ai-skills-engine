# Self-Evolution System

A self-improving workflow that learns from napkin entries and tracker history to evolve rules, skills, and workflows over time.

## Overview

The self-evolution system analyzes patterns in your project's napkin (mistake memory) and tracker (work history) to automatically:

1. **Detect patterns** - Repeated mistakes, successful approaches, workflow patterns
2. **Generate proposals** - New rules, skill enhancements, workflow optimizations
3. **Implement changes** - With your approval, backed up files, and effectiveness tracking
4. **Monitor effectiveness** - Track whether changes actually improve the system

## Status

**DISABLED BY DEFAULT** - This is an opt-in system that requires explicit activation.

## Quick Start

### Enable the System

```bash
cd /path/to/your/project
./.cursor/evolution/scripts/enable.sh
```

This will:
- Set `enabled: true` in config.json
- Set `alwaysApply: true` in self-evolution.mdc rule
- Create necessary directories
- Start passive pattern analysis

### Disable the System

```bash
./.cursor/evolution/scripts/disable.sh
```

### Run Manual Analysis

```bash
./.cursor/evolution/scripts/analyze.py /path/to/project
```

### Generate Report

```bash
# Full report
./.cursor/evolution/scripts/report.py /path/to/project

# List pending proposals
./.cursor/evolution/scripts/report.py /path/to/project --pending
```

## How It Works

### 1. Pattern Recognition

The system analyzes:
- **Napkin entries** (`.cursor/napkin.md`)
  - My Mistakes → Preventive rules
  - User Corrections → Enforcement rules
  - What Worked → Best practice skills
  - Repo Surprises → Documentation improvements
  - Preferences → Style/workflow rules

- **Tracker entries** (`TRACKER.md` or `docs/tracker.md`)
  - Repeated workflows → Automation scripts
  - Multi-step sequences → Coordinator patterns
  - Tool usage patterns → Skill enhancements

### 2. Proposal Generation

When patterns meet thresholds (default: 3+ occurrences), the system generates proposals:

**Proposal Types:**
- **New Rules** - Prevent repeated mistakes
- **Rule Modifications** - Strengthen or clarify existing rules
- **New Skills** - Codify successful approaches
- **Skill Modifications** - Enhance existing skills
- **Workflow Optimizations** - Automate repeated sequences

**Scoring System:**
- **Value Score** (0-10): Improvement impact
- **Risk Score** (0-10): Potential for problems
- **Effort Score** (0-10): Implementation complexity
- **Confidence Score** (0-10): Solution certainty

Only proposals with Value ≥6, Risk ≤4, Confidence ≥7 are presented.

### 3. User Review

Each proposal includes:
- Pattern that triggered it
- Evidence from napkin/tracker
- Impact analysis with scores
- Implementation preview
- Recommendation (IMPLEMENT/DEFER/REJECT)

You choose:
- **Accept** - Implement immediately
- **Accept with modifications** - Provide feedback
- **Defer** - Save to backlog
- **Reject** - Discard with reason

### 4. Implementation

On acceptance:
1. Backup files to `.cursor/evolution/backups/[timestamp]/`
2. Implement changes
3. Run verification (lints, tests)
4. Update evolution log
5. Add entry to napkin

### 5. Effectiveness Tracking

After implementation, the system monitors for 7 days (configurable):

**Success Metrics:**
- Did mistakes stop appearing?
- Did workflows become more efficient?
- Was the skill/rule actually used?

**Outcomes:**
- **Success** - Keep change, log success
- **Partial** - Propose refinement
- **Failure** - Propose rollback

## Configuration

Edit `.cursor/evolution/config.json`:

```json
{
  "enabled": false,                    // Master switch
  "mode": "passive",                   // "passive" or "active"
  "min_pattern_frequency": 3,          // Min occurrences to trigger proposal
  "min_value_score": 6,                // Min value score to present
  "max_risk_score": 4,                 // Max risk score to present
  "min_confidence_score": 7,           // Min confidence to present
  "monitoring_period_days": 7,         // How long to track effectiveness
  "auto_implement": false,             // Auto-implement without approval
  "require_user_approval": true,       // Require approval for changes
  "pattern_lookback_days": 30,         // How far back to analyze
  "backup_before_changes": true        // Backup files before modifying
}
```

## Directory Structure

```
.cursor/evolution/
├── config.json              # Configuration
├── LOG.md                   # Master log of all events
├── README.md                # This file
├── proposals/               # Generated proposals
│   └── YYYY-MM-DD-HH-MM.md
├── backups/                 # Pre-change backups
│   └── YYYY-MM-DD-HH-MM/
├── tracking/                # Effectiveness tracking
│   └── YYYY-MM-DD-change-id.md
├── reports/                 # Analysis reports
│   ├── analysis-*.md
│   └── summary-*.md
├── hooks/                   # Git hook examples
│   └── post-commit.sample
└── scripts/                 # Automation scripts
    ├── analyze.py           # Pattern analysis
    ├── enable.sh            # Enable system
    ├── disable.sh           # Disable system
    └── report.py            # Generate reports
```

## Git Hooks (Optional)

To trigger analysis automatically after commits:

```bash
# Copy the sample hook
cp .cursor/evolution/hooks/post-commit.sample .git/hooks/post-commit

# Make it executable
chmod +x .git/hooks/post-commit
```

The hook will run analysis after commits that modify napkin.md or TRACKER.md.

## Usage Patterns

### Passive Mode (Recommended)

Enable the system and let it work in the background:
- Analyzes patterns after substantial work
- Generates proposals when thresholds met
- Notifies you when proposals ready
- You review and approve/reject

### Active Mode

Manually trigger analysis when needed:
```bash
# In Cursor, say:
"Run evolution analysis"
"What patterns do you see?"
"Suggest improvements"
```

### One-Time Analysis

Run analysis without enabling ongoing monitoring:
```bash
./.cursor/evolution/scripts/analyze.py /path/to/project
```

## Safety Features

1. **Disabled by default** - Explicit opt-in required
2. **User approval required** - No auto-implementation without permission
3. **Automatic backups** - Files backed up before modification
4. **Effectiveness tracking** - Changes monitored for success
5. **Rollback mechanism** - Easy restoration from backups
6. **Conflict detection** - Prevents rule conflicts
7. **Impact simulation** - Risk analysis before proposals

## Example Evolution Cycle

**Week 1:**
- System detects 3 napkin entries about PostgreSQL version mistakes
- Generates proposal: "Add PostgreSQL version verification rule"
- You review and accept
- Rule implemented with backup

**Week 2:**
- Tracker shows rule prevented 2 potential mistakes
- Effectiveness tracking: SUCCESS
- Rule validated and kept

**Week 3:**
- System detects 4 "What Worked" entries about parallel subagent dispatch
- Generates proposal: "Enhance coordinator skill with parallel patterns"
- You accept with modifications
- Skill updated

**Week 4:**
- Tracker shows 3 tasks used new pattern successfully
- Effectiveness tracking: SUCCESS
- Enhancement validated

## Troubleshooting

### System not generating proposals

**Check:**
1. Is system enabled? (`cat .cursor/evolution/config.json | grep enabled`)
2. Are there enough patterns? (Need 3+ occurrences by default)
3. Is napkin/tracker being updated? (Check file modification times)
4. Run manual analysis to see what patterns exist

### Proposals have low scores

**Reasons:**
- Pattern frequency too low (increase `min_pattern_frequency`)
- Risk too high (review impact analysis)
- Confidence too low (insufficient evidence)

**Solutions:**
- Gather more data (more napkin/tracker entries)
- Adjust scoring thresholds in config
- Manually review patterns with `analyze.py`

### Changes not being tracked

**Check:**
1. Is tracking file created? (`.cursor/evolution/tracking/`)
2. Has monitoring period passed? (Default 7 days)
3. Are there tracker entries showing usage?

### Want to rollback a change

```bash
# Find the backup
ls .cursor/evolution/backups/

# Restore from backup
cp -r .cursor/evolution/backups/YYYY-MM-DD-HH-MM/* /path/to/original/location/

# Update evolution log
# (Document the rollback and reason)
```

## Best Practices

1. **Start with passive mode** - Let the system learn your patterns
2. **Review proposals carefully** - Don't auto-accept everything
3. **Track effectiveness** - Wait for monitoring period to complete
4. **Adjust thresholds** - Tune config based on your project size
5. **Keep napkin updated** - More data = better proposals
6. **Document decisions** - Add notes when accepting/rejecting proposals
7. **Regular reviews** - Run reports weekly to see trends

## Integration with Existing Systems

### With Napkin
- Napkin is **input** (source of patterns)
- Evolution results logged **to** napkin
- Never modifies napkin structure

### With Tracker
- Tracker is **input** (workflow patterns)
- Evolution milestones logged **to** tracker
- Never modifies tracker structure

### With Rules
- Can propose new rules or modifications
- Masterrule changes require confidence ≥9
- Always checks for conflicts

### With Skills
- Can propose new skills or enhancements
- Updates INDEX.md when adding skills
- Tracks skill usage via tracker

## FAQ

**Q: Will this modify my code automatically?**
A: No, unless you set `auto_implement: true` in config. By default, all changes require your approval.

**Q: What if a change breaks something?**
A: All files are backed up before modification. You can restore from `.cursor/evolution/backups/`.

**Q: How much overhead does this add?**
A: Minimal. Analysis runs in background after substantial work. Typical analysis takes 1-2 seconds.

**Q: Can I use this with multiple projects?**
A: Yes, each project has its own `.cursor/evolution/` directory with independent configuration.

**Q: What if I disagree with a proposal?**
A: Reject it with a reason. The system learns from rejections and won't propose similar changes.

**Q: Can I customize the scoring thresholds?**
A: Yes, edit `config.json` to adjust min/max scores for value, risk, confidence, and effort.

**Q: Does this work with the coordinator mode?**
A: Yes, it can propose coordinator pattern improvements based on subagent success/failure patterns.

## Contributing

Found a bug or have a feature request? Please open an issue in the main repository.

## License

Same as parent project (Apache 2.0).
