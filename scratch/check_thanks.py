with open('lib/localization/screen_translations.dart', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r"'([a-z_]{2,10})':\s*\{([^}]+)\}", text)
with open('scratch/thanks_output.txt', 'w', encoding='utf-8') as out:
    for lang, content in matches:
        for line in content.splitlines():
            if 'thanks_journey' in line:
                out.write(f"{lang}: {line.strip()}\n")
print("Done writing thanks_output.txt")
