# Attributions

This project combines original custom work with skills sourced from the broader Cursor/Claude community. This document provides proper attribution for all sourced materials and highlights our custom contributions.

## Custom Skills & Rules (Original Work)

All custom work in this repository is licensed under Apache 2.0.

### Custom Rules (8 rules - all custom)

All rules in `.cursor/rules/` are original creations for this project:

1. **`masterrule.mdc`** - Mandatory skill scanning protocol with "Skill Proof" enforcement
2. **`coordinator-mode.mdc`** - Multi-agent orchestration system with 6-phase protocol (ASSESS → PLAN → DISPATCH → MONITOR → VERIFY → ACCEPT)
3. **`auto-battle-test-plans.mdc`** - Automatic plan validation with 10-point checklist and auto-revision
4. **`anti-hang-subagents.mdc`** - Context exhaustion prevention with batching rules and prompt size limits
5. **`tracker-maintenance.mdc`** - Project history protocol for persistent work tracking
6. **`auto-execute-plans.mdc`** - Plan execution trigger with mandatory skill loading
7. **`pipeline-execution.mdc`** - RFP pipeline mode with agent impersonation
8. **`auto-docs-audit.mdc`** - Documentation maintenance with code-to-diagram mapping

**Note**: The napkin system in `masterrule.mdc` is adapted from [blader/napkin](https://github.com/blader/napkin).

### Custom & Customized Skills (~35-45 skills)

### Fully Custom (Original Work)

#### Core Workflow Skills

- **`project-tracker`** ⭐ - Persistent project history journal with tracker file maintenance protocol
- **`pipeline-evolution`** ⭐ - Self-improving pipeline system that harvests insights and promotes them to control plane
- **`verification-before-completion`** ⭐ - Evidence-before-claims protocol with "Iron Law" of verification
- **`executing-plans`** ⭐ - Batch execution with checkpoints and architect review
- **`writing-plans`** ⭐ - Comprehensive implementation plans with TDD focus
- **`feature-design-assistant`** ⭐ - Natural collaborative dialogue for feature planning
- **`git-commit`** ⭐ - Conventional commit message automation
- **`dispatching-parallel-agents`** ⭐ - Parallel task orchestration
- **`test-fixing`** ⭐ - Systematic test failure resolution
- **`using-git-worktrees`** ⭐ - Isolated workspace creation for feature work

#### Problem-Solving Skills

- **`when-stuck`** ⭐ - Dispatcher to problem-solving techniques based on stuck type
- **`collision-zone-thinking`** ⭐ - Force unrelated concepts together for emergent properties
- **`inversion-exercise`** ⭐ - Flip core assumptions to reveal hidden constraints
- **`meta-pattern-recognition`** ⭐ - Spot patterns appearing across 3+ domains
- **`scale-game`** ⭐ - Test at extremes (1000x bigger/smaller) to expose fundamental truths
- **`simplification-cascades`** ⭐ - Find one insight that eliminates multiple components

#### Development Skills

- **`create-plan`** ⭐ - Concise plan creation for coding tasks
- **`clean-code`** ⭐ - Pragmatic coding standards without over-engineering
- **`code-review-checklist`** ⭐ - Comprehensive review checklist
- **`database-design`** ⭐ - Database design principles and decision-making
- **`software-architecture`** ⭐ - Quality-focused architecture guide
- **`test-driven-development`** ⭐ - TDD workflow and patterns
- **`testing-patterns`** ⭐ - Jest testing patterns and factory functions

#### Specialized Skills

- **`holistic-bug-analysis`** ⭐ - Multi-level bug analysis (symptom vs root cause)
- **`holistic-testing`** ⭐ - Behavioral testing with fixture files
- **`codebase-maintenance`** ⭐ - Systematic codebase cleanup
- **`db-cheatsheet`** ⭐ - Database schema reference
- **`subagent-driven-development`** ⭐ - Implementation with independent tasks

### Customized (Adapted from Community Sources)

These skills may have originated from common Cursor/Claude skill repositories but have been modified or extended for this project:

- **`brainstorming`** 🔧 - Idea-to-design dialogue (customized with YAGNI enforcement and git-worktree integration)
- **`using-superpowers`** 🔧 - Skill discovery protocol (appears in community, may be customized)

**Legend**:
- ⭐ = Fully custom (original work)
- 🔧 = Customized (adapted from community sources)

See [docs/CUSTOM_SKILLS.md](docs/CUSTOM_SKILLS.md) for detailed documentation of each custom skill and rule.

### Custom Workflows

- **[cursor-prompt-queue](https://github.com/payals/cursor-prompt-queue)** - Batch sequential prompts with dynamic variable passing between steps. Fresh context per step without context rot.

## Sourced Skills

### vibeship-spawner-skills (Apache 2.0)

Source: https://github.com/vibeship/spawner-skills

AI research and agent development skills (~15-20 skills):

- **Agent Frameworks**: `crewai`, `langgraph`, `langfuse`
- **RAG & Memory**: `rag-implementation`, `rag-engineer`, `conversation-memory`, `agent-memory-systems`
- **Agent Design**: `ai-agents-architect`, `agent-tool-builder`, `autonomous-agents`
- **Prompt Engineering**: `prompt-engineer`, `prompt-engineering`

### Orchestra Research

AI/ML research skills covering the full ML lifecycle (~80-90 skills):

#### Distributed Training
- `deepspeed`, `pytorch-fsdp`, `megatron-core`, `accelerate`, `pytorch-lightning`, `ray-train`, `torchtitan`

#### Fine-Tuning
- `axolotl`, `llama-factory`, `peft`, `unsloth`, `litgpt`

#### Inference & Serving
- `vllm`, `sglang`, `tensorrt-llm`, `llama-cpp`

#### Post-Training & RLHF
- `trl-fine-tuning`, `grpo-rl-training`, `openrlhf`, `verl`, `miles`, `slime`, `torchforge`, `simpo`

#### Optimization & Quantization
- `flash-attention`, `awq`, `gptq`, `bitsandbytes`, `gguf`, `hqq`

#### Multimodal Models
- `whisper`, `clip`, `llava`, `stable-diffusion`, `blip-2`, `segment-anything`, `audiocraft`

#### Evaluation & Benchmarking
- `lm-evaluation-harness`, `bigcode-evaluation-harness`, `nemo-evaluator`, `agent-evaluation`

#### MLOps & Observability
- `mlflow`, `weights-and-biases`, `tensorboard`, `langsmith`, `phoenix`

#### RAG & Vector Databases
- `chroma`, `faiss`, `pinecone`, `qdrant`, `sentence-transformers`

#### Safety & Alignment
- `constitutional-ai`, `llamaguard`, `nemo-guardrails`

#### Mechanistic Interpretability
- `transformer-lens`, `saelens`, `nnsight`, `pyvene`

#### Model Architectures
- `nanogpt`, `mamba`, `rwkv`

#### Emerging Techniques
- `knowledge-distillation`, `long-context`, `model-merging`, `model-pruning`, `moe-training`, `speculative-decoding`

#### Data Processing
- `nemo-curator`, `ray-data`

#### Infrastructure
- `modal`, `lambda-labs`, `skypilot`

### Anthropic

Document processing skills with MCP integration:

- `docx`, `docx-official`, `docx-anthropic` - Word document manipulation
- `pptx`, `pptx-official` - PowerPoint presentation creation
- `pdf`, `pdf-official`, `pdf-anthropic` - PDF processing and form filling
- `xlsx`, `xlsx-official` - Excel spreadsheet manipulation

### Vercel Engineering (MIT)

- `react-best-practices` - React and Next.js performance optimization with 40+ rules

Source: Vercel Engineering team

### Supabase

- `supabase-postgres-best-practices` - Postgres performance optimization and best practices

Source: Supabase team

### Microsoft GitHub

- `github-workflow-automation` - GitHub workflows, PR reviews, and CI/CD integration

### Community & Other Sources

#### Senior Development Skills
- `senior-backend`, `senior-frontend`, `senior-fullstack`, `senior-architect`
- `senior-devops`, `senior-security`, `senior-secops`
- `senior-data-engineer`, `senior-data-scientist`, `senior-ml-engineer`
- `senior-qa`, `senior-prompt-engineer`

#### Development Tools
- `docker-expert`, `devops-iac-engineer`, `error-resolver`
- `code-reviewer`, `database-schema-designer`

#### Web Development
- `shopify-apps`, `shopify-development` - Shopify app development patterns
- `segment-cdp` - Segment Customer Data Platform patterns
- `upstash-qstash`, `trigger-dev`, `inngest` - Serverless job queues and workflows
- `web-performance-optimization`, `roier-seo`

#### Workflow Automation
- n8n skills: `n8n-code-javascript`, `n8n-code-python`, `n8n-expression-syntax`, `n8n-mcp-tools-expert`, `n8n-node-configuration`, `n8n-validation-expert`, `n8n-workflow-patterns`
- `zapier-make-patterns`, `planning-with-files`

#### Utilities
- `playwright-skill`, `browser-automation`, `browser-extension-builder`
- `web-artifacts-builder`, `domain-name-brainstormer`
- `pdf-processing`, `pdf-processing-pro`
- `obsidian-markdown`, `obsidian-bases`, `json-canvas`
- `doc-coauthoring`, `documentation-templates`

#### Research & Analysis
- `research-engineer`, `ml-paper-writing`

#### Search & Data
- `exa-search`, `tavily-web`, `firecrawl-scraper`, `blockrun`, `perplexity`
- `context7-auto-research`

#### Specialized
- `qa-test-planner`, `gemini`, `gepetto`, `jira`, `datadog-cli`
- `geo-fundamentals`, `network-101`, `busybox-on-windows`
- `using-superpowers` - Skill discovery protocol (likely Anthropic/community source, needs attribution research)

## License Compliance

- **Custom work**: Apache 2.0
- **Sourced skills**: Retain original licenses where specified
- **Community skills**: Assumed permissive use; proper attribution added where known

## Contributing Attribution

If you identify the source of any unattributed skills or find attribution errors, please:

1. Open an issue with the skill name and correct attribution
2. Submit a PR updating the skill's YAML frontmatter and this file
3. Include links to source repositories when available

## Acknowledgments

Special thanks to:

- **Anthropic** - For Claude and document processing skills
- **Microsoft** - For Cursor IDE and GitHub integration skills
- **vibeship** - For spawner-skills collection
- **Orchestra Research** - For comprehensive AI/ML research skills
- **Vercel, Supabase, and the broader community** - For domain-specific expertise
- **blader** - For the napkin persistent memory pattern

This project stands on the shoulders of giants. We're grateful to the entire Cursor/Claude community for building and sharing these skills.
