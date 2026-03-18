# Napkin — Persistent Session Memory

Adapted from [blader/napkin](https://github.com/blader/napkin). This file tracks mistakes, corrections, surprises, and preferences across sessions. Read it before working; update it when something noteworthy happens.

---

## My Mistakes

<!-- Agent errors: wrong assumptions, bad approaches, failed commands -->
- 2026-03-18 Phase 3 used PG 17 as "latest stable" throughout all generated files; user corrected that PG 18 (released Sept 2025) is the current latest. Always verify PostgreSQL latest version against current date before generating architecture docs.


## User Corrections

<!-- Things the user told me to do differently -->



## Repo Surprises

<!-- Non-obvious things about this codebase that tripped me up -->



## Preferences

<!-- How the user likes things done — style, workflow, communication -->



## What Worked

<!-- Successful approaches worth repeating -->
- 2026-03-18 Phase 4: Dispatching 3 parallel subagents for row responses (one per section group) completed all 39 files efficiently without context window issues.
- 2026-03-18 Phase 4: Pre-reading all solution drafts via explore subagent before dispatching writers gave writers complete context without needing to read files themselves.
- 2026-03-18 Phase 4: REPLACE strategy was correct — prior supplemental docs had phantom section numbers (1_11, 4_11) from a different CSV iteration.
- 2026-03-18 Phase 6: Writing a Python compilation script (compile_responses.py) to parse all 39 row response files was far more reliable than reading files manually. Regex-based parsing of the standardized format worked on first attempt.
- 2026-03-18 Phase 6: Shell subagent_type="shell" Task tool calls failed with "Required tool READ not found" — handle file operations directly in coordinator instead.
- 2026-03-18 Phase 6: The existing convert_supplementals_to_pdf.py script with pandoc+weasyprint fallback worked perfectly — all 25 PDFs generated in ~27 seconds.
- 2026-03-18 Phase 6 PDF fix: pandoc --pdf-engine=weasyprint with --css flag does NOT reliably apply image sizing CSS. The fix was to bypass pandoc's PDF engine entirely: pandoc converts MD→HTML, then weasyprint Python API renders HTML→PDF with CSS embedded in the HTML `<style>` tag. This gives full CSS control.
- 2026-03-18 Phase 6 PDF fix: Mermaid-rendered PNGs are often very tall (692x2652px = 26.8 inches at page width). Without `max-height: 7.5in`, they overflow across multiple pages creating blank pages. Both `max-width: 100%` AND `max-height: 7.5in` with `object-fit: contain` are needed.
- 2026-03-18 Phase 6 PDF fix: PyPDF2 page.extract_text() returns 0 lines for pages that contain only images — useful for detecting "blank" pages that are actually image overflow.


