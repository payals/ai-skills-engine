#!/usr/bin/env python3
"""
Self-Evolution Pattern Analysis Script

Analyzes napkin.md and TRACKER.md to detect patterns and generate improvement proposals.
"""

import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Tuple


class EvolutionAnalyzer:
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.cursor_dir = project_root / ".cursor"
        self.evolution_dir = self.cursor_dir / "evolution"
        self.config = self._load_config()
        
    def _load_config(self) -> dict:
        config_path = self.evolution_dir / "config.json"
        if config_path.exists():
            with open(config_path) as f:
                return json.load(f)
        return {}
    
    def analyze_napkin(self) -> Dict[str, List[Tuple[str, str]]]:
        """Parse napkin.md and extract categorized entries."""
        napkin_path = self.project_root / ".cursor" / "napkin.md"
        if not napkin_path.exists():
            return {}
        
        content = napkin_path.read_text()
        
        # Extract sections
        sections = {
            "mistakes": [],
            "corrections": [],
            "surprises": [],
            "preferences": [],
            "what_worked": []
        }
        
        current_section = None
        section_markers = {
            "## My Mistakes": "mistakes",
            "## User Corrections": "corrections",
            "## Repo Surprises": "surprises",
            "## Preferences": "preferences",
            "## What Worked": "what_worked"
        }
        
        for line in content.split("\n"):
            # Check for section headers
            for marker, section_name in section_markers.items():
                if line.startswith(marker):
                    current_section = section_name
                    break
            
            # Extract dated entries
            if current_section and line.startswith("- "):
                match = re.match(r"- (\d{4}-\d{2}-\d{2}) (.+)", line)
                if match:
                    date_str, entry = match.groups()
                    sections[current_section].append((date_str, entry))
        
        return sections
    
    def analyze_tracker(self) -> List[Dict[str, str]]:
        """Parse TRACKER.md and extract entries."""
        tracker_paths = [
            self.project_root / "TRACKER.md",
            self.project_root / "docs" / "tracker.md",
            self.project_root / "docs" / "TRACKER.md"
        ]
        
        for tracker_path in tracker_paths:
            if tracker_path.exists():
                return self._parse_tracker(tracker_path)
        
        return []
    
    def _parse_tracker(self, path: Path) -> List[Dict[str, str]]:
        """Parse tracker file into structured entries."""
        content = path.read_text()
        entries = []
        
        # Match tracker entries (## [YYYY-MM-DD] - Title format)
        entry_pattern = r"## \[(\d{4}-\d{2}-\d{2})\] - (.+?)(?=\n## \[|\Z)"
        matches = re.finditer(entry_pattern, content, re.DOTALL)
        
        for match in matches:
            date_str, entry_content = match.groups()
            entries.append({
                "date": date_str,
                "content": entry_content.strip()
            })
        
        return entries
    
    def detect_patterns(self) -> Dict[str, any]:
        """Detect patterns in napkin and tracker data."""
        napkin_data = self.analyze_napkin()
        tracker_data = self.analyze_tracker()
        
        lookback_days = self.config.get("pattern_lookback_days", 30)
        cutoff_date = datetime.now() - timedelta(days=lookback_days)
        
        patterns = {
            "repeated_mistakes": self._find_repeated_patterns(
                napkin_data.get("mistakes", []), cutoff_date
            ),
            "successful_approaches": self._find_repeated_patterns(
                napkin_data.get("what_worked", []), cutoff_date
            ),
            "user_corrections": self._analyze_corrections(
                napkin_data.get("corrections", []), cutoff_date
            ),
            "workflow_patterns": self._analyze_workflows(tracker_data, cutoff_date),
            "knowledge_gaps": self._detect_gaps(napkin_data, cutoff_date),
            "rule_violations": self._detect_rule_violations(napkin_data, cutoff_date)
        }
        
        return patterns
    
    def _find_repeated_patterns(
        self, entries: List[Tuple[str, str]], cutoff_date: datetime
    ) -> List[Dict[str, any]]:
        """Find patterns that repeat multiple times."""
        min_frequency = self.config.get("min_pattern_frequency", 3)
        
        # Filter by date
        recent_entries = [
            (date_str, entry) for date_str, entry in entries
            if datetime.strptime(date_str, "%Y-%m-%d") >= cutoff_date
        ]
        
        # Extract keywords and find common themes
        keyword_counts = Counter()
        entry_by_keyword = defaultdict(list)
        
        for date_str, entry in recent_entries:
            # Extract meaningful keywords (simple approach)
            words = re.findall(r'\b[A-Z][a-z]+\b|\b[a-z]{4,}\b', entry)
            for word in words:
                if word.lower() not in ['this', 'that', 'with', 'from', 'have']:
                    keyword_counts[word.lower()] += 1
                    entry_by_keyword[word.lower()].append((date_str, entry))
        
        # Find patterns that meet minimum frequency
        patterns = []
        for keyword, count in keyword_counts.most_common():
            if count >= min_frequency:
                patterns.append({
                    "keyword": keyword,
                    "frequency": count,
                    "entries": entry_by_keyword[keyword]
                })
        
        return patterns[:10]  # Top 10 patterns
    
    def _analyze_corrections(
        self, entries: List[Tuple[str, str]], cutoff_date: datetime
    ) -> List[Dict[str, any]]:
        """Analyze user corrections to identify behavior patterns."""
        recent_entries = [
            (date_str, entry) for date_str, entry in entries
            if datetime.strptime(date_str, "%Y-%m-%d") >= cutoff_date
        ]
        
        corrections = []
        for date_str, entry in recent_entries:
            corrections.append({
                "date": date_str,
                "correction": entry,
                "category": self._categorize_correction(entry)
            })
        
        return corrections
    
    def _categorize_correction(self, entry: str) -> str:
        """Categorize a correction by type."""
        entry_lower = entry.lower()
        
        if any(word in entry_lower for word in ["version", "latest", "current"]):
            return "version_awareness"
        elif any(word in entry_lower for word in ["test", "verify", "check"]):
            return "verification"
        elif any(word in entry_lower for word in ["format", "style", "convention"]):
            return "style_convention"
        elif any(word in entry_lower for word in ["read", "check", "look"]):
            return "information_gathering"
        else:
            return "other"
    
    def _analyze_workflows(
        self, entries: List[Dict[str, str]], cutoff_date: datetime
    ) -> List[Dict[str, any]]:
        """Analyze tracker entries for workflow patterns."""
        recent_entries = [
            entry for entry in entries
            if datetime.strptime(entry["date"], "%Y-%m-%d") >= cutoff_date
        ]
        
        # Look for repeated multi-step workflows
        workflows = []
        for entry in recent_entries:
            content = entry["content"]
            # Count steps (lines starting with -, *, or numbers)
            steps = re.findall(r'^\s*[-*\d]+\.?\s+.+$', content, re.MULTILINE)
            if len(steps) >= 3:
                workflows.append({
                    "date": entry["date"],
                    "steps": len(steps),
                    "content_preview": content[:200]
                })
        
        return workflows
    
    def _detect_gaps(
        self, napkin_data: Dict[str, List[Tuple[str, str]]], cutoff_date: datetime
    ) -> List[str]:
        """Detect knowledge gaps (problems without solutions)."""
        mistakes = napkin_data.get("mistakes", [])
        surprises = napkin_data.get("surprises", [])
        
        recent_issues = []
        for date_str, entry in mistakes + surprises:
            if datetime.strptime(date_str, "%Y-%m-%d") >= cutoff_date:
                recent_issues.append(entry)
        
        # Simple gap detection: issues that don't have corresponding "what worked"
        gaps = []
        what_worked = [entry for _, entry in napkin_data.get("what_worked", [])]
        
        for issue in recent_issues:
            # Check if there's a related solution
            has_solution = any(
                self._text_similarity(issue, solution) > 0.3
                for solution in what_worked
            )
            if not has_solution:
                gaps.append(issue)
        
        return gaps[:5]  # Top 5 gaps
    
    def _detect_rule_violations(
        self, napkin_data: Dict[str, List[Tuple[str, str]]], cutoff_date: datetime
    ) -> List[Dict[str, any]]:
        """Detect potential rule violations from mistakes."""
        mistakes = napkin_data.get("mistakes", [])
        
        violations = []
        rule_keywords = ["should", "must", "always", "never", "required"]
        
        for date_str, entry in mistakes:
            if datetime.strptime(date_str, "%Y-%m-%d") >= cutoff_date:
                if any(keyword in entry.lower() for keyword in rule_keywords):
                    violations.append({
                        "date": date_str,
                        "entry": entry,
                        "potential_rule": self._extract_rule_from_mistake(entry)
                    })
        
        return violations
    
    def _extract_rule_from_mistake(self, entry: str) -> str:
        """Extract a potential rule from a mistake entry."""
        # Simple extraction: convert mistake to preventive rule
        if "used" in entry.lower() or "assumed" in entry.lower():
            return f"Always verify before {entry.split('used')[0] if 'used' in entry else entry.split('assumed')[0]}"
        return f"Prevent: {entry[:100]}"
    
    def _text_similarity(self, text1: str, text2: str) -> float:
        """Simple text similarity based on common words."""
        words1 = set(re.findall(r'\b\w+\b', text1.lower()))
        words2 = set(re.findall(r'\b\w+\b', text2.lower()))
        
        if not words1 or not words2:
            return 0.0
        
        intersection = words1 & words2
        union = words1 | words2
        
        return len(intersection) / len(union)
    
    def generate_report(self) -> str:
        """Generate a human-readable analysis report."""
        patterns = self.detect_patterns()
        
        report = [
            "# Self-Evolution Pattern Analysis Report",
            f"\n**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"**Lookback Period**: {self.config.get('pattern_lookback_days', 30)} days",
            "\n---\n"
        ]
        
        # Repeated Mistakes
        report.append("\n## Repeated Mistakes\n")
        repeated = patterns["repeated_mistakes"]
        if repeated:
            for i, pattern in enumerate(repeated[:5], 1):
                report.append(f"\n### {i}. {pattern['keyword'].title()} ({pattern['frequency']} occurrences)")
                for date_str, entry in pattern['entries'][:2]:
                    report.append(f"- [{date_str}] {entry[:100]}...")
        else:
            report.append("No repeated mistakes detected.\n")
        
        # Successful Approaches
        report.append("\n## Successful Approaches\n")
        successful = patterns["successful_approaches"]
        if successful:
            for i, pattern in enumerate(successful[:5], 1):
                report.append(f"\n### {i}. {pattern['keyword'].title()} ({pattern['frequency']} occurrences)")
                for date_str, entry in pattern['entries'][:2]:
                    report.append(f"- [{date_str}] {entry[:100]}...")
        else:
            report.append("No repeated successful approaches detected.\n")
        
        # User Corrections
        report.append("\n## User Corrections\n")
        corrections = patterns["user_corrections"]
        if corrections:
            by_category = defaultdict(list)
            for correction in corrections:
                by_category[correction["category"]].append(correction)
            
            for category, items in by_category.items():
                report.append(f"\n### {category.replace('_', ' ').title()} ({len(items)} corrections)")
                for item in items[:2]:
                    report.append(f"- [{item['date']}] {item['correction'][:100]}...")
        else:
            report.append("No user corrections in this period.\n")
        
        # Knowledge Gaps
        report.append("\n## Knowledge Gaps\n")
        gaps = patterns["knowledge_gaps"]
        if gaps:
            for i, gap in enumerate(gaps, 1):
                report.append(f"{i}. {gap[:150]}...")
        else:
            report.append("No significant knowledge gaps detected.\n")
        
        # Rule Violations
        report.append("\n## Potential Rule Violations\n")
        violations = patterns["rule_violations"]
        if violations:
            for violation in violations[:3]:
                report.append(f"\n- **[{violation['date']}]** {violation['entry']}")
                report.append(f"  - *Suggested rule*: {violation['potential_rule']}")
        else:
            report.append("No rule violations detected.\n")
        
        # Workflow Patterns
        report.append("\n## Workflow Patterns\n")
        workflows = patterns["workflow_patterns"]
        if workflows:
            report.append(f"Detected {len(workflows)} multi-step workflows (3+ steps)")
            for workflow in workflows[:3]:
                report.append(f"- [{workflow['date']}] {workflow['steps']} steps")
        else:
            report.append("No significant workflow patterns detected.\n")
        
        return "\n".join(report)


def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: analyze.py <project_root>")
        sys.exit(1)
    
    project_root = Path(sys.argv[1])
    analyzer = EvolutionAnalyzer(project_root)
    
    report = analyzer.generate_report()
    print(report)
    
    # Save report
    reports_dir = project_root / ".cursor" / "evolution" / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M")
    report_path = reports_dir / f"analysis-{timestamp}.md"
    report_path.write_text(report)
    
    print(f"\n\nReport saved to: {report_path}")


if __name__ == "__main__":
    main()
