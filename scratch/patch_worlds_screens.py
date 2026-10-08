# -*- coding: utf-8 -*-
# 1. Patch lib/screens/worlds_screen.dart
with open('lib/screens/worlds_screen.dart', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace dialog in worlds_screen.dart
target_dialog = """                                    showProfessionalLockDialog(
                                      context,
                                      title: 'World Locked',
                                      subtitle: world.localizedTitle,
                                      message: 'Complete all 40 levels of World ${world.worldNumber - 1} to unlock this world!',"""

repl_dialog = """                                    showProfessionalLockDialog(
                                      context,
                                      title: tr('world_locked'),
                                      subtitle: world.localizedTitle,
                                      message: tr('world_unlock_req').replaceAll('{n}', '${world.worldNumber - 1}'),"""

assert target_dialog in text, "target_dialog not found in worlds_screen.dart"
text = text.replace(target_dialog, repl_dialog)

# Replace Levels Cleared in worlds_screen.dart
target_cleared = """                            Text(
                              '$completedLevels / ${world.levelsCount} Levels Cleared',"""

repl_cleared = """                            Text(
                              '${formatNumber(completedLevels)} / ${formatNumber(world.levelsCount)} ${tr('levels_cleared')}',"""

assert target_cleared in text, "target_cleared not found in worlds_screen.dart"
text = text.replace(target_cleared, repl_cleared)

# Replace Complete all 40 levels... prompt in worlds_screen.dart
target_prompt = """                      child: Text(
                        'Complete all 40 levels of World ${world.worldNumber - 1} to unlock',"""

repl_prompt = """                      child: Text(
                        tr('world_unlock_req').replaceAll('{n}', '${world.worldNumber - 1}'),"""

assert target_prompt in text, "target_prompt not found in worlds_screen.dart"
text = text.replace(target_prompt, repl_prompt)

with open('lib/screens/worlds_screen.dart', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully patched lib/screens/worlds_screen.dart!")


# 2. Patch lib/screens/world_levels_screen.dart
with open('lib/screens/world_levels_screen.dart', 'r', encoding='utf-8') as f:
    text2 = f.read()

target_wl1 = """                                  showProfessionalLockDialog(
                                    context,
                                    title: 'World Locked',
                                    subtitle: world.localizedTitle,
                                    message: 'Complete all 40 levels of World ${world.worldNumber - 1} to unlock this world!',"""

repl_wl1 = """                                  showProfessionalLockDialog(
                                    context,
                                    title: tr('world_locked'),
                                    subtitle: world.localizedTitle,
                                    message: tr('world_unlock_req').replaceAll('{n}', '${world.worldNumber - 1}'),"""

assert target_wl1 in text2, "target_wl1 not found in world_levels_screen.dart"
text2 = text2.replace(target_wl1, repl_wl1)

target_wl2 = "title: 'Level Locked',"
repl_wl2 = "title: tr('level_locked'),"

assert target_wl2 in text2, "target_wl2 not found in world_levels_screen.dart"
text2 = text2.replace(target_wl2, repl_wl2)

with open('lib/screens/world_levels_screen.dart', 'w', encoding='utf-8') as f:
    f.write(text2)

print("Successfully patched lib/screens/world_levels_screen.dart!")
