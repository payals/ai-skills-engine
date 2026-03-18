# Changelog

All notable changes to the AI Skills Engine project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

#### Self-Evolution System
- **Automated improvement workflow** that learns from napkin and tracker to evolve rules, skills, and workflows
- **Pattern recognition engine** (`analyze.py`) - Detects repeated mistakes, successful approaches, and workflow patterns
- **Proposal generation** with impact analysis and scoring (Value, Risk, Effort, Confidence)
- **Safe implementation** with automatic backups and effectiveness tracking
- **Rollback support** for failed changes
- **Configuration system** (`config.json`) with customizable thresholds and settings
- **Management scripts**:
  - `enable.sh` / `disable.sh` - System activation
  - `analyze.py` - Pattern analysis
  - `report.py` - Status and effectiveness reports
- **Git hook example** (`post-commit.sample`) for automatic analysis
- **Comprehensive documentation** in `docs/SELF_EVOLUTION.md`
- **Template files** for proposals and tracking
- **Disabled by default** - Opt-in system with full safety controls

## [1.0.0] - 2026-03-18

### Added

#### Initial Release - Comprehensive Skills System
- Transform minimal README into full-featured documentation
- Add architecture overview, quick start guide, and examples
- Document 227 skills across 10 categories
- Include installation instructions for Cursor and other IDEs
- Add troubleshooting, contributing guidelines, and use cases
- Add untracked `docs/` and `dot_cursor/` directories with skills and rules
- 7 core custom rules (masterrule, coordinator-mode, auto-battle-test-plans, anti-hang-subagents, auto-execute-plans, auto-docs-audit, pipeline-execution)
- ~30-40 fully custom skills across development, problem-solving, and specialized categories
- Integration with 280+ sourced skills from vibeship, Orchestra Research, Anthropic, and community

#### Attribution & Documentation
- Comprehensive `ATTRIBUTIONS.md` crediting all sources (vibeship, Orchestra Research, Anthropic, Vercel, Supabase, Microsoft, community)
- `docs/CUSTOM_SKILLS.md` with detailed documentation of 8 custom rules and ~40-50 custom skills
- Custom Skills & Workflows section in README
- Attributions section in README with full credits and acknowledgments
- Integration of cursor-prompt-queue workflow documentation

#### Project Tracker System
- New `project-tracker` skill in `.cursor/skills/development/project-tracker/`
  - `SKILL.md` - Main skill documentation (280 lines)
  - `templates/tracker_template.md` - Example tracker structure with 4 sample entries
  - `examples.md` - 7 real-world usage scenarios
- New `tracker-maintenance.mdc` rule in `.cursor/rules/`
  - Enforces reading tracker before substantial work
  - Enforces updating tracker after meaningful completion
  - Anti-hang safeguards
  - Integration with project-tracker skill
- Documentation of tracker system in README with example entry
- Rule #8 documentation in `docs/RULES.md`

#### Documentation Improvements
- Design philosophy section in CUSTOM_SKILLS.md (enforcement + guidance, fresh context, evidence-based, self-improvement)
- Integration map showing how custom rules and skills work together
- Contributing guidelines for custom skills/rules
- Updated Rules badge count from 7 to 8

### Changed
- Transformed minimal README into comprehensive documentation (280+ skills documented)
- Updated README Table of Contents to include Custom Skills & Workflows and Attributions
- Updated `docs/RULES.md` integration diagram to include tracker-maintenance
- Enhanced What is This section in README to mention Project Tracker and Prompt Queue
- Updated .gitignore to exclude .cursor/ directory

### Technical Details
- All YAML frontmatter validated
- All internal documentation links verified
- No sensitive files in repository
- Full license compliance ensured
- Clear distinction between fully custom ⭐ and customized 🔧 skills

### Repository Structure
- `dot_cursor/` - Skills and rules for Cursor IDE
  - `dot_cursor/skills/` - 280+ skills across 12 categories
  - `dot_cursor/rules/` - 8 custom rules (now `.cursor/rules/` in projects)
- `docs/` - Comprehensive documentation
  - Architecture, rules, custom skills, IDE adaptation guides
- `ATTRIBUTIONS.md` - Full source credits and license compliance
- `CHANGELOG.md` - Version history
- `README.md` - Complete overview and quick start

## [Unreleased]

### Planned
- Architecture diagram visualization
- Video walkthrough of custom features
- Additional problem-solving techniques
- More domain-specific skills
- Community skill submission process

---

## Version History

- **v1.0.0** (2026-03-18) - Initial Release
  - Comprehensive skills system with 227 skills
  - 8 custom rules for AI agent orchestration
  - ~30-40 fully custom skills + ~5-10 customized skills
  - Full attribution and documentation
  - Project tracker system for persistent history
  - Integration with cursor-prompt-queue workflow

---

## Attribution

This project combines original custom work with skills sourced from:
- vibeship-spawner-skills (Apache 2.0)
- Orchestra Research
- Anthropic
- Vercel Engineering (MIT)
- Supabase
- Microsoft GitHub
- Community contributions

See [ATTRIBUTIONS.md](ATTRIBUTIONS.md) for complete attribution details.

## License

Apache License 2.0 - See [LICENSE](LICENSE) file for details.
