# Self-Evolution Workflow Diagram

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     Self-Evolution System                        │
│                    (Disabled by Default)                         │
└─────────────────────────────────────────────────────────────────┘
                                │
                                │ User enables via enable.sh
                                ▼
                    ┌───────────────────────┐
                    │   System Activated    │
                    │   alwaysApply: true   │
                    └───────────────────────┘
                                │
                                ▼
        ┌───────────────────────────────────────────────┐
        │         Continuous Monitoring                 │
        │  (After tracker/napkin updates)               │
        └───────────────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────────┐
│                      PHASE 1: Pattern Recognition                 │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Input Sources:                                                   │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │ napkin.md   │  │ TRACKER.md  │  │ rules/*.mdc │             │
│  │             │  │             │  │             │             │
│  │ • Mistakes  │  │ • Workflows │  │ • Current   │             │
│  │ • What      │  │ • Patterns  │  │   rules     │             │
│  │   Worked    │  │ • Tool use  │  │             │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│         │                 │                 │                     │
│         └─────────────────┴─────────────────┘                     │
│                           │                                       │
│                           ▼                                       │
│              ┌─────────────────────────┐                         │
│              │   analyze.py            │                         │
│              │   • Frequency analysis  │                         │
│              │   • Temporal patterns   │                         │
│              │   • Category clustering │                         │
│              │   • Gap detection       │                         │
│              └─────────────────────────┘                         │
│                           │                                       │
│                           ▼                                       │
│              ┌─────────────────────────┐                         │
│              │   Pattern Report        │                         │
│              │   • Top 5 mistakes      │                         │
│              │   • Top 5 successes     │                         │
│              │   • Top 3 gaps          │                         │
│              │   • Rule violations     │                         │
│              └─────────────────────────┘                         │
└───────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────────┐
│                    PHASE 2: Proposal Generation                   │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Trigger Conditions:                                              │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ • 3+ repeated mistakes    → New preventive rule           │ │
│  │ • 3+ "What Worked"        → New skill or enhancement      │ │
│  │ • 2+ user corrections     → Enforcement rule              │ │
│  │ • 3+ workflow patterns    → Automation script             │ │
│  │ • 2+ rule violations      → Rule strengthening            │ │
│  └────────────────────────────────────────────────────────────┘ │
│                           │                                       │
│                           ▼                                       │
│              ┌─────────────────────────┐                         │
│              │   Proposal Generator    │                         │
│              │   • Type determination  │                         │
│              │   • Evidence collection │                         │
│              │   • Change drafting     │                         │
│              └─────────────────────────┘                         │
│                           │                                       │
│                           ▼                                       │
│              ┌─────────────────────────┐                         │
│              │   Impact Scoring        │                         │
│              │   • Value: 0-10         │                         │
│              │   • Risk: 0-10          │                         │
│              │   • Effort: 0-10        │                         │
│              │   • Confidence: 0-10    │                         │
│              └─────────────────────────┘                         │
│                           │                                       │
│                           ▼                                       │
│              ┌─────────────────────────┐                         │
│              │   Threshold Filter      │                         │
│              │   Value ≥ 6             │                         │
│              │   Risk ≤ 4              │                         │
│              │   Confidence ≥ 7        │                         │
│              └─────────────────────────┘                         │
│                           │                                       │
│                  Pass     │     Fail                              │
│                  ┌────────┴────────┐                              │
│                  ▼                 ▼                              │
│         ┌─────────────┐   ┌─────────────┐                       │
│         │  Generate   │   │   Discard   │                       │
│         │  Proposal   │   │  (Log why)  │                       │
│         └─────────────┘   └─────────────┘                       │
│                  │                                                │
│                  ▼                                                │
│         ┌─────────────────────────┐                              │
│         │  proposals/             │                              │
│         │  YYYY-MM-DD-HH-MM.md    │                              │
│         └─────────────────────────┘                              │
└───────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────────┐
│                      PHASE 3: User Review                         │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│              ┌─────────────────────────┐                         │
│              │   Notify User           │                         │
│              │   "Proposal ready"      │                         │
│              └─────────────────────────┘                         │
│                           │                                       │
│                           ▼                                       │
│              ┌─────────────────────────┐                         │
│              │   Present Proposal      │                         │
│              │   • Pattern detected    │                         │
│              │   • Evidence            │                         │
│              │   • Impact scores       │                         │
│              │   • Implementation      │                         │
│              │     preview             │                         │
│              └─────────────────────────┘                         │
│                           │                                       │
│                           ▼                                       │
│              ┌─────────────────────────┐                         │
│              │   User Decision         │                         │
│              └─────────────────────────┘                         │
│                           │                                       │
│         ┌─────────────────┼─────────────────┬──────────┐        │
│         ▼                 ▼                 ▼          ▼        │
│    ┌────────┐      ┌──────────┐      ┌────────┐  ┌────────┐   │
│    │ Accept │      │ Accept + │      │ Defer  │  │ Reject │   │
│    │        │      │   Mods   │      │        │  │        │   │
│    └────────┘      └──────────┘      └────────┘  └────────┘   │
│         │                 │                 │          │        │
│         │                 │                 │          │        │
│         ▼                 ▼                 ▼          ▼        │
│    Implement        Revise &          Save to    Log reason    │
│                     Implement         backlog                   │
└───────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────────┐
│                    PHASE 4: Implementation                        │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Step 1: Backup                                                   │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  cp files → .cursor/evolution/backups/YYYY-MM-DD-HH-MM/   │ │
│  └────────────────────────────────────────────────────────────┘ │
│                           │                                       │
│                           ▼                                       │
│  Step 2: Implement Changes                                        │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  • Create/modify rule files                               │ │
│  │  • Create/modify skill files                              │ │
│  │  • Create/modify scripts                                  │ │
│  │  • Update INDEX.md if needed                              │ │
│  └────────────────────────────────────────────────────────────┘ │
│                           │                                       │
│                           ▼                                       │
│  Step 3: Verify                                                   │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  • Run linters                                            │ │
│  │  • Run tests                                              │ │
│  │  • Check for conflicts                                    │ │
│  └────────────────────────────────────────────────────────────┘ │
│                           │                                       │
│                  Pass     │     Fail                              │
│                  ┌────────┴────────┐                              │
│                  ▼                 ▼                              │
│         ┌─────────────┐   ┌─────────────┐                       │
│         │  Continue   │   │  Rollback   │                       │
│         │             │   │  from backup│                       │
│         └─────────────┘   └─────────────┘                       │
│                  │                 │                              │
│                  ▼                 ▼                              │
│  Step 4: Document                                                 │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  • Update evolution LOG.md                                │ │
│  │  • Add entry to napkin.md                                 │ │
│  │  • Update proposal status                                 │ │
│  └────────────────────────────────────────────────────────────┘ │
│                           │                                       │
│                           ▼                                       │
│  Step 5: Start Tracking                                           │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  Create tracking/YYYY-MM-DD-change-id.md                  │ │
│  │  • Success metrics defined                                │ │
│  │  • Monitoring period: 7 days                              │ │
│  └────────────────────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────────┐
│                 PHASE 5: Effectiveness Tracking                   │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Monitoring Period: 7 days (configurable)                         │
│                                                                   │
│  Day 1-7: Collect Evidence                                        │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  • Monitor napkin.md for mistake recurrence              │ │
│  │  • Monitor TRACKER.md for usage patterns                 │ │
│  │  • Track user feedback                                   │ │
│  │  • Measure against success metrics                       │ │
│  └────────────────────────────────────────────────────────────┘ │
│                           │                                       │
│                           ▼                                       │
│  Day 7: Evaluate                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  Primary metric:   [Met / Not Met]                        │ │
│  │  Secondary metric: [Met / Not Met]                        │ │
│  │  Tertiary metric:  [Met / Not Met]                        │ │
│  └────────────────────────────────────────────────────────────┘ │
│                           │                                       │
│         ┌─────────────────┼─────────────────┐                    │
│         ▼                 ▼                 ▼                    │
│    ┌────────┐      ┌──────────┐      ┌────────┐                │
│    │SUCCESS │      │ PARTIAL  │      │ FAILED │                │
│    │ All    │      │ Some     │      │ None   │                │
│    │ metrics│      │ metrics  │      │ met    │                │
│    │ met    │      │ met      │      │        │                │
│    └────────┘      └──────────┘      └────────┘                │
│         │                 │                 │                    │
│         ▼                 ▼                 ▼                    │
│    ┌────────┐      ┌──────────┐      ┌────────┐                │
│    │  KEEP  │      │  REFINE  │      │ROLLBACK│                │
│    │ Change │      │  Adjust  │      │ Restore│                │
│    │validated│     │  & retry │      │ backup │                │
│    └────────┘      └──────────┘      └────────┘                │
│         │                 │                 │                    │
│         └─────────────────┴─────────────────┘                    │
│                           │                                       │
│                           ▼                                       │
│              ┌─────────────────────────┐                         │
│              │   Update Tracking File  │                         │
│              │   • Final status        │                         │
│              │   • Recommendation      │                         │
│              │   • Lessons learned     │                         │
│              └─────────────────────────┘                         │
│                           │                                       │
│                           ▼                                       │
│              ┌─────────────────────────┐                         │
│              │   Log to napkin.md      │                         │
│              │   "Evolution outcome"   │                         │
│              └─────────────────────────┘                         │
└───────────────────────────────────────────────────────────────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │   Cycle Continues     │
                    │   (Back to Phase 1)   │
                    └───────────────────────┘
```

## Data Flow

```
┌──────────────┐
│  napkin.md   │────┐
└──────────────┘    │
                    │
┌──────────────┐    │    ┌──────────────┐    ┌──────────────┐
│ TRACKER.md   │────┼───▶│ analyze.py   │───▶│ Pattern      │
└──────────────┘    │    └──────────────┘    │ Report       │
                    │                         └──────────────┘
┌──────────────┐    │                                │
│ rules/*.mdc  │────┘                                │
└──────────────┘                                     │
                                                     ▼
                                          ┌──────────────────┐
                                          │ Proposal         │
                                          │ Generator        │
                                          └──────────────────┘
                                                     │
                                                     ▼
                                          ┌──────────────────┐
                                          │ proposals/       │
                                          │ YYYY-MM-DD.md    │
                                          └──────────────────┘
                                                     │
                                                     ▼
                                          ┌──────────────────┐
                                          │ User Review      │
                                          └──────────────────┘
                                                     │
                                          Accept     │     Reject
                                          ┌──────────┴──────────┐
                                          ▼                     ▼
                                   ┌──────────────┐    ┌──────────────┐
                                   │ backups/     │    │ LOG.md       │
                                   │ YYYY-MM-DD/  │    │ (rejected)   │
                                   └──────────────┘    └──────────────┘
                                          │
                                          ▼
                                   ┌──────────────┐
                                   │ Implement    │
                                   │ Changes      │
                                   └──────────────┘
                                          │
                                          ▼
                                   ┌──────────────┐
                                   │ tracking/    │
                                   │ change-id.md │
                                   └──────────────┘
                                          │
                                          ▼
                                   ┌──────────────┐
                                   │ Monitor      │
                                   │ 7 days       │
                                   └──────────────┘
                                          │
                                          ▼
                                   ┌──────────────┐
                                   │ Evaluate     │
                                   │ & Decide     │
                                   └──────────────┘
                                          │
                              Success     │     Failure
                              ┌───────────┴───────────┐
                              ▼                       ▼
                       ┌──────────────┐      ┌──────────────┐
                       │ Keep Change  │      │ Rollback     │
                       │ Log success  │      │ from backup  │
                       └──────────────┘      └──────────────┘
```

## State Transitions

```
┌─────────────┐
│  DISABLED   │
│  (Default)  │
└─────────────┘
      │
      │ enable.sh
      ▼
┌─────────────┐
│   ENABLED   │
│  Monitoring │
└─────────────┘
      │
      │ Pattern detected
      ▼
┌─────────────┐
│  PROPOSAL   │
│  Generated  │
└─────────────┘
      │
      │ User review
      ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  ACCEPTED   │     │  DEFERRED   │     │  REJECTED   │
└─────────────┘     └─────────────┘     └─────────────┘
      │                    │                    │
      │ Implement          │ Save to            │ Log reason
      ▼                    │ backlog            ▼
┌─────────────┐           ▼              ┌─────────────┐
│IMPLEMENTED  │     ┌─────────────┐      │   CLOSED    │
│  Tracking   │     │   BACKLOG   │      └─────────────┘
└─────────────┘     └─────────────┘
      │
      │ Monitor 7 days
      ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   SUCCESS   │     │   PARTIAL   │     │   FAILED    │
└─────────────┘     └─────────────┘     └─────────────┘
      │                    │                    │
      │ Keep               │ Refine             │ Rollback
      ▼                    ▼                    ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ VALIDATED   │     │  REVISED    │     │ ROLLED_BACK │
└─────────────┘     └─────────────┘     └─────────────┘
```

## File Lifecycle

```
1. Pattern Detection
   └─▶ reports/analysis-YYYY-MM-DD-HH-MM.md (generated)

2. Proposal Creation
   └─▶ proposals/YYYY-MM-DD-HH-MM.md (created)
       Status: PENDING

3. User Accepts
   ├─▶ backups/YYYY-MM-DD-HH-MM/ (created)
   │   └─▶ [original files backed up]
   ├─▶ [target files modified]
   ├─▶ proposals/YYYY-MM-DD-HH-MM.md (updated)
   │   Status: ACCEPTED → IMPLEMENTED
   ├─▶ LOG.md (appended)
   ├─▶ napkin.md (appended)
   └─▶ tracking/YYYY-MM-DD-change-id.md (created)
       Status: MONITORING

4. Effectiveness Review (Day 7)
   ├─▶ tracking/YYYY-MM-DD-change-id.md (updated)
   │   Status: SUCCESS | PARTIAL | FAILED
   └─▶ napkin.md (appended with outcome)

5. If Rollback Needed
   ├─▶ [restore from backups/YYYY-MM-DD-HH-MM/]
   ├─▶ tracking/YYYY-MM-DD-change-id.md (updated)
   │   Status: ROLLED_BACK
   └─▶ LOG.md (appended with rollback reason)
```

## Integration Points

```
┌─────────────────────────────────────────────────────────────┐
│                    Existing Systems                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐        ┌──────────────┐                 │
│  │  napkin.md   │◀──────▶│ Self-        │                 │
│  │              │  Read  │ Evolution    │                 │
│  │  • Input     │  Write │              │                 │
│  │  • Output    │        │              │                 │
│  └──────────────┘        │              │                 │
│                          │              │                 │
│  ┌──────────────┐        │              │                 │
│  │ TRACKER.md   │◀──────▶│              │                 │
│  │              │  Read  │              │                 │
│  │  • Input     │  Write │              │                 │
│  │  • Output    │        │              │                 │
│  └──────────────┘        │              │                 │
│                          │              │                 │
│  ┌──────────────┐        │              │                 │
│  │ rules/*.mdc  │◀──────▶│              │                 │
│  │              │  Read  │              │                 │
│  │  • Input     │  Write │              │                 │
│  │  • Can modify│        │              │                 │
│  └──────────────┘        │              │                 │
│                          │              │                 │
│  ┌──────────────┐        │              │                 │
│  │ skills/      │◀──────▶│              │                 │
│  │              │  Read  │              │                 │
│  │  • Input     │  Write │              │                 │
│  │  • Can modify│        │              │                 │
│  └──────────────┘        └──────────────┘                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Trigger Conditions

```
Automatic Triggers (when enabled):
├─▶ After tracker update (≥10 lines added)
├─▶ After napkin update (≥2 mistakes OR ≥1 correction OR ≥2 what_worked)
└─▶ Periodic review (every 7 days)

Manual Triggers:
├─▶ User says "evolve" or "self-improve"
├─▶ User says "analyze patterns"
├─▶ User says "suggest improvements"
└─▶ User runs analyze.py directly
```

## Safety Mechanisms

```
┌─────────────────────────────────────────────────────────────┐
│                     Safety Guardrails                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Disabled by Default                                     │
│     └─▶ Requires explicit enable.sh                        │
│                                                             │
│  2. User Approval Required                                  │
│     └─▶ No auto-implementation (unless configured)         │
│                                                             │
│  3. Automatic Backups                                       │
│     └─▶ All files backed up before modification            │
│                                                             │
│  4. Threshold Filtering                                     │
│     ├─▶ Value ≥ 6                                          │
│     ├─▶ Risk ≤ 4                                           │
│     └─▶ Confidence ≥ 7                                     │
│                                                             │
│  5. Conflict Detection                                      │
│     └─▶ Checks for rule/skill conflicts                    │
│                                                             │
│  6. Effectiveness Tracking                                  │
│     └─▶ All changes monitored for 7 days                   │
│                                                             │
│  7. Easy Rollback                                           │
│     └─▶ Restore from backups/ directory                    │
│                                                             │
│  8. Source Data Protection                                  │
│     └─▶ Never modifies napkin.md or TRACKER.md structure   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```
