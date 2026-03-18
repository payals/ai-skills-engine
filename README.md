# AI Skills Engine

> **Supercharge your AI coding assistant with 280+ expert skills and intelligent automation**

A comprehensive, battle-tested collection of AI agent skills and rules for Cursor IDE (and other AI code editors) that transforms your development workflow with context-aware, expert-level assistance.

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/Skills-280%2B-green.svg)](dot_cursor/skills/INDEX.md)
[![Rules](https://img.shields.io/badge/Rules-7-orange.svg)](docs/RULES.md)

---

## 🎯 What is This?

This repository contains a pre-configured `.cursor` directory with:

- **280+ Skills**: Specialized AI capabilities across development, AI/ML, databases, document processing, and more
- **Intelligent Rules System**: Automatic skill discovery and application via the masterrule
- **Skills Index**: Searchable catalog that helps AI find and apply the right expertise automatically
- **Persistent Memory**: Napkin system that learns from mistakes and user preferences across sessions
- **Multi-Agent Orchestration**: Coordinator mode for complex tasks with parallel subagent dispatch

**The key differentiator**: The **masterrule** ensures skills are **automatically scanned and applied** in every session. Your AI assistant doesn't just have access to skills—it's **required** to use them.

---

## 📊 How It Works

![Architecture Diagram](docs/architecture-diagram.png)

The system uses an always-applied rule (masterrule) that enforces a mandatory skill scanning protocol:

1. **User makes a request** → Masterrule intercepts
2. **Reads Skills Index** → Matches keywords to relevant skills
3. **Loads SKILL.md files** → Applies expert knowledge
4. **Coordinator classifies** → Simple (direct) or Complex (subagents)
5. **Delivers response** → With skill proof showing what was applied

**[Learn more about the architecture →](docs/RULES.md)**

---

## 🚀 Quick Start

### Installation (2 minutes)

```bash
# 1. Clone this repository
git clone https://github.com/yourusername/ai-skills-engine.git
cd ai-skills-engine

# 2. Copy to your Cursor project
cd /path/to/your/project
cp -r /path/to/ai-skills-engine/dot_cursor .cursor

# 3. Open Cursor IDE - skills are now active!
```

That's it! The masterrule will automatically start using skills in your next session.

### Verify Installation

Open Cursor and ask: *"What skills are available?"*

The AI should read `.cursor/skills/INDEX.md` and list available skills with a "Skill Proof" header.

---

## 💡 Quick Examples

### Example 1: Docker Optimization

```
You: "My Docker build is taking 10 minutes. Help optimize it."

AI: ## Skill Proof
    Skills Used: docker-expert
    Key Principle: Multi-stage builds + layer caching
    
    [Applies Docker expertise automatically]
    - Analyzes Dockerfile
    - Suggests multi-stage build pattern
    - Optimizes layer caching
    - Reduces build time to 2 minutes
```

### Example 2: Bug Fixing

```
You: "Getting a TypeError in my React component"

AI: ## Skill Proof
    Skills Used: error-resolver, senior-frontend
    
    [Systematically diagnoses]
    - Root cause analysis
    - Checks component lifecycle
    - Provides fix with explanation
```

### Example 3: Feature Planning

```
You: "I want to add user authentication"

AI: ## Skill Proof
    Skills Used: brainstorming (process skill first!)
    
    [Asks clarifying questions]
    - Session vs JWT?
    - OAuth providers?
    - Password requirements?
    
    [Then loads senior-backend for implementation]
```

---

## 📚 Skill Categories

<details>
<summary><b>Development (80+ skills)</b> - Core coding, testing, planning</summary>

- `brainstorming` - Explore requirements before implementation ⭐
- `senior-backend` - Backend systems (Node, Go, Python, Postgres)
- `senior-frontend` - Frontend (React, Next.js, TypeScript)
- `docker-expert` - Container optimization and security
- `git-commit` - Conventional commits with intelligent staging
- `code-reviewer` - Comprehensive code review
- `verification-before-completion` - Evidence-based completion ⭐
- `test-driven-development` - TDD workflow
- `error-resolver` - Systematic error diagnosis
- `senior-architect` - System design and architecture
- And 70+ more...

</details>

<details>
<summary><b>AI Research (100+ skills)</b> - LLMs, training, inference</summary>

- `crewai` - Multi-agent orchestration
- `langgraph` - Stateful AI applications
- `prompt-engineer` - LLM optimization
- `rag-engineer` - Retrieval-augmented generation
- `fine-tuning-axolotl` - Fast fine-tuning
- `distributed-training-deepspeed` - ZeRO optimization
- `inference-serving-vllm` - High-throughput serving
- `evaluation-lm-harness` - Model benchmarking
- And 90+ more...

</details>

<details>
<summary><b>Database (10+ skills)</b> - Schema design, optimization</summary>

- `using-neon` - Neon Serverless Postgres
- `supabase-postgres-best-practices` - Query optimization
- `database-schema-designer` - Schema design patterns

</details>

<details>
<summary><b>Document Processing (15+ skills)</b> - PDF, Word, Excel</summary>

- `pdf` - PDF manipulation and extraction
- `docx` - Word document processing
- `xlsx` - Excel spreadsheet handling
- `pptx` - PowerPoint creation

</details>

<details>
<summary><b>Problem Solving (6 skills)</b> - Creative techniques</summary>

- `when-stuck` - Dispatch to right technique when blocked ⭐
- `collision-zone-thinking` - Force unrelated concepts together
- `inversion-exercise` - Flip assumptions
- `simplification-cascades` - Find insights that eliminate complexity

</details>

<details>
<summary><b>Web Development (15+ skills)</b> - React, Shopify, SEO</summary>

- `react-best-practices` - 40+ performance rules
- `shopify-development` - Shopify apps and themes
- `segment-cdp` - Customer data platform patterns

</details>

<details>
<summary><b>Workflow Automation (15+ skills)</b> - n8n, GitHub Actions</summary>

- `n8n-*` - n8n workflow patterns and validation
- `github-workflow-automation` - GitHub Actions and CI/CD
- `inngest` - Serverless background jobs

</details>

<details>
<summary><b>Utilities (10+ skills)</b> - Browser automation, tools</summary>

- `playwright-skill` - Browser automation
- `browser-extension-builder` - Chrome/Firefox extensions
- `domain-name-brainstormer` - Domain availability checking

</details>

**[Browse full skills index →](dot_cursor/skills/INDEX.md)**

---

## 🎓 Use Cases

### Perfect For:

- **AI/ML Engineers**: 100+ skills for training, fine-tuning, inference, evaluation
- **Full-Stack Teams**: Backend, frontend, database, DevOps expertise
- **Startup Builders**: Rapid prototyping with best practices built-in
- **Solo Developers**: Access to senior-level expertise across all domains
- **Open Source Maintainers**: Code review, testing, documentation skills
- **Technical Writers**: Document processing and co-authoring workflows

### Real-World Applications:

- 🏗️ **Architecture Design**: System design with trade-off analysis
- 🐛 **Bug Fixing**: Systematic root cause analysis
- 📝 **Documentation**: Co-authoring with reader testing
- 🔧 **Refactoring**: Clean code principles and patterns
- 🚀 **Deployment**: Docker, Kubernetes, CI/CD automation
- 🧪 **Testing**: TDD, test generation, coverage analysis
- 🤖 **AI Development**: RAG, agents, fine-tuning, evaluation

---

## 📖 Documentation

### Core Documentation

- **[Rules System](docs/RULES.md)** - How the 7 core rules work (masterrule, coordinator, etc.)
- **[Architecture](docs/RULES.md#how-rules-work-together)** - System design and flow
- **[Skills Index](dot_cursor/skills/INDEX.md)** - Complete catalog of 280+ skills

### Adaptation Guides

- **[VSCode & Other IDEs](docs/OTHER_IDES.md)** - Using skills with VSCode, Continue, Cline
- **[Customization](docs/RULES.md#customizing-rules)** - Adding your own skills and rules

---

## 🔧 Advanced Features

### 1. Masterrule - Mandatory Skill Scanning

The masterrule **enforces** skill usage before every AI response:

```yaml
---
alwaysApply: true
---
# Masterrule

Before ANY response:
1. Read .cursor/skills/INDEX.md
2. Match keywords to skills
3. Load applicable SKILL.md files
4. Produce "Skill Proof" header
```

**Why it matters**: Without enforcement, AI might forget to use skills. With masterrule, expertise is **automatically** applied.

**[Learn more about masterrule →](docs/RULES.md#1-masterrule-masterrulemdc)**

### 2. Coordinator Mode - Multi-Agent Orchestration

For complex tasks (3+ work streams, multi-module changes), coordinator mode:

- Dispatches up to 4 parallel subagents
- Prevents file conflicts
- Runs spec compliance + code quality reviews
- Manages test execution and reporting

**[Learn more about coordinator mode →](docs/RULES.md#2-coordinator-mode-coordinator-modemdc)**

### 3. Auto Battle-Test Plans

Every plan is automatically validated before presentation:

- Checks 10 dimensions (consistency, edge cases, test coverage, etc.)
- Auto-revises CRITICAL/HIGH issues
- Presents only the final, clean plan

**[Learn more about battle-testing →](docs/RULES.md#3-auto-battle-test-plans-auto-battle-test-plansmdc)**

### 4. Napkin - Persistent Memory

`.cursor/napkin.md` learns across sessions:

- Records mistakes and corrections
- Remembers user preferences
- Notes what worked well
- Compounds learning over time

---

## 🔄 Using with Other IDEs

While optimized for Cursor, skills work with:

- **VSCode + GitHub Copilot** - Via workspace instructions
- **VSCode + Continue** - Via custom slash commands
- **VSCode + Cline** - Via custom instructions
- **Any AI code editor** - Manual skill invocation

**[Full adaptation guide →](docs/OTHER_IDES.md)**

### Quick VSCode Setup

```bash
# 1. Copy skills to your project
cp -r /path/to/ai-skills-engine/dot_cursor/skills .cursor/skills

# 2. Create .github/copilot-instructions.md
cat > .github/copilot-instructions.md << 'EOF'
# AI Assistant Instructions

Before responding, check .cursor/skills/INDEX.md for relevant skills.
Read and apply matching SKILL.md files.
Indicate which skills were used.
EOF

# 3. Reference skills in chat
# "@workspace Use the docker-expert skill to optimize this Dockerfile"
```

**Limitations**: No automatic enforcement (manual invocation required)

---

## 🤝 Contributing

Contributions are welcome! To add a new skill:

1. Fork this repository
2. Create your skill: `dot_cursor/skills/{category}/{skill-name}/SKILL.md`
3. Update `dot_cursor/skills/INDEX.md` to register it
4. Add examples and references
5. Submit a pull request

**[Skill creation guide →](dot_cursor/skills/development/writing-skills/SKILL.md)**

---

## 🐛 Troubleshooting

### Skills not loading?

1. Verify `.cursor/skills/INDEX.md` exists
2. Check `masterrule.mdc` is in `.cursor/rules/`
3. Restart Cursor IDE
4. Ask AI: "What skills are available?" to test

### AI not using skills?

1. Ensure your message contains relevant keywords
2. Try explicitly: "Use the docker-expert skill"
3. Check skill is registered in INDEX.md
4. Verify masterrule has `alwaysApply: true`

### Want to disable certain skills?

1. Remove from `.cursor/skills/INDEX.md`, or
2. Delete the skill directory entirely

**[Full troubleshooting guide →](docs/RULES.md#troubleshooting)**

---

## 📄 License

Apache License 2.0 - See [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Inspired by the [Cursor IDE](https://cursor.sh) agent system
- Napkin system adapted from [blader/napkin](https://github.com/blader/napkin)
- Skills curated from community best practices and expert knowledge
- Built with contributions from the AI coding community

---

## 📞 Support & Community

- **Issues**: [Open an issue](https://github.com/yourusername/ai-skills-engine/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/ai-skills-engine/discussions)
- **Updates**: Watch this repo for new skills and improvements
- **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md)

---

## ⭐ Star History

If you find this useful, please star the repository! It helps others discover these skills.

---

**Made with ❤️ for the Cursor IDE and AI coding community**

*Transform your AI assistant from helpful to expert-level*
