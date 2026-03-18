# Using AI Skills in Other IDEs

While this repository is optimized for Cursor IDE, the skills and knowledge can be adapted to work with other AI-powered code editors and agents.

## VSCode with GitHub Copilot Chat

### Overview

VSCode with GitHub Copilot Chat doesn't have native support for `.cursor/rules/` files, but you can replicate the skill system using:
- **Workspace instructions** (`.github/copilot-instructions.md`)
- **Custom instructions** in Copilot settings
- **Manual skill invocation** via chat

### Setup Instructions

#### 1. Install GitHub Copilot

```bash
# Install Copilot extensions
code --install-extension GitHub.copilot
code --install-extension GitHub.copilot-chat
```

#### 2. Create Workspace Instructions

Create `.github/copilot-instructions.md` in your project root:

```markdown
# AI Assistant Instructions

## Skill System

This project uses a skill-based AI assistant system. Skills are located in `.cursor/skills/`.

### Before responding to any request:

1. Check `.cursor/skills/INDEX.md` for relevant skills
2. Read the matching SKILL.md file(s)
3. Apply the skill instructions
4. Indicate which skills were used in your response

### Available Skill Categories:

- development/ - Core development skills
- ai-research/ - AI/ML engineering
- database/ - Database design and optimization
- document-processing/ - PDF, DOCX, XLSX handling
- problem-solving/ - Creative problem-solving techniques
- web-development/ - Web development patterns
- workflow-automation/ - Automation and CI/CD
- utilities/ - General utilities

### Quick Dispatch:

- Planning/Design → brainstorming, create-plan
- Bug fixing → when-stuck, error-resolver
- Testing → test-driven-development, testing-patterns
- Code review → code-reviewer
- Git commits → git-commit
- Docker → docker-expert
- Database → using-neon, supabase-postgres
- Backend → senior-backend
- Frontend → senior-frontend, react-best-practices

[Add more specific instructions for your project]
```

#### 3. Reference Skills in Chat

When asking Copilot for help, explicitly reference skills:

```
@workspace Use the docker-expert skill to optimize this Dockerfile
```

```
@workspace Check .cursor/skills/INDEX.md and apply the relevant skill for fixing this React error
```

### Limitations

**What doesn't work**:
- ❌ Automatic skill scanning (no `alwaysApply: true` equivalent)
- ❌ Mandatory skill proof headers
- ❌ Napkin persistent memory system
- ❌ Coordinator mode with subagent dispatch
- ❌ Auto battle-test plans

**What works**:
- ✅ Manual skill invocation via chat
- ✅ Workspace-level instructions
- ✅ Reading SKILL.md files when asked
- ✅ Following skill patterns and best practices

### Workarounds

#### Simulating Masterrule

Add to your Copilot instructions:

```markdown
## Mandatory Skill Check Protocol

Before responding to ANY request:
1. Read .cursor/skills/INDEX.md
2. Match the request to relevant skills
3. Load and apply the SKILL.md files
4. Start your response with: "Skills used: [skill-name]"
```

**Note**: This relies on Copilot following instructions consistently, which is not guaranteed.

#### Simulating Napkin

Create a `NOTES.md` file in your project:

```markdown
# Project Notes

## Mistakes & Corrections
- [Date] [What went wrong and how it was fixed]

## User Preferences
- [Date] [Preference or style guideline]

## What Worked
- [Date] [Successful approach or pattern]
```

Reference it in chat: `@workspace Check NOTES.md for project-specific learnings`

---

## VSCode with Continue

### Overview

