#!/usr/bin/env bash
# Scaffold a new problem folder from the template.
#
# Usage:
#   ./scripts/new_problem.sh <week_number> <problem_number> <slug> <difficulty>
#
# Example:
#   ./scripts/new_problem.sh 1 2 titanic-survival-classifier Easy
#
# Creates:
#   problems/week-01/02-titanic-survival-classifier/README.md   (pre-filled from template)
#   problems/week-01/02-titanic-survival-classifier/solution.py (empty starter)

set -euo pipefail

if [ "$#" -ne 4 ]; then
  echo "Usage: $0 <week_number> <problem_number> <slug> <difficulty>"
  echo "Example: $0 1 2 titanic-survival-classifier Easy"
  exit 1
fi

WEEK_NUM=$(printf "%02d" "$1")
PROB_NUM=$(printf "%02d" "$2")
SLUG="$3"
DIFFICULTY="$4"

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WEEK_DIR="$REPO_ROOT/problems/week-$WEEK_NUM"
PROB_DIR="$WEEK_DIR/$PROB_NUM-$SLUG"

mkdir -p "$PROB_DIR"

TITLE=$(echo "$SLUG" | sed 's/-/ /g' | sed -r 's/(^|[[:space:]])(.)/\1\U\2/g')
TODAY=$(date +%Y-%m-%d)

sed \
  -e "s/<Problem Name>/$TITLE/" \
  -e "s/Easy \/ Medium \/ Hard/$DIFFICULTY/" \
  -e "s/\*\*Week:\*\* #/\*\*Week:\*\* $1/" \
  -e "s/YYYY-MM-DD/$TODAY/" \
  "$REPO_ROOT/templates/PROBLEM_TEMPLATE.md" > "$PROB_DIR/README.md"

touch "$PROB_DIR/solution.py"

echo "Created: $PROB_DIR/"
echo "  - README.md (from template, pre-filled with title/difficulty/date)"
echo "  - solution.py (empty)"
