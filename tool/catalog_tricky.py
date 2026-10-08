# -*- coding: utf-8 -*-
"""
Master Tricky Catalog: exactly 350 items (IDs 651-1000).
Every item is an 8-tuple:
(q_en, opts_en, ans_en, exp_en, q_ur, opts_ur, ans_ur, exp_ur)
"""

from tool.tricky_p1_chunk1 import ITEMS as c1
from tool.tricky_p1_chunk2 import ITEMS as c2
from tool.tricky_batch_2 import ITEMS as b2
from tool.tricky_batch_3 import ITEMS as b3
from tool.tricky_batch_4 import ITEMS as b4
from tool.tricky_batch_5 import ITEMS as b5
from tool.tricky_batch_5_part2 import ITEMS as b5_2
from tool.tricky_batch_6 import ITEMS as b6

ITEMS = c1 + c2 + b2 + b3 + b4 + b5 + b5_2 + b6

if __name__ == '__main__':
    print(f"Catalog Tricky loaded: {len(ITEMS)} items.")
