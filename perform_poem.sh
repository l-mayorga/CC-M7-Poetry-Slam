#!/bin/bash
# Opens a poem in Preview and reads it out loud.

# Usage: bash perform_poem.sh <poem_title> [--move-bg]

# Validate usage
if [ -z "$1" ]; then
    echo "Usage: $0 <poem_title> [--move-bg]"
    exit 1
fi

# Check if the poem txt exists
if [ ! -f "generated_poems_txt/$1.txt" ]; then
    echo "generated_poems_txt/$1.txt"
    echo "Poem txt not found"
    exit 1
fi

# Check if the poem png exists
if [ ! -f "generated_poems_png/$1.png" ]; then
    echo "Poem png not found"
    exit 1
fi

open -a "Preview" "generated_poems_png/$1.png"

sleep 1

# Read the poem
cat "generated_poems_txt/$1.txt" | tr '\n' ' ' | say

# If flag set, the move the bg png to the bgs folder
if [[ " $@ " == *" --move-bg "* ]]; then
    mv generated_poems_png/$1_bg.png generated_bgs_png/$1_bg.png
fi