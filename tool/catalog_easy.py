# -*- coding: utf-8 -*-
"""
Catalog Easy: Complete 250 distinct Easy items in EN and UR
Combines Part 1 (1-125) and Part 2 (126-250)
"""
try:
    from tool.catalog_easy_part1 import ITEMS as PART1
    from tool.catalog_easy_part2 import ITEMS as PART2
except ImportError:
    from catalog_easy_part1 import ITEMS as PART1
    from catalog_easy_part2 import ITEMS as PART2

EASY_ITEMS = PART1 + PART2

if __name__ == '__main__':
    print(f"Total Easy items: {len(EASY_ITEMS)}")
