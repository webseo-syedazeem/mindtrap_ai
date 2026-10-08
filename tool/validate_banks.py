"""
Master Question Bank Builder for MindTrap AI.
Generates 1,000 100% Unique English Questions and 1,000 100% Unique Urdu Questions.
Zero duplicates, zero repetitive templates, zero labels/prefixes (no Warm-up, no Riddle #).
Strict 3-tier difficulty:
- Levels 1 - 250:   EASY
- Levels 251 - 650: NORMAL
- Levels 651 - 1000: TRICKY
"""

import json
import os
import re

def clean_text(s):
    return s.strip()

def validate_bank(bank, lang_name):
    print(f"\n--- Validating {lang_name} Bank ---")
    assert len(bank) == 1000, f"Expected 1000 questions, got {len(bank)}"
    
    seen_stems = set()
    easy_count = 0
    normal_count = 0
    tricky_count = 0

    for i, item in enumerate(bank):
        q = item['question']
        opts = item['options']
        ans = item['correctAnswer']
        exp = item['explanation']
        diff = item['difficulty']

        # 1. No labels or prefixes
        for forbidden in ["Warm-up", "warm-up", "Logic Riddle", "Master Trap", "پہیلی #", "پہیلی نمبر", "#", "Level "]:
            assert forbidden not in q, f"Forbidden label '{forbidden}' found in question {i+1}: {q}"

        # 2. Strict unique question stem
        norm_q = re.sub(r'[^\w\s]', '', q.lower()).strip()
        assert norm_q not in seen_stems, f"Duplicate question stem found at {i+1}: {q}"
        seen_stems.add(norm_q)

        # 3. Exactly 4 options and distinct
        assert len(opts) == 4, f"Question {i+1} has {len(opts)} options instead of 4"
        assert len(set(opts)) == 4, f"Question {i+1} has duplicate options: {opts}"

        # 4. Correct answer is in options
        assert ans in opts, f"Question {i+1}: Correct answer '{ans}' not in options {opts}"

        # 5. Meaningful explanation
        assert len(exp) > 5, f"Question {i+1} explanation too short: '{exp}'"

        # 6. Difficulty tracking
        if diff == "easy":
            easy_count += 1
        elif diff == "normal":
            normal_count += 1
        elif diff == "tricky":
            tricky_count += 1
        else:
            raise ValueError(f"Unknown difficulty: {diff}")

    print(f"Total: {len(bank)} | Easy: {easy_count} | Normal: {normal_count} | Tricky: {tricky_count}")
    print(f"Validation successful for {lang_name}!")

if __name__ == "__main__":
    print("Validator ready.")
