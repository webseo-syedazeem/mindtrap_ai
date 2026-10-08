# -*- coding: utf-8 -*-
with open('lib/widgets/app_drawer.dart', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Signed out notification
text = text.replace("message: 'Signed out successfully',", "message: tr('signed_out_success'),")

# 2. Segmented tab buttons
text = text.replace("title: 'GAME MENU',", "title: tr('game_menu'),")
text = text.replace("title: 'LANGUAGES ($langCount)',", "title: '${tr('languages')} ($langCount)',")

# 3. 1,000 Levels Odyssey header
text = text.replace(
    """                        Text(
                          '1,000 LEVELS ODYSSEY',""",
    """                        Text(
                          tr('levels_odyssey'),"""
)

# 4. Worlds Odyssey NavTile
text = text.replace(
    """          _buildNavTile(
            title: tr('worlds'),
            subtitle: '25 Worlds • 1,000 Levels Map',
            badgeText: '25 WORLDS',""",
    """          _buildNavTile(
            title: tr('worlds'),
            subtitle: tr('worlds_map_sub'),
            badgeText: tr('worlds_badge'),"""
)

# 5. Store NavTile
text = text.replace(
    """          _buildNavTile(
            title: tr('store'),
            subtitle: 'Gems, Coins & Hint Boosters',
            badgeText: 'HOT DEALS',""",
    """          _buildNavTile(
            title: tr('store'),
            subtitle: tr('store_sub'),
            badgeText: tr('hot_deals'),"""
)

# 6. Daily Rewards badge
text = text.replace(
    """          _buildNavTile(
            title: tr('daily_rewards'),
            subtitle: tr('daily_rewards_sub'),
            badgeText: 'FREE',""",
    """          _buildNavTile(
            title: tr('daily_rewards'),
            subtitle: tr('daily_rewards_sub'),
            badgeText: tr('free'),"""
)

# 7. Edit Mind Profile badge
text = text.replace(
    """          // 3.5. Edit Mind Profile
          _buildNavTile(
            title: tr('edit_mind_profile'),
            subtitle: tr('edit_mind_profile_sub'),
            badgeText: 'MIND',""",
    """          // 3.5. Edit Mind Profile
          _buildNavTile(
            title: tr('edit_mind_profile'),
            subtitle: tr('edit_mind_profile_sub'),
            badgeText: tr('mind_badge'),"""
)

# 8. Active Language tile
text = text.replace(
    """          // 4. Active Language Selector Shortcut
          _buildNavTile(
            title: 'Language: ${currentLanguage.englishName}',
            subtitle: '${currentLanguage.flagEmoji} ${currentLanguage.nativeName} (Tap to change)',""",
    """          // 4. Active Language Selector Shortcut
          _buildNavTile(
            title: '${tr('language_label')}: ${currentLanguage.nativeName}',
            subtitle: '${currentLanguage.flagEmoji} ${currentLanguage.nativeName} (${tr('tap_to_change')})',"""
)

# 9. Game Settings tile
text = text.replace(
    """          // 5. Game Settings
          _buildNavTile(
            title: tr('settings'),
            subtitle: 'Audio, vibration & game data',
            badgeText: 'CONFIG',""",
    """          // 5. Game Settings
          _buildNavTile(
            title: tr('settings'),
            subtitle: tr('settings_sub'),
            badgeText: tr('config_badge'),"""
)

# 10. Rate Us tile
text = text.replace(
    """          // 6. Rate Us
          _buildNavTile(
            title: 'Rate MindTrap',
            subtitle: 'Show your love with 5 stars',
            badgeText: '5 STARS',""",
    """          // 6. Rate Us
          _buildNavTile(
            title: tr('rate_us'),
            subtitle: tr('rate_us_subtitle'),
            badgeText: tr('stars_5_badge'),"""
)

# 11. Quick audio strip header
text = text.replace(
    """                const Text(
                  'QUICK AUDIO & HAPTICS',""",
    """                Text(
                  tr('quick_audio_haptics'),"""
)

# 12. Audio toggles labels
text = text.replace("label: 'Sound',", "label: tr('sound'),")
text = text.replace("label: 'Music',", "label: tr('music'),")
text = text.replace("label: 'Vibrate',", "label: tr('vibration'),")

with open('lib/widgets/app_drawer.dart', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated app_drawer.dart successfully!")
