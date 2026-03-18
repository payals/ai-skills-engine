# Custom Skills & Rules Documentation

This document provides detailed explanations of all custom skills and rules created specifically for the AI Skills Engine. These represent original innovations in AI agent orchestration, workflow management, and quality enforcement.

## Table of Contents

- [Custom Rules](#custom-rules)
- [Custom Workflow Skills](#custom-workflow-skills)
- [Custom Problem-Solving Skills](#custom-problem-solving-skills)
- [Custom Development Skills](#custom-development-skills)
- [Custom Workflows](#custom-workflows)
- [Design Philosophy](#design-philosophy)

---

## Custom Rules

Rules are enforcement mechanisms that run automatically via `alwaysApply: true`. They define **WHEN** and **THAT** behaviors must occur, delegating **HOW** to skills.

### 1. masterrule.mdc

**Purpose**: Mandatory skill scanning protocol that ensures expertise is applied to every response.

**How it works**:
1. Intercepts every user request
2. Reads `INDEX.md` to match keywords to relevant skills
3. Loads applicable `SKILL.md` files
4. Requires "Skill Proof" header showing which skills were applied
5. Integrates napkin.md for persistent mistake memory

**Why it exists**: Without enforcement, skills are optional and often ignored. This rule makes expertise mandatory and auditable.

**Key innovation**: The "Skill Proof" header provides transparency about which expertise was applied, making the AI's decision-making process visible.

### 2. coordinator-mode.mdc

**Purpose**: Multi-agent orchestration system that classifies tasks and coordinates parallel/sequential work.

**How it works**:
- **Phase 1 (ASSESS)**: Dispatch explore subagents to gather context
- **Phase 2 (PLAN)**: Create decomposition with TodoWrite, identify parallel tracks
- **Phase 3 (DISPATCH)**: Launch up to 4 concurrent generalPurpose subagents
- **Phase 4 (MONITOR)**: Track completion, store compact summaries
- **Phase 5 (VERIFY)**: Dispatch spec compliance + code quality review subagents
- **Phase 6 (ACCEPT)**: Run tests, synthesize final report

**Why it exists**: Complex tasks need structured coordination to prevent:
- File conflicts (two subagents editing the same file)
- Missing verification (code shipped without tests)
- Context accumulation (one agent doing everything)

**Key innovation**: The two-stage review (spec compliance → code quality) catches both "wrong thing built correctly" and "right thing built poorly."

### 3. auto-battle-test-plans.mdc

**Purpose**: Automatically validates every plan before presenting it to the user.

**How it works**:
1. After creating ANY plan, immediately battle-test it
2. Check 10 dimensions: consistency, naming conventions, edge cases, data flow, tests, observability, UI/UX, conflicts, already-implemented, imports
3. Auto-revise if CRITICAL or HIGH issues found
4. Loop cap: 2 rounds maximum
5. Present only the final revised plan

**Why it exists**: Plans often have subtle issues (wrong function names, missing edge cases, incorrect assumptions) that waste time during execution. Catching them upfront saves hours.

**Key innovation**: The battle-test runs **before** user confirmation, so users only see clean, validated plans.

### 4. anti-hang-subagents.mdc

**Purpose**: Prevents context exhaustion when processing large document sets.

**How it works**:
- Never process all rows in one call (max 20 rows per batch)
- Write incrementally after each batch
- Keep subagent prompts under 2000 words
- Avoid reading entire directories inline
- Report progress after each stage
- Limit to 2-3 concurrent subagents for large pipelines

**Why it exists**: Processing 100+ requirement rows in one subagent exhausts context windows and appears to hang. Batching prevents this.

**Key innovation**: Fresh sessions per phase + incremental writes ensure partial progress is always saved.

### 5. tracker-maintenance.mdc

**Purpose**: Enforces reading/updating project tracker files for persistent history.

**How it works**:
- **MUST read tracker** before substantial work when history may matter
- **MUST update tracker** after meaningful completed work (features, bug fixes, refactors)
- Default locations: `TRACKER.md`, `docs/tracker.md`, `docs/TRACKER.md`
- Format: `## [YYYY-MM-DD] - Title` with purpose, changes, files, verification, outcome
- Anti-hang: Never update tracker as sole tool call

**Why it exists**: Without persistent history, each session starts from zero. The tracker provides project memory across sessions.

**Key innovation**: Integration with project-tracker skill creates a complete read/write protocol for project history.

### 6. auto-execute-plans.mdc

**Purpose**: Automatically executes .plan.md files when user says "execute."

**How it works**:
1. Triggered by "execute" keyword + .plan.md file presence
2. Loads relevant skills based on plan content
3. Requires documentation audit before execution
4. Follows plan structure with checkpoints

**Why it exists**: Bridges planning and execution phases with automatic skill loading.

### 7. pipeline-execution.mdc

**Purpose**: Specialized mode for RFP pipeline processing with agent impersonation.

**How it works**:
- Triggered by `pipeline/prompts/phase*.md` files
- Agent impersonates roles (Requirements Analyst, Solution Architect, etc.)
- Batch operations for large datasets (100+ rows)
- Fresh session per phase prevents context accumulation

**Why it exists**: RFP response generation requires specialized multi-phase workflows with role-based processing.

### 8. auto-docs-audit.mdc

**Purpose**: Maintains documentation after code changes.

**How it works**:
- Triggered after 3+ file modifications
- Code-to-diagram mapping tables
- Mermaid diagram verification
- Updates affected documentation

**Why it exists**: Documentation drifts from code without automatic maintenance.

---

## Custom Workflow Skills

Workflow skills define **HOW** to execute complex processes. They provide step-by-step protocols.

### project-tracker

**Purpose**: Persistent project history journal across sessions.

**What it does**:
- Teaches when to read tracker (before substantial work)
- Teaches when to update tracker (after meaningful completion)
- Defines entry format with date, purpose, changes, files, verification, outcome
- Explains relationship to plan files, todos, and napkin

**Why it exists**: Projects need memory. Without a tracker, you lose context about what was built, why decisions were made, and what outcomes resulted.

**Key innovation**: Append-only philosophy preserves history. Integration with tracker-maintenance rule creates automatic enforcement.

**Files**: `SKILL.md`, `templates/tracker_template.md`, `examples.md`

### pipeline-evolution

**Purpose**: Self-improving pipeline system that learns from completed runs.

**What it does**:
1. **Harvest**: Extract insights from completed pipeline runs
2. **Consolidate**: Group related learnings
3. **Promote**: Update control plane files and phase prompts
4. **Apply**: Ensure changes are used in next run

**Why it exists**: Pipelines should improve over time. Manual improvement is slow and inconsistent.

**Key innovation**: Automatic promotion of learnings into the pipeline's control files creates a self-improving system.

### verification-before-completion

**Purpose**: Evidence-based completion protocol - never claim done without proof.

**What it does**:
- "Iron Law": Run verification commands before claiming success
- Red-green cycle: Show failure → show fix → show success
- Anti-rationalization: No excuses, only evidence
- Verification commands must be run, not described

**Why it exists**: Agents often claim "tests passing" without actually running them. This skill enforces evidence.

**Key innovation**: The "Iron Law" makes verification non-negotiable. Evidence before assertions, always.

### executing-plans

**Purpose**: Batch execution of implementation plans with review checkpoints.

**What it does**:
1. Read plan file
2. Create TodoWrite for tracking
3. Execute in batches (5-10 steps)
4. Architect review after each batch
5. Handle blockers with user escalation

**Why it exists**: Large plans need structured execution with quality gates.

**Key innovation**: Architect review between batches catches issues early before they compound.

### writing-plans

**Purpose**: Create comprehensive implementation plans before coding.

**What it does**:
- Bite-sized tasks (2-5 minutes each)
- TDD-focused structure (tests before implementation)
- Clear handoff to execution (subagent-driven or parallel)
- Explicit file paths and function names

**Why it exists**: Good plans prevent rework. Vague plans waste time.

**Key innovation**: Granularity requirement (2-5 min tasks) forces concrete thinking.

### brainstorming

**Purpose**: Idea-to-design dialogue before implementation.

**What it does**:
- One question at a time (no walls of text)
- 200-300 word sections with validation
- YAGNI enforcement (You Aren't Gonna Need It)
- Clarify requirements before proposing solutions

**Why it exists**: Jumping to implementation without understanding requirements leads to wrong solutions.

**Key innovation**: Mandatory brainstorming before creative work prevents premature implementation.

### using-superpowers

**Purpose**: Skill discovery protocol - find and use relevant skills.

**What it does**:
- Task-to-skill mapping table
- Red flag rationalization prevention ("I'll just...")
- Mandatory skill checking before responses
- Process skills first (brainstorming, when-stuck) then implementation

**Why it exists**: Skills are useless if agents don't know when to use them.

**Key innovation**: The mapping table makes skill discovery systematic, not random.

### feature-design-assistant

**Purpose**: Natural collaborative dialogue for feature planning.

**What it does**:
- Turn ideas into fully formed designs through conversation
- Ask clarifying questions
- Explore edge cases
- Propose architecture before implementation

**Why it exists**: Features need design, not just code.

### git-commit

**Purpose**: Conventional commit message automation.

**What it does**:
- Auto-detect commit type (feat, fix, refactor, etc.)
- Generate commit message from diff
- Interactive override of type/scope/description
- Intelligent file staging for logical grouping

**Why it exists**: Good commit messages require consistency and thought. Automation ensures both.

### dispatching-parallel-agents

**Purpose**: Orchestrate multiple independent tasks concurrently.

**What it does**:
- Identify independent work streams
- Launch parallel subagents (up to 4)
- Prevent file conflicts
- Aggregate results

**Why it exists**: Sequential execution of parallel work is slow.

### test-fixing

**Purpose**: Systematic test failure resolution.

**What it does**:
- Run test suite
- Group failures by error type
- Fix in batches
- Re-run to verify
- Loop until all passing

**Why it exists**: Fixing tests one-by-one is inefficient. Smart grouping speeds it up.

### using-git-worktrees

**Purpose**: Create isolated workspaces for feature work.

**What it does**:
- Smart directory selection
- Safety verification
- Worktree creation with proper branching
- Cleanup after merge

**Why it exists**: Feature work needs isolation from current workspace.

---

## Custom Problem-Solving Skills

Techniques for breaking through stuck points.

### when-stuck

**Purpose**: Dispatcher to the right problem-solving technique based on how you're stuck.

**What it does**:
- Diagnose stuck type (too complex, too vague, conflicting constraints, etc.)
- Route to appropriate technique
- Provides decision tree

**Why it exists**: Different stuck types need different techniques. This skill routes correctly.

### collision-zone-thinking

**Purpose**: Force unrelated concepts together to discover emergent properties.

**What it does**:
- "What if we treated X like Y?"
- Cross-domain analogies
- Unexpected combinations

**Why it exists**: Innovation often comes from combining unrelated ideas.

**Example**: "What if we treated API rate limits like traffic lights?" → Leads to adaptive throttling.

### inversion-exercise

**Purpose**: Flip core assumptions to reveal hidden constraints.

**What it does**:
- "What if the opposite were true?"
- Challenge foundational beliefs
- Find alternative approaches

**Why it exists**: Assumptions blind us to better solutions.

**Example**: "What if we didn't need a database?" → Leads to stateless architecture.

### meta-pattern-recognition

**Purpose**: Spot patterns appearing across 3+ domains to find universal principles.

**What it does**:
- Identify recurring structures
- Extract general principles
- Apply to new domains

**Why it exists**: Universal patterns are powerful abstractions.

**Example**: "Caching appears in CPU, DNS, CDN, and databases" → Extract general caching principles.

### scale-game

**Purpose**: Test at extremes (1000x bigger/smaller, instant/year-long) to expose fundamental truths.

**What it does**:
- Scale problem up 1000x
- Scale problem down 1000x
- What breaks? What becomes obvious?

**Why it exists**: Normal scales hide fundamental constraints.

**Example**: "What if we had 1 user?" → Reveals over-engineering. "What if we had 1 billion users?" → Reveals scalability issues.

### simplification-cascades

**Purpose**: Find one insight that eliminates multiple components.

**What it does**:
- "If this is true, we don't need X, Y, or Z"
- Cascade simplifications
- Reduce complexity dramatically

**Why it exists**: The best solutions are simple.

**Example**: "If we make it stateless, we don't need session storage, sticky sessions, or session replication."

---

## Custom Development Skills

### create-plan

**Purpose**: Create concise implementation plans.

**What it does**:
- User explicitly asks for plan
- Create structured plan file
- Handoff to executing-plans or subagent-driven-development

**Why it exists**: Simple planning skill for when user wants a plan.

### clean-code

**Purpose**: Pragmatic coding standards without over-engineering.

**What it does**:
- Concise, direct code
- No unnecessary comments
- No premature abstraction
- Readability over cleverness

**Why it exists**: Clean code is maintainable code.

### code-review-checklist

**Purpose**: Comprehensive review checklist.

**What it does**:
- Functionality, security, performance, maintainability
- Systematic review process
- Catches common issues

**Why it exists**: Consistent reviews catch more issues.

### database-design

**Purpose**: Database design principles and decision-making.

**What it does**:
- Schema design
- Indexing strategy
- ORM selection
- Serverless databases

**Why it exists**: Good database design prevents future pain.

### software-architecture

**Purpose**: Quality-focused architecture guide.

**What it does**:
- Architecture patterns
- Trade-off analysis
- Scalability considerations
- Tech stack decisions

**Why it exists**: Architecture decisions have long-term consequences.

### test-driven-development

**Purpose**: TDD workflow and patterns.

**What it does**:
- Red-green-refactor cycle
- Test-first mindset
- Test organization
- Mocking strategies

**Why it exists**: TDD produces better-designed, more testable code.

### testing-patterns

**Purpose**: Jest testing patterns and factory functions.

**What it does**:
- Factory functions for test data
- Mocking strategies
- Test organization
- Common patterns

**Why it exists**: Consistent testing patterns improve test quality.

---

## Custom Workflows

### cursor-prompt-queue

**Repository**: https://github.com/payals/cursor-prompt-queue

**Purpose**: Batch sequential prompts with dynamic variable passing between steps. Fresh context per step without context rot.

**How it works**:
1. Write prompts in a queue file with `{{step_N.key}}` placeholders
2. Say "execute prompt queue"
3. Agent dispatches fresh subagent for each step
4. Captures declared outputs
5. Resolves placeholders in subsequent steps
6. Resumable across sessions via state file

**Why it exists**: Multi-step tasks hit three friction points:
1. Waiting between prompts
2. Context rot in long sessions
3. Manual handoff of dynamic references

**Key innovation**: Dynamic placeholder resolution (`{{step_1.plan_file}}`) allows steps to reference outputs from earlier steps without knowing paths ahead of time.

**Example**:
```markdown
## Step 1: Create migration plan
### Prompt
Create an implementation plan for the database migration. Save to docs/plans/.
### Outputs
- plan_file: path to the plan file created

---

## Step 2: Execute the plan
### Prompt
Execute the plan at {{step_1.plan_file}}.
### Outputs
(none)
```

**Integration**: Can be installed into any Cursor project. Complements the AI Skills Engine's orchestration capabilities.

---

## Design Philosophy

### Separation of Concerns

**Rules** enforce **WHEN** and **THAT**:
- "You MUST read tracker before substantial work"
- "You MUST update tracker after completion"
- "You MUST battle-test plans before presenting"

**Skills** teach **HOW** and **WHY**:
- "Here's how to write a good tracker entry"
- "Here's why the tracker is valuable"
- "Here's the template to follow"

### Enforcement + Guidance

Rules provide guardrails, skills provide expertise. Together they create:
- **Mandatory quality** (rules enforce)
- **High quality** (skills guide)
- **Auditable quality** (skill proof shows what was applied)

### Fresh Context Philosophy

Multiple custom components enforce fresh context:
- **coordinator-mode**: Dispatches fresh subagents per track
- **anti-hang-subagents**: Fresh sessions per pipeline phase
- **cursor-prompt-queue**: Fresh subagent per queue step

**Why**: Context rot degrades quality. Fresh context maintains quality across long tasks.

### Evidence-Based Completion

Multiple components enforce evidence:
- **verification-before-completion**: Run commands, show output
- **auto-battle-test-plans**: Check 10 dimensions before presenting
- **coordinator-mode Phase 5**: Spec compliance + code quality reviews

**Why**: Claims without evidence lead to broken code. Evidence prevents this.

### Self-Improvement

Multiple components enable learning:
- **napkin.md**: Persistent mistake memory
- **pipeline-evolution**: Harvest insights, promote to control plane
- **tracker**: Project history informs future decisions

**Why**: Systems that learn from experience get better over time.

---

## Integration Map

How custom rules and skills work together:

```
masterrule.mdc
├─ Enforces skill scanning
├─ Requires skill proof
└─ Integrates napkin.md

coordinator-mode.mdc
├─ Uses verification-before-completion (Phase 5)
├─ Uses holistic-bug-analysis (for bug fixes)
├─ Uses holistic-testing (for features)
└─ Uses TodoWrite (Phase 2)

auto-battle-test-plans.mdc
├─ Triggered after create-plan
└─ Uses project-tracker skill for history checks

tracker-maintenance.mdc
├─ Enforces read/update triggers
└─ Delegates HOW to project-tracker skill

auto-execute-plans.mdc
├─ Triggered by "execute" + .plan.md
├─ Uses executing-plans skill
└─ May trigger coordinator-mode for complex plans

pipeline-execution.mdc
├─ Uses anti-hang-subagents rules
└─ Uses pipeline-evolution for self-improvement
```

---

## Contributing Custom Skills

When creating new custom skills/rules:

1. **Rules** should:
   - Enforce WHEN/THAT, not HOW
   - Be lightweight (60-180 lines)
   - Reference skills for details
   - Include anti-patterns section

2. **Skills** should:
   - Teach HOW/WHY comprehensively
   - Include examples and templates
   - Explain relationship to other files
   - Provide quick reference checklists

3. **Both** should:
   - Have clear frontmatter with triggers
   - Be documented in this file
   - Include attribution if adapted from others
   - Follow existing patterns

See [ATTRIBUTIONS.md](../ATTRIBUTIONS.md) for licensing and attribution guidelines.
