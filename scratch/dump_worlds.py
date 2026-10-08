import re

with open('lib/models/world_model.dart', 'r', encoding='utf-8') as f:
    text = f.read()

# Find WorldData definitions
# WorldData(id: 0, title: '...', subtitle: '...', lore: '...')
worlds = re.findall(r"WorldData\(\s*id:\s*(\d+),\s*title:\s*'([^']+)',\s*subtitle:\s*'([^']+)',.*?lore:\s*'([^']+)'", text, re.DOTALL)
print(f"Extracted {len(worlds)} worlds from world_model.dart:")
for wid, title, subtitle, lore in worlds:
    print(f"World {wid}: {title} | {subtitle} | {lore[:30]}...")
