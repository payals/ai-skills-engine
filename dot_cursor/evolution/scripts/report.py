#!/usr/bin/env python3
"""
Self-Evolution Reporting Script

Generates comprehensive reports on evolution system effectiveness.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List


class EvolutionReporter:
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.evolution_dir = project_root / ".cursor" / "evolution"
        self.log_path = self.evolution_dir / "LOG.md"
        self.config_path = self.evolution_dir / "config.json"
        
    def load_config(self) -> dict:
        if self.config_path.exists():
            with open(self.config_path) as f:
                return json.load(f)
        return {}
    
    def parse_log(self) -> List[Dict[str, any]]:
        """Parse LOG.md into structured events."""
        if not self.log_path.exists():
            return []
        
        content = self.log_path.read_text()
        events = []
        
        # Simple parsing: split by ## headers
        sections = content.split("\n## ")
        for section in sections[1:]:  # Skip header
            lines = section.split("\n")
            if lines:
                title_line = lines[0]
                # Extract date if present
                if title_line.startswith("["):
                    date_str = title_line.split("]")[0][1:]
                    event_type = title_line.split("] - ")[1] if "] - " in title_line else "Unknown"
                    
                    events.append({
                        "date": date_str,
                        "type": event_type,
                        "content": "\n".join(lines[1:])
                    })
        
        return events
    
    def count_proposals(self) -> Dict[str, int]:
        """Count proposals by status."""
        proposals_dir = self.evolution_dir / "proposals"
        if not proposals_dir.exists():
            return {"total": 0, "accepted": 0, "rejected": 0, "pending": 0}
        
        proposals = list(proposals_dir.glob("*.md"))
        
        counts = {
            "total": len(proposals),
            "accepted": 0,
            "rejected": 0,
            "pending": 0
        }
        
        for proposal_path in proposals:
            content = proposal_path.read_text()
            if "Status: ACCEPTED" in content or "Status: IMPLEMENTED" in content:
                counts["accepted"] += 1
            elif "Status: REJECTED" in content:
                counts["rejected"] += 1
            else:
                counts["pending"] += 1
        
        return counts
    
    def count_tracking(self) -> Dict[str, int]:
        """Count effectiveness tracking by status."""
        tracking_dir = self.evolution_dir / "tracking"
        if not tracking_dir.exists():
            return {"total": 0, "success": 0, "partial": 0, "failed": 0, "monitoring": 0}
        
        tracking_files = list(tracking_dir.glob("*.md"))
        
        counts = {
            "total": len(tracking_files),
            "success": 0,
            "partial": 0,
            "failed": 0,
            "monitoring": 0
        }
        
        for tracking_path in tracking_files:
            content = tracking_path.read_text()
            if "Status: SUCCESS" in content:
                counts["success"] += 1
            elif "Status: PARTIAL" in content:
                counts["partial"] += 1
            elif "Status: FAILED" in content:
                counts["failed"] += 1
            else:
                counts["monitoring"] += 1
        
        return counts
    
    def generate_report(self, date_range: int = 30) -> str:
        """Generate comprehensive evolution report."""
        config = self.load_config()
        events = self.parse_log()
        proposals = self.count_proposals()
        tracking = self.count_tracking()
        
        report = [
            "# Self-Evolution System Report",
            f"\n**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"**Date Range**: Last {date_range} days",
            f"**System Status**: {'ENABLED' if config.get('enabled') else 'DISABLED'}",
            "\n---\n"
        ]
        
        # Summary Statistics
        report.append("\n## Summary Statistics\n")
        report.append(f"- **Total Proposals**: {proposals['total']}")
        report.append(f"  - Accepted: {proposals['accepted']}")
        report.append(f"  - Rejected: {proposals['rejected']}")
        report.append(f"  - Pending: {proposals['pending']}")
        report.append(f"\n- **Effectiveness Tracking**: {tracking['total']} changes tracked")
        report.append(f"  - Success: {tracking['success']}")
        report.append(f"  - Partial: {tracking['partial']}")
        report.append(f"  - Failed: {tracking['failed']}")
        report.append(f"  - Monitoring: {tracking['monitoring']}")
        
        if proposals['total'] > 0:
            success_rate = (proposals['accepted'] / proposals['total']) * 100
            report.append(f"\n- **Acceptance Rate**: {success_rate:.1f}%")
        
        if tracking['total'] > 0:
            effectiveness_rate = (tracking['success'] / tracking['total']) * 100
            report.append(f"- **Effectiveness Rate**: {effectiveness_rate:.1f}%")
        
        # Recent Events
        report.append("\n\n## Recent Events\n")
        if events:
            recent_events = events[-10:]  # Last 10 events
            for event in reversed(recent_events):
                report.append(f"\n### [{event['date']}] {event['type']}")
                # Show first 200 chars of content
                preview = event['content'][:200].strip()
                if preview:
                    report.append(f"{preview}...")
        else:
            report.append("No events recorded yet.\n")
        
        # Configuration
        report.append("\n\n## Current Configuration\n")
        report.append(f"- **Mode**: {config.get('mode', 'passive')}")
        report.append(f"- **Auto-implement**: {config.get('auto_implement', False)}")
        report.append(f"- **Require approval**: {config.get('require_user_approval', True)}")
        report.append(f"- **Monitoring period**: {config.get('monitoring_period_days', 7)} days")
        report.append(f"- **Min pattern frequency**: {config.get('min_pattern_frequency', 3)}")
        report.append(f"- **Pattern lookback**: {config.get('pattern_lookback_days', 30)} days")
        
        # Recommendations
        report.append("\n\n## Recommendations\n")
        
        if not config.get('enabled'):
            report.append("- ⚠️  System is currently disabled. Enable to start pattern analysis.")
        
        if proposals['pending'] > 0:
            report.append(f"- 📋 You have {proposals['pending']} pending proposals to review.")
        
        if tracking['monitoring'] > 0:
            report.append(f"- 🔍 {tracking['monitoring']} changes are currently being monitored.")
        
        if tracking['failed'] > 0:
            report.append(f"- ⚠️  {tracking['failed']} changes failed effectiveness review. Consider rollback.")
        
        if proposals['total'] == 0:
            report.append("- 💡 No proposals generated yet. System needs more data from napkin/tracker.")
        
        return "\n".join(report)
    
    def list_pending_proposals(self) -> str:
        """List all pending proposals."""
        proposals_dir = self.evolution_dir / "proposals"
        if not proposals_dir.exists():
            return "No proposals directory found."
        
        proposals = list(proposals_dir.glob("*.md"))
        pending = []
        
        for proposal_path in proposals:
            content = proposal_path.read_text()
            if "Status: ACCEPTED" not in content and "Status: REJECTED" not in content:
                # Extract title
                lines = content.split("\n")
                title = "Untitled"
                for line in lines:
                    if line.startswith("## Self-Evolution Proposal:"):
                        title = line.replace("## Self-Evolution Proposal:", "").strip()
                        break
                
                pending.append({
                    "file": proposal_path.name,
                    "title": title,
                    "path": proposal_path
                })
        
        if not pending:
            return "No pending proposals."
        
        output = ["# Pending Proposals\n"]
        for i, proposal in enumerate(pending, 1):
            output.append(f"{i}. **{proposal['title']}**")
            output.append(f"   File: {proposal['file']}")
            output.append(f"   Path: {proposal['path']}\n")
        
        return "\n".join(output)


def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: report.py <project_root> [--pending]")
        sys.exit(1)
    
    project_root = Path(sys.argv[1])
    reporter = EvolutionReporter(project_root)
    
    if "--pending" in sys.argv:
        output = reporter.list_pending_proposals()
    else:
        output = reporter.generate_report()
    
    print(output)
    
    # Save report
    reports_dir = project_root / ".cursor" / "evolution" / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M")
    report_type = "pending" if "--pending" in sys.argv else "summary"
    report_path = reports_dir / f"{report_type}-{timestamp}.md"
    report_path.write_text(output)
    
    print(f"\n\nReport saved to: {report_path}")


if __name__ == "__main__":
    main()
