#!/usr/bin/env python3
"""Rename all remaining non-fig files based on their pattern."""
import os
import re

folder = "/Users/diarmidcampbell/Desktop/Archies book project/archie book figures"
os.chdir(folder)

# Get all files that don't start with fig_
files = [f for f in os.listdir(".") if not f.startswith("fig_") and not f.startswith(".")]

# Pattern to extract chapter and figure number
# Format is typically: chapter_fignum_description.ext or chapter_fignumletter_description.ext
pattern = re.compile(r'^(\d+)_(\d+[a-z]?)[\._].*\.(\w+)$')

for old_name in sorted(files):
    match = pattern.match(old_name)
    if match:
        chapter = match.group(1).zfill(2)
        fig_num = match.group(2)
        # Handle figure numbers like "10a" -> "10a", "3" -> "03"
        if fig_num[-1].isalpha():
            num_part = fig_num[:-1].zfill(2)
            letter = fig_num[-1]
            fig_formatted = f"{num_part}{letter}"
        else:
            fig_formatted = fig_num.zfill(2)
        ext = match.group(3)
        new_name = f"fig_{chapter}_{fig_formatted}.{ext}"

        # Check if target exists
        if os.path.exists(new_name):
            print(f"SKIP (exists): {old_name[:50]}... -> {new_name}")
        else:
            try:
                os.rename(old_name, new_name)
                print(f"OK: {old_name[:50]}... -> {new_name}")
            except Exception as e:
                print(f"ERROR: {old_name[:50]}...: {e}")
    else:
        print(f"NO MATCH: {old_name}")

print("\n\nFinal check - remaining non-fig files:")
remaining = [f for f in os.listdir(".") if not f.startswith("fig_") and not f.startswith(".")]
if remaining:
    for f in remaining:
        print(f"  {f}")
else:
    print("  None! All files renamed successfully.")

print(f"\nTotal files: {len(os.listdir('.')) - 1}")  # -1 for .DS_Store
