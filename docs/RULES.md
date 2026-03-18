# Rules System Documentation

The rules system in `.cursor/rules/` provides persistent, always-applied instructions that guide the AI's behavior across all sessions. These rules are the foundation of the intelligent skill system.

## Core Rules

### 1. Masterrule (`masterrule.mdc`)

**Purpose**: Enforces mandatory skill scanning before every AI response.

**Status**: `alwaysApply: true` - Active in every session

**What it does**:
- Forces the AI to read `.cursor/skills/INDEX.md` before responding
- Matches your request keywords to relevant skills
- Loads appropriate SKILL.md files automatically
- Requires a "Skill Proof" header showing which skills were used
- Maintains skill priority order (process → implementation → verification)
- Manages the Napkin persistent memory system

**Why it matters**: Without masterrule, the AI might forget to use available skills. With it, expert knowledge is **automatically** applied to every task.

**Key Components**:

1. **Skill Scanning Protocol** (4 steps):
   - Step 1: Read Skills Index
   - Step 2: Load applicable skills
   - Step 3: Produce skill proof header
   - Step 4: Apply skills or declare none

2. **Enforcement Rules**:
   - Any response without "Skill Proof" header is invalid
   - If even 1% chance a skill applies, it MUST be read
   - Process skills come before implementation skills

3. **Napkin System**:
   - Reads `.cursor/napkin.md` at session start
   - Records mistakes, corrections, preferences
   - Compounds learning across sessions

---

### 2. Coordinator Mode (`coordinator-mode.mdc`)

**Purpose**: Orchestrates complex multi-step tasks using subagent dispatch and parallel execution.

**Status**: `alwaysApply: true` - Active in every session

**What it does**:
- Classifies tasks as SIMPLE (direct action) or COORDINATED (subagent orchestration)
- For complex tasks: assesses, plans, dispatches, monitors, verifies, and accepts
- Manages up to 4 parallel subagents for independent work streams
- Enforces spec compliance and code quality reviews
- Prevents file conflicts between concurrent subagents

**When it activates**:
- 3+ independent work streams across modules
- Multi-module feature implementation
- Bug analysis spanning multiple subsystems
- Architecture changes touching 6+ files

**Coordinator Protocol** (6 phases):

1. **ASSESS**: Dispatch explore subagents to gather context
2. **PLAN**: Create TodoWrite decomposition with parallel tracks
3. **DISPATCH**: Launch up to 4 generalPurpose subagents concurrently
4. **MONITOR**: Track progress, store compact summaries
5. **VERIFY**: Run spec compliance + code quality reviews
6. **ACCEPT**: Run tests, synthesize final report

**Context Efficiency**:
- Graph-first: Reads `codebase_graph.json` before files
- Subagent-first reading for files >200 lines
- Compact state: 3-5 line summaries, not full outputs
- Batched dispatch for true parallelism

---

### 3. Auto Battle-Test Plans (`auto-battle-test-plans.mdc`)

**Purpose**: Automatically validates and stress-tests every plan immediately after creation.

**Status**: `alwaysApply: true` - Active in every session

**What it does**:
- After ANY plan is created, immediately battle-tests it
- Checks for: consistency, naming conventions, edge cases, data flow, test coverage, observability, UI/UX, conflicts, duplicates, dependencies
- Auto-revises plans with CRITICAL or HIGH issues
- Presents only the final, clean plan to users

**Battle-Test Checklist** (10 items):
1. Consistency with codebase (files/functions exist?)
2. Naming conventions (camelCase vs snake_case)
3. Edge cases (empty inputs, null values, concurrent access)
4. Data flow correctness (transformations in right order?)
5. Test coverage (all functions covered?)
6. Observability (adequate logging?)
7. UI/UX impact (response shape correct?)
8. Conflicts (file modification conflicts?)
9. Already implemented (duplicate work?)
10. Import paths and dependencies (will imports resolve?)

**Output Format**:
- Severity levels: CRITICAL, HIGH, MEDIUM, LOW
- Auto-revises without asking (user sees final plan only)
- Loop cap: 2 rounds maximum

**What users see**:
```
## Battle-Test Summary
- Rounds: 1 revision needed
- Issues found and fixed: [list]
- Remaining concerns: [if any]
```

---

### 4. Anti-Hang Safeguards (`anti-hang-subagents.mdc`)

**Purpose**: Prevents long-running subagent tasks from hanging by enforcing chunking and progressive output.

**Status**: `alwaysApply: true` - Active in every session

**What it does**:
- Enforces batch processing (max 20 rows per batch)
- Requires incremental writes (never accumulate all outputs)
- Limits subagent prompt size (under 2000 words)
- Enforces progress checkpoints
- Limits parallel subagents (max 4 concurrent)

**7 Anti-Hang Rules**:

