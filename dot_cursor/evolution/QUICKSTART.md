# Self-Evolution System - Quick Start

Get the self-evolution system up and running in 5 minutes.

## What is This?

A self-improving workflow that learns from your project's napkin (mistake memory) and tracker (work history) to automatically improve rules, skills, and workflows.

## Quick Start

### 1. Enable the System (30 seconds)

```bash
cd /path/to/your/project
./.cursor/evolution/scripts/enable.sh
```

This will:
- Set `enabled: true` in config
- Activate the evolution rule
- Create necessary directories

### 2. Verify It's Working (10 seconds)

```bash
# Check status
cat .cursor/evolution/config.json | grep enabled
# Should show: "enabled": true

# Check rule is active
grep "alwaysApply:" .cursor/rules/self-evolution.mdc
# Should show: alwaysApply: true
```

### 3. Let It Learn (Passive Mode)

The system will now automatically:
- Analyze napkin.md and TRACKER.md after substantial work
- Detect patterns (repeated mistakes, successful approaches)
- Generate proposals when patterns meet thresholds (3+ occurrences)
- Notify you when proposals are ready

**No action needed** - just keep using napkin and tracker as normal.

### 4. Review Your First Proposal (When Ready)

After a few days of work, check for proposals:

```bash
# List pending proposals
./.cursor/evolution/scripts/report.py /path/to/project --pending
```

Or in Cursor, say:
```
"Show pending evolution proposals"
"Run evolution analysis"
```

### 5. Accept/Reject Proposals

When you see a proposal:

**Option 1: Accept**
- System backs up files
- Implements changes
- Starts effectiveness tracking (7 days)

**Option 2: Reject**
- Provide reason
- System learns from rejection

**Option 3: Defer**
- Save to backlog for later review

## What Happens Next?

### Week 1: Learning Phase
- System collects patterns
- No proposals yet (need 3+ occurrences)
- Keep updating napkin and tracker

### Week 2: First Proposals
- System detects patterns
- Generates 1-3 proposals
- You review and accept/reject

### Week 3: Effectiveness Tracking
- Accepted changes are monitored
- System measures impact
- Success/failure determined

### Week 4: Continuous Improvement
- Successful changes kept
- Failed changes rolled back
- New patterns detected
- Cycle continues

## Configuration (Optional)

Edit `.cursor/evolution/config.json` to customize:

```json
{
  "min_pattern_frequency": 3,    // Lower = more proposals
  "min_value_score": 6,           // Lower = more proposals
  "monitoring_period_days": 7,    // How long to track
  "auto_implement": false         // Require approval
}
```

## Common Commands

```bash
# Enable/Disable
./.cursor/evolution/scripts/enable.sh
./.cursor/evolution/scripts/disable.sh

# Run analysis manually
./.cursor/evolution/scripts/analyze.py /path/to/project

# Generate report
./.cursor/evolution/scripts/report.py /path/to/project

# List pending proposals
./.cursor/evolution/scripts/report.py /path/to/project --pending

# View latest analysis
cat .cursor/evolution/reports/analysis-*.md | tail -100
```

## In Cursor IDE

```
# Trigger analysis
"Run evolution analysis"
"What patterns do you see?"
"Suggest improvements"

# Check status
"Show evolution status"
"List pending proposals"

# Review proposals
"Show proposal [filename]"
"Accept proposal [filename]"
"Reject proposal [filename]"
```

## Safety Features

1. **Disabled by default** - Explicit opt-in required
2. **User approval required** - No auto-implementation
3. **Automatic backups** - Files backed up before changes
4. **Effectiveness tracking** - Changes monitored for success
5. **Easy rollback** - Restore from backups if needed

## Troubleshooting

### No proposals generated?

**Check:**
1. Is system enabled? `cat .cursor/evolution/config.json | grep enabled`
2. Are there enough patterns? Run `analyze.py` to see
3. Is napkin/tracker being updated? Check file modification times

**Solution:**
- Lower `min_pattern_frequency` to 2 in config
- Increase `pattern_lookback_days` to 60
- Ensure napkin and tracker are actively used

### Proposals have low scores?

**Reason:** Not enough evidence yet

**Solution:**
- Gather more data (more napkin/tracker entries)
- Review patterns with `analyze.py`
- Wait a few more days for patterns to strengthen

### Want to disable temporarily?

```bash
./.cursor/evolution/scripts/disable.sh
```

All data is preserved. Re-enable anytime with `enable.sh`.

## Next Steps

1. **Read full documentation**: `docs/SELF_EVOLUTION.md`
2. **Setup Git hooks** (optional): `cp .cursor/evolution/hooks/post-commit.sample .git/hooks/post-commit`
3. **Customize configuration**: Edit `config.json` for your project
4. **Review weekly**: Run `report.py` to see trends

## Example Evolution Cycle

**Day 1-7**: System learns your patterns
- 3 napkin entries about PostgreSQL version mistakes
- 4 tracker entries showing parallel subagent success

**Day 8**: First proposals generated
- Proposal 1: Add PostgreSQL version verification rule
- Proposal 2: Enhance coordinator skill with parallel patterns

**Day 9**: You review and accept both

**Day 10-16**: Effectiveness tracking
- Rule prevents 2 version mistakes
- Skill used in 3 new tasks

**Day 17**: Success confirmed
- Both changes validated
- System continues learning

## Questions?

- **Full docs**: `docs/SELF_EVOLUTION.md`
- **System README**: `.cursor/evolution/README.md`
- **Configuration**: `.cursor/evolution/config.json`
- **Templates**: `.cursor/evolution/proposals/TEMPLATE.md`

## Disable Anytime

```bash
./.cursor/evolution/scripts/disable.sh
```

No data is lost. Re-enable whenever you want.

---

**Ready to evolve? Run `enable.sh` and let the system learn!**