[Continue](https://continue.dev) is an open-source AI code assistant for VSCode that supports custom context providers and slash commands.

### Setup Instructions

#### 1. Install Continue

```bash
code --install-extension Continue.continue
```

#### 2. Configure Context Providers

Edit `~/.continue/config.json`:

```json
{
  "contextProviders": [
    {
      "name": "skills",
      "params": {
        "directory": ".cursor/skills"
      }
    }
  ],
  "slashCommands": [
    {
      "name": "skill",
      "description": "Load and apply a skill",
      "run": "Read .cursor/skills/{args}/SKILL.md and apply its instructions"
    }
  ]
}
```

#### 3. Use Slash Commands

```
/skill docker-expert
How do I optimize this Dockerfile?
```

```
/skill senior-backend
Review this API endpoint
```

### Advantages Over Copilot

- ✅ Custom slash commands for skills
- ✅ Context providers for automatic skill loading
- ✅ Open-source and extensible
- ✅ Supports multiple LLM providers (OpenAI, Anthropic, local models)

### Limitations

- ❌ No automatic skill scanning without custom extension
- ❌ No rule system equivalent
- ❌ Manual skill invocation required

---

## VSCode with Cline (formerly Claude Dev)

### Overview

[Cline](https://github.com/cline/cline) is a VSCode extension that brings Claude directly into your editor with autonomous coding capabilities.

### Setup Instructions

#### 1. Install Cline

```bash
code --install-extension saoudrizwan.claude-dev
```

#### 2. Configure Custom Instructions

In Cline settings, add custom instructions:

```
Before responding to any request:
1. Check if .cursor/skills/INDEX.md exists
2. If it does, read it and find relevant skills
3. Load the matching SKILL.md files
4. Apply the skill instructions
5. Indicate which skills you used

Skills are organized by category in .cursor/skills/[category]/[skill]/SKILL.md
```

#### 3. Use Skills in Chat

```
Check the skills index and apply the appropriate skill for this task: [your request]
```

### Advantages

- ✅ Claude-powered (same model as Cursor)
- ✅ Autonomous coding capabilities
- ✅ Can read and apply SKILL.md files
- ✅ Supports custom instructions

### Limitations

- ❌ No automatic skill enforcement
- ❌ No coordinator mode
- ❌ Manual skill reference required

---

## General Adaptation Strategy

### For Any AI Code Editor

1. **Copy the skills directory**:
   ```bash
   cp -r /path/to/ai-skills-engine/dot_cursor/skills .cursor/skills
   ```

2. **Create a skill invocation pattern**:
   - Add workspace/project instructions
   - Create a convention for referencing skills
   - Document the skill system in your project README

3. **Manual skill workflow**:
   ```
   Step 1: User identifies task type
   Step 2: User checks .cursor/skills/INDEX.md
   Step 3: User tells AI: "Use the [skill-name] skill"
   Step 4: AI reads and applies SKILL.md
   ```

4. **Adapt skill content**:
   - Some skills reference Cursor-specific features (artifacts, subagents)
   - Modify SKILL.md files to remove Cursor-specific instructions
   - Keep the core knowledge and patterns

### What Transfers Well

✅ **Knowledge and patterns**: All skill content (best practices, patterns, checklists)
✅ **Manual invocation**: Explicitly asking AI to use a skill
✅ **Documentation**: Skills as reference documentation
✅ **Checklists**: Using skills as quality checklists

### What Doesn't Transfer

❌ **Automatic enforcement**: No equivalent to `alwaysApply: true`
❌ **Skill scanning**: No automatic skill discovery
❌ **Napkin system**: No persistent memory across sessions
❌ **Coordinator mode**: No subagent orchestration
❌ **Battle-testing**: No automatic plan validation

---

## Creating a Lightweight Version

For editors without advanced AI features, create a simplified version:

### 1. Extract Core Knowledge

Create a `CONVENTIONS.md` file:

```markdown
# Project Conventions

## Docker
[Core principles from docker-expert skill]

## Backend
[Core principles from senior-backend skill]

## Frontend
[Core principles from senior-frontend skill]

[etc.]
```

### 2. Create Checklists

Create `CHECKLISTS.md`:

```markdown
# Code Review Checklist
[From code-review-checklist skill]

# Testing Checklist
[From test-driven-development skill]

# Deployment Checklist
[From senior-devops skill]
```

### 3. Reference in AI Chat

```
Before we start, please read CONVENTIONS.md and follow the [relevant section] guidelines
```

---

## Official Resources

### VSCode AI Extensions

- **GitHub Copilot**: https://github.com/features/copilot
- **Continue**: https://continue.dev/docs
- **Cline (Claude Dev)**: https://github.com/cline/cline
- **Tabnine**: https://www.tabnine.com/
- **Codeium**: https://codeium.com/

### VSCode Custom Instructions

- **Copilot Instructions**: https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot
- **Workspace Settings**: https://code.visualstudio.com/docs/getstarted/settings

### AI Agent Frameworks

- **LangChain**: For building custom AI agents
- **AutoGPT**: For autonomous task execution
- **Semantic Kernel**: Microsoft's AI orchestration framework

---

## Contributing Adaptations

If you successfully adapt this skill system to another IDE or AI tool, please contribute your setup:

1. Fork this repository
2. Add your adaptation guide to `docs/OTHER_IDES.md`
3. Include setup instructions, limitations, and workarounds
4. Submit a pull request

---

## Future Compatibility

As AI code editors evolve, we expect:

- **Better custom instruction support**: More editors adopting rule-like systems
- **Context provider APIs**: Standardized ways to inject knowledge
- **Skill marketplace**: Shared skill repositories across tools
- **Cross-editor standards**: Common formats for AI instructions

This repository will be updated as new capabilities emerge.

---

**Related Documentation**:
- [Rules System](RULES.md) - How Cursor rules work
- [Architecture](ARCHITECTURE.md) - System design
- [Skills Index](../dot_cursor/skills/INDEX.md) - Available skills
