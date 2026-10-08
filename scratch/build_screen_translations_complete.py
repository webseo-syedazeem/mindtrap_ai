# -*- coding: utf-8 -*-
import json
import os
import re
from base_dictionaries import EN_ACH, EN_DRAWER, UR_ACH, UR_DRAWER, HI_ACH, HI_DRAWER, AR_ACH, AR_DRAWER

# Spanish translations
ES_ACH = {k: v for k, v in EN_ACH.items()}
ES_ACH.update({
    'ach_first_win_title': 'Primera Victoria',
    'ach_first_win_desc': 'Gana tu primera ronda de desafío',
    'ach_perfect_mind_title': 'Mente Perfecta',
    'ach_perfect_mind_desc': 'Completa un desafío con 100% de precisión',
    'ach_quick_learner_title': 'Aprendiz Rápido',
    'ach_quick_learner_desc': 'Responde 10 preguntas correctamente',
    'ach_rising_star_title': 'Estrella en Ascenso',
    'ach_rising_star_desc': 'Completa 5 niveles en el Mundo 1',
    'ach_star_hunter_title': 'Cazador de Estrellas',
    'ach_star_hunter_desc': 'Consigue 15 estrellas en niveles',
    'ach_world_1_complete_title': 'Maestro Mundo 1',
    'ach_world_1_complete_desc': 'Completa los 40 niveles del Mundo 1',
    'ach_sharp_thinker_title': 'Pensador Ágil',
    'ach_sharp_thinker_desc': 'Responde 50 preguntas de desafío correctamente',
    'ach_trap_survivor_title': 'Superviviente de Trampas',
    'ach_trap_survivor_desc': 'Juega 10 rondas de desafío',
    'ach_world_2_complete_title': 'Maestro Mundo 2',
    'ach_world_2_complete_desc': 'Completa los 40 niveles del Mundo 2',
    'ach_world_3_complete_title': 'Maestro Mundo 3',
    'ach_world_3_complete_desc': 'Completa los 40 niveles del Mundo 3',
    'ach_world_5_complete_title': 'Campeón de 5 Mundos',
    'ach_world_5_complete_desc': 'Completa 5 mundos (200 niveles en total)',
    'ach_world_10_complete_title': 'Leyenda de 10 Mundos',
    'ach_world_10_complete_desc': 'Completa 10 mundos (400 niveles en total)',
    'ach_star_collector_50_title': 'Coleccionista de Estrellas',
    'ach_star_collector_50_desc': 'Consigue 50 estrellas en niveles',
    'ach_star_legend_100_title': 'Leyenda de Estrellas',
    'ach_star_legend_100_desc': 'Consigue 100 estrellas en niveles',
    'ach_brainiac_100_title': 'Cerebrito 100',
    'ach_brainiac_100_desc': 'Responde 100 preguntas correctamente',
    'ach_grandmaster_50_title': 'Gran Maestro',
    'ach_grandmaster_50_desc': 'Completa 50 niveles en varios mundos',
    'ach_perfectionist_20_title': 'Perfeccionista',
    'ach_perfectionist_20_desc': 'Gana 3 estrellas en 20 niveles diferentes',
    'ach_challenge_veteran_title': 'Veterano del Desafío',
    'ach_challenge_veteran_desc': 'Juega 25 rondas de desafío',
    'ach_perfect_score_title': 'Puntuación Perfecta',
    'ach_perfect_score_desc': 'Completa 10 rondas de desafío perfectas',
    'ach_challenge_expert_title': 'Experto en Desafíos',
    'ach_challenge_expert_desc': 'Completa 25 niveles de desafío',
    'ach_daily_champion_title': 'Campeón Diario',
    'ach_daily_champion_desc': 'Juega el puzzle diario 7 días seguidos',
    'ach_streak_starter_title': 'Iniciador de Racha',
    'ach_streak_starter_desc': 'Alcanza una racha de 3 días',
    'ach_dedicated_mind_title': 'Mente Dedicada',
    'ach_dedicated_mind_desc': 'Alcanza una racha de 7 días',
    'ach_streak_master_title': 'Maestro de la Racha',
    'ach_streak_master_desc': 'Alcanza una racha de 30 días',
})

ES_DRAWER = {
    'game_menu': 'Menú de Juego',
    'languages': 'Idiomas',
    'levels_odyssey': 'Odisea de 1.000 Niveles',
    'worlds_map_sub': '25 Mundos • Mapa de 1.000 Niveles',
    'worlds_badge': '25 MUNDOS',
    'store_sub': 'Gemas, Monedas y Pistas',
    'hot_deals': 'OFERTAS',
    'free': 'GRATIS',
    'mind_badge': 'MENTE',
    'language_label': 'Idioma',
    'tap_to_change': 'Toca para cambiar',
    'settings_sub': 'Audio, vibración y datos',
    'config_badge': 'AJUSTES',
    'stars_5_badge': '5 ESTRELLAS',
    'quick_audio_haptics': 'AUDIO Y VIBRACIÓN RÁPIDOS',
    'signed_out_success': 'Sesión cerrada con éxito',
    'signed_in_google': '¡Sesión iniciada con Google!',
    'google_sign_in_failed': 'Fallo al iniciar sesión con Google',
}

