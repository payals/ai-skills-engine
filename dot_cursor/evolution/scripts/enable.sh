#!/bin/bash
# Enable self-evolution system

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
EVOLUTION_DIR="$PROJECT_ROOT/.cursor/evolution"
RULE_FILE="$PROJECT_ROOT/.cursor/rules/self-evolution.mdc"
CONFIG_FILE="$EVOLUTION_DIR/config.json"

echo "🧬 Enabling Self-Evolution System..."
echo ""

# Check if rule file exists
if [ ! -f "$RULE_FILE" ]; then
    echo "❌ Error: self-evolution.mdc not found at $RULE_FILE"
    exit 1
fi

# Check if config exists
if [ ! -f "$CONFIG_FILE" ]; then
    echo "❌ Error: config.json not found at $CONFIG_FILE"
    exit 1
fi

# Update config.json to enable
echo "📝 Updating configuration..."
python3 - <<EOF
import json
from pathlib import Path

config_path = Path("$CONFIG_FILE")
config = json.loads(config_path.read_text())
config["enabled"] = True
config_path.write_text(json.dumps(config, indent=2))
print("✅ Configuration updated: enabled = true")
EOF

# Update rule frontmatter to alwaysApply: true
echo "📝 Updating rule file..."
python3 - <<EOF
from pathlib import Path
import re

rule_path = Path("$RULE_FILE")
content = rule_path.read_text()

# Replace alwaysApply: false with alwaysApply: true
updated = re.sub(
    r'alwaysApply:\s*false',
    'alwaysApply: true',
    content
)

if updated != content:
    rule_path.write_text(updated)
    print("✅ Rule file updated: alwaysApply = true")
else:
    print("⚠️  Rule file already has alwaysApply: true")
EOF

# Create necessary directories
mkdir -p "$EVOLUTION_DIR/proposals"
mkdir -p "$EVOLUTION_DIR/backups"
mkdir -p "$EVOLUTION_DIR/tracking"
mkdir -p "$EVOLUTION_DIR/reports"

echo ""
echo "✅ Self-Evolution System Enabled!"
echo ""
echo "📊 Status:"
echo "   - Pattern analysis: ACTIVE"
echo "   - Auto-implement: $(jq -r '.auto_implement' "$CONFIG_FILE")"
echo "   - Require approval: $(jq -r '.require_user_approval' "$CONFIG_FILE")"
echo "   - Monitoring period: $(jq -r '.monitoring_period_days' "$CONFIG_FILE") days"
echo ""
echo "🔍 The system will now:"
echo "   1. Analyze napkin.md and TRACKER.md for patterns"
echo "   2. Generate improvement proposals when patterns detected"
echo "   3. Request your approval before implementing changes"
echo "   4. Track effectiveness of all changes"
echo ""
echo "📚 To disable: run ./cursor/evolution/scripts/disable.sh"
echo "📊 To run analysis: run ./cursor/evolution/scripts/analyze.py $PROJECT_ROOT"
echo ""
