#!/usr/bin/env bash
# ==============================================================================
# OWASP TriSuElla — GitHub Wiki Publisher (Bash)
# Publishes wiki documentation to both target GitHub Wiki repositories
# ==============================================================================

set -euo pipefail

TARGET="${1:-both}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
WIKI_SOURCE_DIR="$PROJECT_ROOT/wiki"

ORIGIN_WIKI_URL="https://github.com/thundel/TriSuElla-AIDLCA-Framework.wiki.git"
OWASP_WIKI_URL="https://github.com/OWASP/TriSuElla-AIDLCA-Framework.wiki.git"

echo "============================================================"
echo "  OWASP TriSuElla GitHub Wiki Publisher v3.4.0"
echo "============================================================"
echo "Source Wiki Directory: $WIKI_SOURCE_DIR"

publish_to_wiki() {
    local name="$1"
    local url="$2"

    echo ""
    echo "[*] Processing remote: $name ($url)..."

    if ! git ls-remote "$url" >/dev/null 2>&1; then
        echo "[-] Wiki repo not yet initialized on GitHub for $name."
        echo "    To initialize, visit the repository on GitHub, click the 'Wiki' tab, and click 'Create the first page'."
        echo "    GitHub URL: ${url%.wiki.git}/wiki"
        return 0
    fi

    local temp_dir="$PROJECT_ROOT/scratch/wiki-publish-$name"
    rm -rf "$temp_dir"

    echo "[+] Cloning wiki repository..."
    git clone "$url" "$temp_dir"

    echo "[+] Copying wiki markdown files..."
    cp -r "$WIKI_SOURCE_DIR"/* "$temp_dir/"

    cd "$temp_dir"
    git config user.name "Bhaskar Puppala (PATEL)"
    git config user.email "bhaskar@trisuella.org"
    git add .
    if git diff --cached --quiet; then
        echo "[✓] Wiki for $name is already up to date."
    else
        git commit -m "docs(wiki): update TriSuElla-AIDLCA-Framework v3.4.0 documentation suite"
        echo "[+] Pushing to GitHub Wiki ($name)..."
        git push origin HEAD
        echo "[✓] Successfully published wiki to $name!"
    fi

    cd "$PROJECT_ROOT"
    rm -rf "$temp_dir"
}

if [ "$TARGET" = "both" ] || [ "$TARGET" = "origin" ]; then
    publish_to_wiki "origin" "$ORIGIN_WIKI_URL"
fi

if [ "$TARGET" = "both" ] || [ "$TARGET" = "owasp" ]; then
    publish_to_wiki "owasp" "$OWASP_WIKI_URL"
fi

echo ""
echo "[✓] Finished wiki publishing process."
