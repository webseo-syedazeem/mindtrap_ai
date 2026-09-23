import 'package:flutter/material.dart';
import '../localization/app_language.dart';

class WorldData {
  final int id; // 0 to 9
  final String title;
  final String subtitle;
  final String lore;
  final String backgroundAsset;
  final Color primaryColor;
  final Color secondaryColor;
  final Color glowColor;
  final Color cardGradientStart;
  final Color cardGradientEnd;
  final IconData icon;
  final int requiredStarsToUnlock;

  const WorldData({
    required this.id,
    required this.title,
    required this.subtitle,
    required this.lore,
    required this.backgroundAsset,
    required this.primaryColor,
    required this.secondaryColor,
    required this.glowColor,
    required this.cardGradientStart,
    required this.cardGradientEnd,
    required this.icon,
    this.requiredStarsToUnlock = 0,
  });

  int get worldNumber => id + 1;

  String get localizedTitle {
    final key = 'world_${id}_title';
    final val = tr(key);
    return val != key ? val : title;
  }

  String get localizedSubtitle {
    final key = 'world_${id}_subtitle';
    final val = tr(key);
    return val != key ? val : subtitle;
  }

  String get localizedLore {
    final key = 'world_${id}_lore';
    final val = tr(key);
    return val != key ? val : lore;
  }
}

class WorldThemes {
  WorldThemes._();