1. **Never process all rows in one call**: Split into batches of 20 max
2. **Write incrementally**: Save outputs immediately, not at end
3. **Subagent prompt size limits**: Keep prompts under 2000 words
4. **Avoid reading entire directories inline**: List first, read in groups
5. **Progress checkpoints**: Report after each stage, write intermediate outputs
6. **Fresh sessions prevent accumulation**: Each phase in fresh session
7. **Parallel work limits**: Max 4 subagents, practical max 2-3

**Problem it solves**: Large document processing (100+ rows, 17+ docs) can exhaust context windows and appear to hang.

---

## Additional Rules

### 5. Auto Execute Plans (`auto-execute-plans.mdc`)

**Purpose**: Automatically executes plans after creation without waiting for user confirmation.

**When it activates**: After plan creation, if user has indicated they want immediate execution.

---

### 6. Auto Docs Audit (`auto-docs-audit.mdc`)

**Purpose**: Automatically audits documentation for completeness, accuracy, and consistency.

**When it activates**: When documentation is created or modified.

---

### 7. Pipeline Execution (`pipeline-execution.mdc`)

**Purpose**: Manages multi-phase pipeline execution with state tracking and error recovery.

**When it activates**: For complex pipeline workflows requiring phase-by-phase execution.

---

### 8. Tracker Maintenance (`tracker-maintenance.mdc`)

**Purpose**: Enforces persistent project history tracking across sessions.

**Status**: `alwaysApply: true` - Active in every session

**What it does**:
- Enforces reading tracker before substantial work when history matters
- Enforces updating tracker after meaningful completed work
- Defines when to read (multi-file features, conventions, avoiding duplicates)
- Defines when to update (features, bug fixes, refactors, docs milestones)
- Specifies format: `## [YYYY-MM-DD] - Title` with purpose, changes, files, verification, outcome
- Integrates with project-tracker skill for detailed guidance

**Default tracker locations**: `TRACKER.md`, `docs/tracker.md`, `docs/TRACKER.md`

**Why it matters**: Without persistent history, each session starts from zero. The tracker provides project memory, helping avoid duplicate work and maintain context about what was built and why.

**Anti-hang safeguard**: Never updates tracker as sole tool call (prevents IDE hang).

**[Learn more about the tracker →](CUSTOM_SKILLS.md#project-tracker)**

---

## How Rules Work Together

```
User Request
    ↓
Masterrule (enforces skill scanning)
    ↓
Skills Index → Load relevant skills
    ↓
Coordinator Mode (classifies task complexity)
    ↓
    ├─→ SIMPLE: Direct action
    │   └─→ Tracker Maintenance (read/update history)
    │
    └─→ COORDINATED:
        ├─→ Auto Battle-Test Plans (validates plans)
        ├─→ Anti-Hang Safeguards (prevents hangs)
        ├─→ Tracker Maintenance (read/update history)
        └─→ Subagent dispatch with reviews
```

## Rule Priority

1. **Masterrule**: Always runs first (skill scanning)
2. **Coordinator Mode**: Classifies and orchestrates
3. **Auto Battle-Test Plans**: Validates plans before execution
4. **Anti-Hang Safeguards**: Prevents context exhaustion
5. **Domain-specific rules**: Applied as needed

## Customizing Rules

### Disabling a Rule

To disable a rule, set `alwaysApply: false` in the frontmatter:

```yaml
---
name: rule-name
alwaysApply: false
---
```

### Creating a New Rule

1. Create a `.mdc` file in `.cursor/rules/`
2. Add frontmatter with metadata:
   ```yaml
   ---
   name: my-custom-rule
   description: What this rule does
   globs: ["**/*.js"]  # Optional: apply to specific files
   alwaysApply: true   # Or false for conditional application
   ---
   ```
3. Write rule instructions in markdown

### File-Specific Rules

Use `globs` to apply rules to specific file patterns:

```yaml
---
name: react-component-rules
globs: ["**/*.tsx", "**/*.jsx"]
alwaysApply: true
---
```

## Best Practices

1. **Keep rules focused**: Each rule should have a single, clear purpose
2. **Use alwaysApply sparingly**: Only for rules that should run in every session
3. **Document clearly**: Explain what the rule does and when it activates
4. **Test interactions**: Ensure new rules don't conflict with existing ones
5. **Monitor performance**: Too many always-applied rules can slow responses

## Troubleshooting

### Rules not being applied?

1. Check frontmatter syntax (YAML must be valid)
2. Verify `alwaysApply: true` is set
3. Restart Cursor IDE
4. Check Cursor logs for rule parsing errors

### Rules conflicting?

1. Review rule priority order
2. Check for overlapping `globs` patterns
3. Consider consolidating related rules
4. Use conditional application (`alwaysApply: false`) where appropriate

### Performance issues?

1. Reduce number of always-applied rules
2. Use file-specific globs instead of global application
3. Simplify rule logic
4. Consider combining related rules

---

**Related Documentation**:
- [Architecture Overview](ARCHITECTURE.md) - How the system works
- [Skills System](../dot_cursor/skills/INDEX.md) - Available skills
- [Other IDEs](OTHER_IDES.md) - Using with VSCode and other editors
