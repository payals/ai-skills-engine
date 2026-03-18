---
name: using-superpowers
description: Use when starting any conversation - establishes how to find and use skills by reading relevant SKILL.md files before ANY response
---

<EXTREMELY-IMPORTANT>
If you think there is even a 1% chance a skill might apply to what you are doing, you ABSOLUTELY MUST read the skill.

IF A SKILL APPLIES TO YOUR TASK, YOU DO NOT HAVE A CHOICE. YOU MUST USE IT.

This is not negotiable. This is not optional. You cannot rationalize your way out of this.
</EXTREMELY-IMPORTANT>

# Using Skills

## The Rule

**Check for skills BEFORE ANY RESPONSE.** This includes clarifying questions. Use the Read tool to read relevant `SKILL.md` files from `.cursor/skills/` based on task context.

## How to Find Skills

All skills are in `.cursor/skills/`. Match your task to the appropriate skill directory and read its `SKILL.md`:

### Task → Skill Mapping

| Task Type | Read These Skills |
|-----------|-------------------|
| **Planning/Design** | `.cursor/skills/development/brainstorming/SKILL.md`, `.cursor/skills/development/create-plan/SKILL.md`, `.cursor/skills/development/writing-plans/SKILL.md` |
| **Bug fixing/Debugging** | `.cursor/skills/problem-solving/when-stuck/SKILL.md`, `.cursor/skills/development/error-resolver/SKILL.md` |
| **Database work** | `.cursor/skills/database/` — choose based on DB (postgres, neon, supabase) |
| **Schema design** | `.cursor/skills/development/database-schema-designer/SKILL.md` |
| **Testing** | `.cursor/skills/development/test-driven-development/SKILL.md`, `.cursor/skills/development/testing-patterns/SKILL.md` |
| **Test failures** | `.cursor/skills/development/test-fixing/SKILL.md` |
| **Code review** | `.cursor/skills/development/code-reviewer/SKILL.md`, `.cursor/skills/development/code-review-checklist/SKILL.md` |
| **Architecture** | `.cursor/skills/development/senior-architect/SKILL.md`, `.cursor/skills/development/software-architecture/SKILL.md` |
| **Backend/API** | `.cursor/skills/development/senior-backend/SKILL.md` |
| **Frontend/UI** | `.cursor/skills/development/senior-frontend/SKILL.md`, `.cursor/skills/development/frontend-dev-guidelines/SKILL.md` |
| **DevOps/Infrastructure** | `.cursor/skills/development/senior-devops/SKILL.md`, `.cursor/skills/development/devops-iac-engineer/SKILL.md` |
| **Docker** | `.cursor/skills/development/docker-expert/SKILL.md` |
| **Security** | `.cursor/skills/development/senior-security/SKILL.md`, `.cursor/skills/development/senior-secops/SKILL.md` |
| **ML/AI** | `.cursor/skills/development/senior-ml-engineer/SKILL.md`, `.cursor/skills/development/senior-prompt-engineer/SKILL.md` |
| **Data engineering** | `.cursor/skills/development/senior-data-engineer/SKILL.md`, `.cursor/skills/development/senior-data-scientist/SKILL.md` |
| **Git commits** | `.cursor/skills/development/git-commit/SKILL.md` |
| **Feature design** | `.cursor/skills/development/feature-design-assistant/SKILL.md` |
| **Stuck/blocked** | `.cursor/skills/problem-solving/when-stuck/SKILL.md`, `.cursor/skills/problem-solving/SKILL.md` |
| **Verification** | `.cursor/skills/development/verification-before-completion/SKILL.md` |

### Workflow

1. **Identify task type** from user message
2. **Read relevant SKILL.md** using the Read tool
3. **Announce**: "Using [skill name] for [purpose]"
4. **If skill has checklist**: Create TodoWrite todos for each item
5. **Follow skill exactly**

## Red Flags

These thoughts mean STOP—you're rationalizing:

| Thought | Reality |
|---------|---------|
| "This is just a simple question" | Questions are tasks. Check for skills. |
| "I need more context first" | Skill check comes BEFORE clarifying questions. |
| "Let me explore the codebase first" | Skills tell you HOW to explore. Check first. |
| "I can check git/files quickly" | Files lack conversation context. Check for skills. |
| "Let me gather information first" | Skills tell you HOW to gather information. |
| "This doesn't need a formal skill" | If a skill exists, use it. |
| "I remember this skill" | Skills evolve. Read current version. |
| "This doesn't count as a task" | Action = task. Check for skills. |
| "The skill is overkill" | Simple things become complex. Use it. |
| "I'll just do this one thing first" | Check BEFORE doing anything. |
| "This feels productive" | Undisciplined action wastes time. Skills prevent this. |

## Skill Priority

When multiple skills could apply, use this order:

1. **Process skills first** (brainstorming, debugging) - these determine HOW to approach the task
2. **Implementation skills second** (frontend-design, database) - these guide execution

"Let's build X" → brainstorming first, then implementation skills.
"Fix this bug" → when-stuck/debugging first, then domain-specific skills.

## Skill Types

**Rigid** (TDD, debugging): Follow exactly. Don't adapt away discipline.

**Flexible** (patterns): Adapt principles to context.

The skill itself tells you which.

## User Instructions

Instructions say WHAT, not HOW. "Add X" or "Fix Y" doesn't mean skip workflows.
