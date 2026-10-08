# -*- coding: utf-8 -*-
import sys
sys.path.append('tool')

from data_normal_remaining_part1 import ITEMS as PART1
from data_normal_remaining_part2 import ITEMS as PART2

ITEMS = PART1 + PART2
print(f"Total Normal Remaining combined: {len(ITEMS)} items.")
