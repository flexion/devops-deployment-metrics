#!/bin/sh
if git diff --cached --name-only | grep -q "^.env$"; then
    echo "Error: Attempt to commit forbidden file '.env'"
    exit 1
fi
