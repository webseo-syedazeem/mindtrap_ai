import re

with open('lib/main.dart', 'r', encoding='utf-8') as f:
    text = f.read()

# find blocks of PuzzleLevel(question: ..., options: ..., correctAnswer: ..., explanation: ...)
pattern = re.compile(r"PuzzleLevel\s*\(\s*question:\s*['\"](.*?)['\"],\s*options:\s*\[(.*?)\],\s*correctAnswer:\s*['\"](.*?)['\"],\s*explanation:\s*['\"](.*?)['\"],?", re.DOTALL)
matches = pattern.findall(text)
print(f"Total PuzzleLevel instances: {len(matches)}")
unique_q = {m[0].strip() for m in matches}
print(f"Total Unique Questions: {len(unique_q)}")
