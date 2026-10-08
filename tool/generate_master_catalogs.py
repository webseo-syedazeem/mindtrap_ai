# -*- coding: utf-8 -*-
"""
Generates complete 1,000 non-repeating, diverse questions for EN and UR.
Enforces:
- 0 identical question stems
- 0 identical POV structures (max frequency of any 5-word sentence signature <= 2)
- 0 synthetic tags or parenthetical markers
- Exact difficulty distributions: 250 Easy, 400 Normal, 350 Tricky
"""
import json
import re

print("Compiling catalogs...")
