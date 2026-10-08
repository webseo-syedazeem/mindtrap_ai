# -*- coding: utf-8 -*-
"""
Master Builder for MindTrap AI: 1,000 completely unique, distinct questions in EN and UR.
Guarantees:
- Exactly 1,000 questions per language (250 Easy, 400 Normal, 350 Tricky)
- ZERO duplicate stems
- ZERO template loops or repeated POVs (max signature frequency <= 2)
- ZERO robotic prefixes or suffixes
- 4 unique options per question, correct answer matching
- Pure authentic English and Urdu native phrasing
"""
import json
import os
import re
from collections import Counter

print("Starting generation of 1,000 pristine items...")
