import json
import os
import re

# Read app_language.dart
with open('lib/localization/app_language.dart', 'r', encoding='utf-8') as f:
    app_lang_content = f.read()

codes = re.findall(r"AppLanguage\(\s*code:\s*'([^']+)'", app_lang_content)
print(f"Total languages in app_language.dart: {len(codes)}")

missing_files = []
invalid_json = []
empty_questions = []

for c in codes:
    json_path = f"assets/questions/{c}.json"
    if not os.path.exists(json_path):
        missing_files.append(c)
        continue
    try:
        with open(json_path, 'r', encoding='utf-8') as jf:
            data = json.load(jf)
            if not isinstance(data, list) or len(data) == 0:
                empty_questions.append((c, len(data) if isinstance(data, list) else 'not a list'))
            else:
                # verify question format
                valid_count = 0
                for item in data:
                    q = item.get('question', '')
                    opts = item.get('options', [])
                    ans = item.get('correct_answer', '')
                    if q and len(opts) == 4 and ans in opts:
                        valid_count += 1
                if valid_count < 10:
                    empty_questions.append((c, f"only {valid_count} valid questions out of {len(data)}"))
    except Exception as e:
        invalid_json.append((c, str(e)))

print("Missing files:", missing_files)
print("Invalid JSON:", invalid_json)
print("Empty/Malformed questions:", empty_questions)