  static const List<WorldData> allWorlds = [
    WorldData(
      id: 0,
      title: 'Sunset Meadow',
      subtitle: 'Golden Dawn',
      lore: 'Bask in golden sunlight across blooming wildflower hills where foundational logic begins.',
      backgroundAsset: 'assets/images/Stage-1.webp',
      primaryColor: Color(0xFFFF9E00),
      secondaryColor: Color(0xFFFF5400),
      glowColor: Color(0xFFFFD166),
      cardGradientStart: Color(0x992B1500),
      cardGradientEnd: Color(0xCC110800),
      icon: Icons.wb_sunny_rounded,
      requiredStarsToUnlock: 0,
    ),
    WorldData(
      id: 1,
      title: 'Sunlit Forest',
      subtitle: 'Whispering Pines',
      lore: 'Traverse enchanted pine groves where golden sunbeams pierce morning mist.',
      backgroundAsset: 'assets/images/Stage-2.webp',
      primaryColor: Color(0xFF10B981),
      secondaryColor: Color(0xFF059669),
      glowColor: Color(0xFF34D399),
      cardGradientStart: Color(0x99042617),
      cardGradientEnd: Color(0xCC01120A),
      icon: Icons.forest_rounded,
      requiredStarsToUnlock: 6,
    ),
    WorldData(
      id: 2,
      title: 'Tropical Lagoon',
      subtitle: 'Sunset Coast',
      lore: 'Stroll pristine sands where warm ocean waves reflect brilliant sunset colors.',
      backgroundAsset: 'assets/images/Stage-3.webp',
      primaryColor: Color(0xFF00C9FF),
      secondaryColor: Color(0xFFFF6B6B),
      glowColor: Color(0xFF48CAE4),
      cardGradientStart: Color(0x99062E3B),
      cardGradientEnd: Color(0xCC02141A),
      icon: Icons.beach_access_rounded,
      requiredStarsToUnlock: 15,
    ),
    WorldData(
      id: 3,
      title: 'Sakura Sanctuary',
      subtitle: 'Mount Fuji Twilight',
      lore: 'Marvel at cherry blossom petals dancing across mirrored lakes under snow-capped peaks.',
      backgroundAsset: 'assets/images/Stage-4.webp',
      primaryColor: Color(0xFFF472B6),
      secondaryColor: Color(0xFFEC4899),
      glowColor: Color(0xFFFBCFE8),
      cardGradientStart: Color(0x99330922),
      cardGradientEnd: Color(0xCC17030F),
      icon: Icons.filter_vintage_rounded,
      requiredStarsToUnlock: 25,
    ),
    WorldData(
      id: 4,
      title: 'Lavender Twilight',
      subtitle: 'Firefly Valley',
      lore: 'Immerse your mind in endless purple lavender rows illuminated by dancing firefly orbs.',
      backgroundAsset: 'assets/images/Stage-5.webp',
      primaryColor: Color(0xFF06B6D4),
      secondaryColor: Color(0xFF0284C7),
      glowColor: Color(0xFF67E8F9),
      cardGradientStart: Color(0x99083344),
      cardGradientEnd: Color(0xCC031826),
      icon: Icons.nightlight_round,
      requiredStarsToUnlock: 35,
    ),
    WorldData(
      id: 5,
      title: 'Autumn Haven',
      subtitle: 'Golden Brook',
      lore: 'Follow crystal clear streams through golden birch woods to a peaceful mountain shelter.',
      backgroundAsset: 'assets/images/Stage-6.webp',
      primaryColor: Color(0xFFF59E0B),
      secondaryColor: Color(0xFFD97706),
      glowColor: Color(0xFFFDE68A),
      cardGradientStart: Color(0x99301E03),
      cardGradientEnd: Color(0xCC140C01),
      icon: Icons.park_rounded,
      requiredStarsToUnlock: 45,
    ),
    WorldData(
      id: 6,
      title: 'Alpine Glaciers',
      subtitle: 'Crystal Peaks',
      lore: 'Conquer majestic snowy mountain massifs mirrored in pure turquoise glacial water.',
      backgroundAsset: 'assets/images/Stage-7.webp',
      primaryColor: Color(0xFF38BDF8),
      secondaryColor: Color(0xFF0284C7),
      glowColor: Color(0xFFBAE6FD),
      cardGradientStart: Color(0x9904223A),
      cardGradientEnd: Color(0xCC02101C),
      icon: Icons.landscape_rounded,
      requiredStarsToUnlock: 55,
    ),
    WorldData(
      id: 7,
      title: 'Blossom Valley',
      subtitle: 'Serene Mist',
      lore: 'Float above dreamlike pastel valleys shrouded in gentle mist and blossoming trees.',
      backgroundAsset: 'assets/images/daily_puzzle_landing_background.webp',
      primaryColor: Color(0xFFFB7185),
      secondaryColor: Color(0xFFE11D48),
      glowColor: Color(0xFFFECDD3),
      cardGradientStart: Color(0x99300A15),
      cardGradientEnd: Color(0xCC140308),
      icon: Icons.spa_rounded,
      requiredStarsToUnlock: 65,
    ),
    WorldData(
      id: 8,
      title: 'Emerald Waters',
      subtitle: 'Highland Fjord',
      lore: 'Navigate rolling green peaks and serene turquoise fjords under clear mountain skies.',
      backgroundAsset: 'assets/images/level_complete_background.webp',
      primaryColor: Color(0xFF34D399),
      secondaryColor: Color(0xFF059669),
      glowColor: Color(0xFFA7F3D0),
      cardGradientStart: Color(0x9906291C),
      cardGradientEnd: Color(0xCC02120C),
      icon: Icons.water_rounded,
      requiredStarsToUnlock: 75,
    ),
    WorldData(
      id: 9,
      title: 'Celestial Zenith',
      subtitle: 'Sky Realm',
      lore: 'Reach the pinnacle of intellect above sunlit clouds in the realm of master thinkers.',
      backgroundAsset: 'assets/images/puzzle_complete_background.webp',
      primaryColor: Color(0xFF818CF8),
      secondaryColor: Color(0xFF6366F1),
      glowColor: Color(0xFFC7D2FE),
      cardGradientStart: Color(0x9919173D),
      cardGradientEnd: Color(0xCC0A091C),
      icon: Icons.workspace_premium_rounded,
      requiredStarsToUnlock: 85,
    ),
  ];

  static WorldData getWorld(int worldIndex) {
    if (worldIndex < 0 || worldIndex >= allWorlds.length) {
      return allWorlds[0];
    }
    return allWorlds[worldIndex];
  }
}