# French translations
FR_ACH = {k: v for k, v in EN_ACH.items()}
FR_ACH.update({
    'ach_first_win_title': 'Première Victoire',
    'ach_first_win_desc': 'Gagnez votre premier tour de défi',
    'ach_perfect_mind_title': 'Esprit Parfait',
    'ach_perfect_mind_desc': 'Terminez un défi avec 100% de précision',
    'ach_quick_learner_title': 'Apprenti Rapide',
    'ach_quick_learner_desc': 'Répondez correctement à 10 questions',
    'ach_rising_star_title': 'Étoile Montante',
    'ach_rising_star_desc': 'Terminez 5 niveaux dans le Monde 1',
    'ach_star_hunter_title': 'Chasseur d\'Étoiles',
    'ach_star_hunter_desc': 'Collectez 15 étoiles dans les niveaux',
    'ach_world_1_complete_title': 'Maître du Monde 1',
    'ach_world_1_complete_desc': 'Terminez les 40 niveaux du Monde 1',
    'ach_sharp_thinker_title': 'Penseur Vif',
    'ach_sharp_thinker_desc': 'Répondez correctement à 50 questions de défi',
    'ach_trap_survivor_title': 'Survivant du Piège',
    'ach_trap_survivor_desc': 'Jouez 10 tours de défi',
    'ach_world_2_complete_title': 'Maître du Monde 2',
    'ach_world_2_complete_desc': 'Terminez les 40 niveaux du Monde 2',
    'ach_world_3_complete_title': 'Maître du Monde 3',
    'ach_world_3_complete_desc': 'Terminez les 40 niveaux du Monde 3',
    'ach_world_5_complete_title': 'Champion de 5 Mondes',
    'ach_world_5_complete_desc': 'Terminez 5 mondes (200 niveaux au total)',
    'ach_world_10_complete_title': 'Légende de 10 Mondes',
    'ach_world_10_complete_desc': 'Terminez 10 mondes (400 niveaux au total)',
    'ach_star_collector_50_title': 'Collectionneur d\'Étoiles',
    'ach_star_collector_50_desc': 'Collectez 50 étoiles dans les niveaux',
    'ach_star_legend_100_title': 'Légende d\'Étoiles',
    'ach_star_legend_100_desc': 'Collectez 100 étoiles dans les niveaux',
    'ach_brainiac_100_title': 'Génie 100',
    'ach_brainiac_100_desc': 'Répondez correctement à 100 questions',
    'ach_grandmaster_50_title': 'Grand Maître',
    'ach_grandmaster_50_desc': 'Terminez 50 niveaux à travers les mondes',
    'ach_perfectionist_20_title': 'Perfectionniste',
    'ach_perfectionist_20_desc': 'Obtenez 3 étoiles sur 20 niveaux différents',
    'ach_challenge_veteran_title': 'Vétéran du Défi',
    'ach_challenge_veteran_desc': 'Jouez 25 tours de défi',
    'ach_perfect_score_title': 'Score Parfait',
    'ach_perfect_score_desc': 'Terminez 10 tours de défi parfaits',
    'ach_challenge_expert_title': 'Expert du Défi',
    'ach_challenge_expert_desc': 'Terminez 25 niveaux de défi',
    'ach_daily_champion_title': 'Champion Quotidien',
    'ach_daily_champion_desc': 'Jouez au puzzle quotidien 7 jours d\'affilée',
    'ach_streak_starter_title': 'Départ de Série',
    'ach_streak_starter_desc': 'Atteignez une série de 3 jours',
    'ach_dedicated_mind_title': 'Esprit Dévoué',
    'ach_dedicated_mind_desc': 'Atteignez une série de 7 jours',
    'ach_streak_master_title': 'Maître de Série',
    'ach_streak_master_desc': 'Atteignez une série de 30 jours',
})

FR_DRAWER = {
    'game_menu': 'Menu du Jeu',
    'languages': 'Langues',
    'levels_odyssey': 'Odyssée de 1 000 Niveaux',
    'worlds_map_sub': '25 Mondes • Carte de 1 000 Niveaux',
    'worlds_badge': '25 MONDES',
    'store_sub': 'Gemmes, Pièces & Indices',
    'hot_deals': 'OFFRES',
    'free': 'GRATUIT',
    'mind_badge': 'ESPRIT',
    'language_label': 'Langue',
    'tap_to_change': 'Appuyez pour changer',
    'settings_sub': 'Audio, vibration & données',
    'config_badge': 'PARAMÈTRES',
    'stars_5_badge': '5 ÉTOILES',
    'quick_audio_haptics': 'CONTRÔLES AUDIO RAPIDES',
    'signed_out_success': 'Déconnexion réussie',
    'signed_in_google': 'Connecté avec Google !',
    'google_sign_in_failed': 'Échec de connexion Google',
}

