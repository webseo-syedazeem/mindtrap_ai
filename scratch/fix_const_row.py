# -*- coding: utf-8 -*-
with open('lib/widgets/app_drawer.dart', 'r', encoding='utf-8') as f:
    text = f.read()

target = """                  children: [
                    const Row(
                      children: [
                        Icon(Icons.military_tech_rounded, color: Color(0xFFF59E0B), size: 18),
                        SizedBox(width: 6),
                        Text(
                          tr('levels_odyssey'),"""

repl = """                  children: [
                    Row(
                      children: [
                        const Icon(Icons.military_tech_rounded, color: Color(0xFFF59E0B), size: 18),
                        const SizedBox(width: 6),
                        Text(
                          tr('levels_odyssey'),"""

assert target in text, "Target not found"
text = text.replace(target, repl)

with open('lib/widgets/app_drawer.dart', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed const Row in app_drawer.dart!")
