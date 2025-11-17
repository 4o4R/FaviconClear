#!/bin/bash
set -e

DIR="$(cd "$(dirname "$0")" && pwd)"
SCRIPT="$DIR/clear_favicon_cache.py"

echo "Running favicon cache cleaner..."
/usr/bin/env python3 "$SCRIPT"

printf "\nDone. Press ENTER to close this window."
read -r _