# German translations
DE_ACH = {k: v for k, v in EN_ACH.items()}
DE_ACH.update({
    'ach_first_win_title': 'Erster Sieg',
    'ach_first_win_desc': 'Gewinne deine erste Herausforderungsrunde',
    'ach_perfect_mind_title': 'Perfekter Geist',
    'ach_perfect_mind_desc': 'Schließe eine Herausforderung mit 100% Genauigkeit ab',
    'ach_quick_learner_title': 'Schnelllerner',
    'ach_quick_learner_desc': 'Beantworte 10 Fragen richtig',
    'ach_rising_star_title': 'Aufsteigender Stern',
    'ach_rising_star_desc': 'Schließe 5 Level in Welt 1 ab',
    'ach_star_hunter_title': 'Sternenjäger',
    'ach_star_hunter_desc': 'Sammle 15 Sterne in Leveln',
    'ach_world_1_complete_title': 'Meister Welt 1',
    'ach_world_1_complete_desc': 'Schließe alle 40 Level von Welt 1 ab',
})

DE_DRAWER = {
    'game_menu': 'Spielmenü',
    'languages': 'Sprachen',
    'levels_odyssey': '1.000 Level Odyssee',
    'worlds_map_sub': '25 Welten • 1.000 Level Karte',
    'worlds_badge': '25 WELTEN',
    'store_sub': 'Edelsteine, Münzen & Hinweise',
    'hot_deals': 'ANGEBOTE',
    'free': 'GRATIS',
    'mind_badge': 'GEIST',
    'language_label': 'Sprache',
    'tap_to_change': 'Tippen zum Ändern',
    'settings_sub': 'Audio, Vibration & Spieldaten',
    'config_badge': 'EINSTELLUNGEN',
    'stars_5_badge': '5 STERNE',
    'quick_audio_haptics': 'SCHNELL-AUDIO & HAPTIK',
    'signed_out_success': 'Erfolgreich abgemeldet',
    'signed_in_google': 'Mit Google angemeldet!',
    'google_sign_in_failed': 'Google-Anmeldung fehlgeschlagen',
}

CURATED = {
    'en': (EN_ACH, EN_DRAWER),
    'ur': (UR_ACH, UR_DRAWER),
    'hi': (HI_ACH, HI_DRAWER),
    'ar': (AR_ACH, AR_DRAWER),
    'es': (ES_ACH, ES_DRAWER),
    'fr': (FR_ACH, FR_DRAWER),
    'de': (DE_ACH, DE_DRAWER),
}

# Read current screen_translations.dart
file_path = 'lib/localization/screen_translations.dart'
with open(file_path, 'r', encoding='utf-8') as f:
    orig_code = f.read()

# Parse data for each language
pattern = r"'([a-zA-Z_]+)':\s*\{([^}]+)\}"
matches = re.findall(pattern, orig_code)

all_langs = {}
for code, block in matches:
    kv_pattern = r"'([a-zA-Z0-9_]+)':\s*'([^']*)'"
    pairs = re.findall(kv_pattern, block)
    all_langs[code] = dict(pairs)

print(f"Parsed {len(all_langs)} languages from screen_translations.dart")

# Now update each language
for code in all_langs:
    cur_ach, cur_drawer = CURATED.get(code, (EN_ACH, EN_DRAWER))
    for k, v in cur_ach.items():
        all_langs[code][k] = v
    for k, v in cur_drawer.items():
        all_langs[code][k] = v

print("Merged all new keys for all languages!")

# Generate Dart file
output = [
    "// AUTO-GENERATED - DO NOT MODIFY DIRECTLY",
    "// Screen Translations for MindTrap AI (Achievements, Stats/Progress, Daily Challenge, Drawer, Form).",
    "// Complete coverage for all 56 supported languages.",
    "",
    "class ScreenTranslations {",
    "  ScreenTranslations._();",
    "",
    "  static const Map<String, Map<String, String>> data = {",
]

for code, kvs in all_langs.items():
    output.append(f"    '{code}': {{")
    for k, v in kvs.items():
        escaped_v = v.replace("\\", "\\\\").replace("'", "\\'")
        output.append(f"      '{k}': '{escaped_v}',")
    output.append("    },")

output.append("  };")
output.append("}")
output.append("")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(output))

print(f"Successfully wrote {file_path} with {len(all_langs)} languages!")
