# -*- coding: utf-8 -*-
"""
Professional Master Question Bank Generator for MindTrap AI.
Strict criteria:
1. 1000 Unique English questions & 1000 Unique Urdu questions.
2. 0 repeating questions, 0 repeating options sets, 0 repetitive POV templates.
3. 0 label prefixes: NO "Warm-up", NO "Logic Riddle", NO "Master Trap", NO "آسان پہیلی".
4. Difficulty tiers:
   - 1-250:   EASY (Clean, approachable, everyday logic, intuitive physics/nature)
   - 251-650: NORMAL (Deductive puzzles, patterns, probability, clever scenarios)
   - 651-1000: TRICKY (Mind-benders, counter-intuitive traps, lateral misdirection)
"""

import json
import os
import re

def normalize(text):
    return ' '.join(re.sub(r'[^\w\s]', '', text.lower()).split())

class BankBuilder:
    def __init__(self, lang_code):
        self.lang_code = lang_code
        self.items = []
        self.seen_stems = set()

    def add(self, tier, question, options, answer, explanation):
        q = question.strip()
        ans = answer.strip()
        opts = [o.strip() for o in options]
        exp = explanation.strip()

        # Sanity check: NO label prefixes
        for bad in ["Warm-up", "warm-up", "Logic Riddle", "Master Trap", "پہیلی #", "#", "Level "]:
            if bad in q:
                raise ValueError(f"Found forbidden prefix '{bad}' in: {q}")

        # Unique question stem
        norm = normalize(q)
        if norm in self.seen_stems:
            return False
        
        # Must have 4 options and answer in options
        if len(opts) != 4 or len(set(opts)) != 4 or ans not in opts:
            return False

        self.seen_stems.add(norm)
        self.items.append({
            "id": len(self.items) + 1,
            "difficulty": tier,
            "question": q,
            "options": opts,
            "correctAnswer": ans,
            "explanation": exp
        })
        return True

print("BankBuilder helper ready.")
