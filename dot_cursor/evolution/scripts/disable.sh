#!/bin/bash
# Disable self-evolution system

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
EVOLUTION_DIR="$PROJECT_ROOT/.cursor/evolution"
RULE_FILE="$PROJECT_ROOT/.cursor/rules/self-evolution.mdc"
CONFIG_FILE="$EVOLUTION_DIR/config.json"

echo "🧬 Disabling Self-Evolution System..."
echo ""

# Update config.json to disable
echo "📝 Updating configuration..."
python3 - <<EOF
import json
from pathlib import Path

config_path = Path("$CONFIG_FILE")
if config_path.exists():
    config = json.loads(config_path.read_text())
    config["enabled"] = False
    config_path.write_text(json.dumps(config, indent=2))
    print("✅ Configuration updated: enabled = false")
else:
    print("⚠️  Config file not found")
EOF

# Update rule frontmatter to alwaysApply: false
echo "📝 Updating rule file..."
python3 - <<EOF
from pathlib import Path
import re

rule_path = Path("$RULE_FILE")
if rule_path.exists():
    content = rule_path.read_text()
    
    # Replace alwaysApply: true with alwaysApply: false
    updated = re.sub(
        r'alwaysApply:\s*true',
        'alwaysApply: false',
        content
    )
    
    if updated != content:
        rule_path.write_text(updated)
        print("✅ Rule file updated: alwaysApply = false")
    else:
        print("⚠️  Rule file already has alwaysApply: false")
else:
    print("⚠️  Rule file not found")
EOF

echo ""
echo "✅ Self-Evolution System Disabled!"
echo ""
echo "📊 Status:"
echo "   - Pattern analysis: INACTIVE"
echo "   - The system will not analyze patterns or generate proposals"
echo ""
echo "💡 Note:"
echo "   - All existing proposals, backups, and tracking data are preserved"
echo "   - You can still manually run analysis: ./cursor/evolution/scripts/analyze.py $PROJECT_ROOT"
echo "   - To re-enable: run ./cursor/evolution/scripts/enable.sh"
echo ""
