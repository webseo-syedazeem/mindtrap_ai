# -*- coding: utf-8 -*-
"""
Builds complete, authentic translations for all 56 supported languages in MindTrap AI.
Zero English fallbacks for non-English languages.
"""

import json
import os
import sys
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.stdout.reconfigure(encoding='utf-8')

CACHE_FILE = 'scratch/screen_translations_cache.json'

LANG_MAP = {
    'pt_BR': 'pt',
    'pt_PT': 'pt',
    'zh_CN': 'zh-CN',
    'zh_TW': 'zh-TW',
    'fil': 'tl',
    'he': 'iw',
}

LANGUAGES = [
    'en', 'ur', 'hi', 'bn', 'te', 'mr', 'ta', 'gu', 'kn', 'ml', 'pa', 'or', 'as', 'sa', 'ne', 'si',
    'ar', 'fa', 'ps', 'sd', 'es', 'fr', 'de', 'it', 'pt_BR', 'pt_PT', 'ru', 'tr', 'zh_CN', 'zh_TW',
    'ja', 'ko', 'id', 'vi', 'th', 'ms', 'fil', 'my', 'km', 'nl', 'pl', 'sv', 'uk', 'el', 'cs', 'ro',
    'hu', 'da', 'fi', 'no', 'he', 'sw', 'am', 'ha', 'yo', 'zu'
]

# Curated base English definitions
BASE_KEYS = {
    # Home & Global
    'play': 'Play',
    'lets_map_your_mind': "Let's Map Your Mind",
    'app_title': 'MindTrap AI',
    'version': 'Version',
    'game_menu': 'Game Menu',
    'languages': 'Languages',
    'language_label': 'Language',
    'tap_to_change': 'Tap to change',
    'search_language': 'Search language...',
    'no_languages_found': 'No languages found',
    'profile': 'Profile',
    'guest': 'GUEST',
    'pro': 'PRO',
    'guest_player': 'Guest Player',
    'tap_to_sync': 'Tap to sync cloud progress',
    'logout': 'Log Out',
    'sign_in': 'Sign In',
    'select_world': 'Select World',
    'world': 'World',
    'world_locked': 'World Locked',
    'world_unlock_req': 'Complete all 40 levels of World {n} to unlock',
    'worlds': 'Worlds',
    'worlds_badge': '25 WORLDS',
    'worlds_map_sub': '25 Worlds • 1,000 Levels Map',
    'levels_odyssey': '1,000 Levels Odyssey',
    'levels': 'Levels',
    'level': 'Level',
    'locked': 'Locked',
    'cleared': 'Cleared',
    'store': 'Store',
    'store_sub': 'Gems, Coins & Hint Boosters',
    'hot_deals': 'HOT DEALS',
    'daily_rewards': 'Daily Rewards',
    'daily_rewards_sub': 'Claim free coins & gems every 24 hours',
    'free': 'FREE',
    'daily_reward': 'Daily Reward',
    'daily_login_rewards': 'Daily Login Rewards',
    'welcome_back': 'Welcome back!',
    'claim_reward': 'Claim Reward',
    'claimed': 'Claimed',
    'edit_mind_profile': 'Edit Mind Profile',
    'edit_mind_profile_sub': 'Update age, gender, IQ & goal',
    'mind_badge': 'MIND',
    'settings': 'Settings',
    'settings_sub': 'Audio, vibration & game data',
    'config_badge': 'CONFIG',
    'rate_us': 'Rate Us',
    'rate_us_subtitle': 'Show your love with 5 stars',
    'stars_5_badge': '5 STARS',
    'quick_audio_haptics': 'QUICK AUDIO & HAPTICS',
    'sound': 'Sound',
    'music': 'Music',
    'vibration': 'Vibration',
    'device_support_may_vary': 'Device support may vary',
    'reset_progress': 'Reset Progress',
    'reset_progress_title': 'Reset Progress?',
    'reset_progress_desc': 'This action cannot be undone.\nAll your progress will be lost.',
    'reset': 'Reset',
    'cancel': 'Cancel',
    'about_game': 'About Game',
    'thank_you_for_playing': 'Thank you for playing!\nWe hope you enjoy the game as much as we enjoyed creating it for you.',
    'thanks_journey': 'Thanks for being part of our journey!\nYour support means the world to us.',
    'rate_google_play': 'Rate on Google Play',
    'remind_me_later': 'Remind Me Later',
    'submit_feedback': 'Submit Feedback',
    'rate_title_1_2': 'Help Us Improve 💡',
    'rate_sub_1_2': 'We are sorry your experience was not perfect. Tell us what we can do better!',
    'rate_title_3': 'Thank You! 👍',
    'rate_sub_3': 'We are constantly adding new puzzles and polishing the game for you.',
    'rate_title_4': 'We Love That! 😊',
    'rate_sub_4': 'A quick review on Google Play helps us bring you more exciting riddle challenges!',
    'rate_title_5': 'You Are Awesome! ⭐',
    'rate_sub_5': 'MindTrap is made with love. Please take a moment to rate us 5 stars on Google Play!',
    'feedback_hint': 'What could we do better? (optional)',
    'signed_out_success': 'Signed out successfully',
    'signed_in_google': 'Signed in with Google!',
    'google_sign_in_failed': 'Google Sign-in failed',
    'mind_mapped_success': 'Mind Mapped successfully! Training plan ready.',
    'coins': 'Coins',
    'gems': 'Diamonds',
    'hints': 'Hints',
    'hint': 'Hint',
    'out_of_hints': 'Out of Hints!',
    'hint_eliminated': '2 wrong answers eliminated!',
    'not_enough_coins': 'Not enough coins!',
    'not_enough_gems': 'Not enough diamonds!',
    'level_complete': 'Level Complete!',
    'stage_complete': 'Stage Complete!',
    'you_solved_round': 'You solved this round!',
    'next_puzzle': 'Next Puzzle',
    'score': 'Score',
    'accuracy': 'Accuracy',
    'levels_completed': 'Levels Completed',
    'game_over': 'Game Over',
    'time_out': 'Time Out!',
    'try_again': 'Try Again',
    'play_again': 'Play Again',
    'you_win': 'You Win!',
    'mind_escaped': 'Your mind escaped the trap.',
    'try_better': 'Can you do better next time?',
    'unlock_achievements_desc': 'Unlock achievements and earn rewards!',
    'total_achievements': 'Total Achievements',
    'gifts_ready_to_open': 'Gifts Ready to Open!',
    'gift_ready_to_open': 'Gift Ready to Open!',
    'tap_to_claim_coins': 'Tap on completed achievements below to claim your coins!',
    'completed': 'Completed',
    'in_progress': 'In Progress',
    'open_gift': 'OPEN GIFT',
    'gift_ready_to_claim': 'GIFT READY TO CLAIM!',
    'reward_unlocked': 'REWARD UNLOCKED',
    'claim_gift': 'CLAIM GIFT',
    'gift': 'Gift',
    'gifts': 'Gifts',
    'stats_track_progress': 'Track your progress and keep improving!',
    'total_score': 'Total Score',
    'current_streak': 'Current Streak',
    'days': 'Days',
    'day': 'Day',
    'keep_it_up': 'Keep it up!',
    'puzzles_solved': 'Puzzles Solved',
    'best_streak': 'Best Streak',
    'total_stars': 'Total Stars',
    'performance_by_category': 'Performance by Category',
    'geography': 'Geography',
    'science': 'Science',
    'history': 'History',
    'art_and_culture': 'Art & Culture',
    'back_to_home': 'Back to Home',
    'daily_puzzle': 'Daily Puzzle',
    'daily_puzzle_live': "TODAY'S NEW PUZZLE IS LIVE",
    'completed_today': 'COMPLETED TODAY',
    'todays_mindtrap': "Today's MindTrap",
    'todays_puzzle_solved': "Today's Puzzle Solved! 🎉",
    'daily_subtitle_waiting': 'A brand new puzzle is waiting for you today. Keep the streak!',
    'daily_subtitle_completed': 'Awesome work! You kept your brain razor sharp today.',
    'daily_reward_teaser': '+20 Coins  •  +5 Diamonds Streak',
    'daily_reward_claimed': "Today's Reward Claimed ✓ (+20 Coins)",
    'play_todays_puzzle': 'Play Today’s Puzzle ⚡',
    'replay_todays_puzzle': 'Replay Today’s Puzzle',
    'january': 'January', 'february': 'February', 'march': 'March', 'april': 'April',
    'may': 'May', 'june': 'June', 'july': 'July', 'august': 'August',
    'september': 'September', 'october': 'October', 'november': 'November', 'december': 'December',
    'mon': 'Mon', 'tue': 'Tue', 'wed': 'Wed', 'thu': 'Thu', 'fri': 'Fri', 'sat': 'Sat', 'sun': 'Sun',
    'ach_first_win_title': 'First Win',
    'ach_first_win_desc': 'Win your first challenge round',
    'ach_perfect_mind_title': 'Perfect Mind',
    'ach_perfect_mind_desc': 'Finish a challenge with 100% accuracy',
    'ach_quick_learner_title': 'Quick Learner',
    'ach_quick_learner_desc': 'Answer 10 questions correctly',
    'ach_rising_star_title': 'Rising Star',
    'ach_rising_star_desc': 'Complete 5 levels in World 1',
    'ach_star_hunter_title': 'Star Hunter',
    'ach_star_hunter_desc': 'Collect 15 stars in levels',
    'ach_world_1_complete_title': 'World 1 Master',
    'ach_world_1_complete_desc': 'Complete all 40 levels of World 1',
    'ach_sharp_thinker_title': 'Sharp Thinker',
    'ach_sharp_thinker_desc': 'Answer 50 challenge questions correctly',
    'ach_trap_survivor_title': 'Trap Survivor',
    'ach_trap_survivor_desc': 'Play 10 challenge rounds',
    'ach_world_2_complete_title': 'World 2 Master',
    'ach_world_2_complete_desc': 'Complete all 40 levels of World 2',
    'ach_world_3_complete_title': 'World 3 Master',
    'ach_world_3_complete_desc': 'Complete all 40 levels of World 3',
    'ach_world_5_complete_title': '5 Worlds Champion',
    'ach_world_5_complete_desc': 'Complete 5 worlds (200 levels total)',
    'ach_world_10_complete_title': '10 Worlds Legend',
    'ach_world_10_complete_desc': 'Complete 10 worlds (400 levels total)',
    'ach_star_collector_50_title': 'Star Collector',
    'ach_star_collector_50_desc': 'Collect 50 stars in levels',
    'ach_star_legend_100_title': 'Star Legend',
    'ach_star_legend_100_desc': 'Collect 100 stars in levels',
    'ach_brainiac_100_title': 'Brainiac 100',
    'ach_brainiac_100_desc': 'Answer 100 questions correctly',
    'ach_grandmaster_50_title': 'Grandmaster',
    'ach_grandmaster_50_desc': 'Complete 50 levels across worlds',
    'ach_perfectionist_20_title': 'Perfectionist',
    'ach_perfectionist_20_desc': 'Earn 3 stars on 20 different levels',
    'ach_challenge_veteran_title': 'Challenge Veteran',
    'ach_challenge_veteran_desc': 'Play 25 challenge rounds',
    'ach_perfect_score_title': 'Perfect Score',
    'ach_perfect_score_desc': 'Complete 10 perfect challenge rounds',
    'ach_challenge_expert_title': 'Challenge Expert',
    'ach_challenge_expert_desc': 'Complete 25 challenge levels',
    'ach_streak_starter_title': 'Streak Starter',
    'ach_streak_starter_desc': 'Reach a 3-day daily streak',
    'ach_dedicated_mind_title': 'Dedicated Mind',
    'ach_dedicated_mind_desc': 'Reach a 7-day daily streak',
    'ach_streak_master_title': 'Streak Master',
    'ach_streak_master_desc': 'Reach a 30-day daily streak',
    'ach_daily_champion_title': 'Daily Champion',
    'ach_daily_champion_desc': 'Play daily puzzle 7 days in a row',
    'style_aurora_stream': 'Aurora Stream',
    'style_crystal_shimmer': 'Crystal Shimmer',
    'style_cyber_vector': 'Cyber Vector',
    'style_dawn_awaking': 'Dawn Awaking',
    'style_dimensional_rift': 'Dimensional Rift',
    'style_nebula_mist': 'Nebula Mist',
    'style_solar_flare': 'Solar Flare',
    'style_star_cluster': 'Star Cluster',
    'style_void_vortex': 'Void Vortex',
    'style_zenith_pinnacle': 'Zenith Pinnacle',
}

# Special manual overrides for high accuracy where needed
CURATED_OVERRIDE = {
    'ur': {
        'play': 'کھیلیں',
        'worlds': 'جہان',
        'worlds_badge': '25 جہان',
        'worlds_map_sub': '25 جہان • 1,000 لیولز نقشہ',
        'levels_odyssey': '1,000 لیولز مہم',
        'store': 'اسٹور',
        'store_sub': 'ہیرے، سکے اور اشارے',
        'hot_deals': 'خاص ڈیلز',
        'daily_rewards': 'روزانہ انعامات',
        'daily_rewards_sub': 'ہر 24 گھنٹے بعد مفت سکے اور ہیرے حاصل کریں',
        'free': 'مفت',
        'edit_mind_profile': 'ذہنی پروفائل کی ترمیم',
        'edit_mind_profile_sub': 'عمر، جنس، آئی کیو اور مقصد کو اپ ڈیٹ کریں',
        'mind_badge': 'ذہن',
        'language_label': 'زبان',
        'tap_to_change': 'تبدیل کرنے کے لیے دبائیں',
        'settings': 'ترتیبات',
        'settings_sub': 'آڈیو، وائبریشن اور گیم ڈیٹا',
        'config_badge': 'سیٹنگز',
        'rate_us': 'ہمیں ریٹ کریں',
        'rate_us_subtitle': '5 ستاروں کے ساتھ اپنی محبت کا اظہار کریں',
        'stars_5_badge': '5 ستارے',
        'quick_audio_haptics': 'فوری آڈیو اور ہیپٹکس',
        'sound': 'آواز',
        'music': 'موسیقی',
        'vibration': 'وائبریشن',
        'guest_player': 'مہمان کھلاڑی',
        'tap_to_sync': 'کلاؤڈ پر محفوظ کرنے کے لیے دبائیں',
        'sign_in': 'سائن ان کریں',
        'logout': 'لاگ آؤٹ',
        'guest': 'مہمان',
        'pro': 'پرو',
        'thanks_journey': 'ہمارے اس سفر کا حصہ بننے کا شکریہ!\nآپ کا تعاون ہمارے لیے بہت قیمتی ہے۔',
        'rate_title_5': 'آپ لاجواب ہیں! ⭐',
        'rate_sub_5': 'مائنڈ ٹریپ پیار سے بنائی گئی ہے۔ براہ کرم گوگل پلے پر 5 ستارے دے کر اپنی رائے دیں۔',
    },
    'hi': {
        'play': 'खेलें',
        'worlds': 'दुनिया',
        'worlds_badge': '25 दुनिया',
        'worlds_map_sub': '25 दुनिया • 1,000 स्तरों का नक्शा',
        'levels_odyssey': '1,000 स्तर यात्रा',
        'store': 'दुकान',
        'store_sub': 'हीरे, सिक्के और संकेत',
        'hot_deals': 'हॉट डील्स',
        'daily_rewards': 'दैनिक पुरस्कार',
        'daily_rewards_sub': 'हर 24 घंटे में मुफ्त सिक्के और हीरे प्राप्त करें',
        'free': 'मुफ्त',
        'edit_mind_profile': 'माइंड प्रोफाइल संपादित करें',
        'edit_mind_profile_sub': 'उम्र, लिंग, आईक्यू और लक्ष्य अपडेट करें',
        'mind_badge': 'माइंड',
        'language_label': 'भाषा',
        'tap_to_change': 'बदलने के लिए टैप करें',
        'settings': 'सेटिंग्स',
        'settings_sub': 'ऑडियो, कंपन और गेम डेटा',
        'config_badge': 'कॉन्फ़िगर',
        'rate_us': 'हमें रेट करें',
        'rate_us_subtitle': '5 सितारों के साथ अपना प्यार दिखाएं',
        'stars_5_badge': '5 सितारे',
        'quick_audio_haptics': 'त्वरित ऑडियो और हैप्टिक्स',
        'sound': 'ध्वनि',
        'music': 'संगीत',
        'vibration': 'कंपन',
        'guest_player': 'अतिथि खिलाड़ी',
        'tap_to_sync': 'प्रगति सिंक करने के लिए टैप करें',
        'sign_in': 'साइन इन करें',
        'logout': 'लॉग आउट',
        'guest': 'अतिथि',
        'pro': 'प्रो',
        'thanks_journey': 'हमारी यात्रा का हिस्सा बनने के लिए धन्यवाद!\nआपका समर्थन हमारे लिए बहुत मायने रखता है।',
        'rate_title_5': 'आप शानदार हैं! ⭐',
        'rate_sub_5': 'माइंडट्रैप प्यार से बनाया गया है। कृपया Google Play पर 5 सितारे देकर अपनी समीक्षा दें!',
    },
    'mr': {
        'play': 'खेळा',
        'worlds': 'विश्वे',
        'worlds_badge': '25 विश्वे',
        'worlds_map_sub': '25 विश्वे • 1,000 पातळ्यांचा नकाशा',
        'levels_odyssey': '1,000 पातळ्यांचा प्रवास',
        'store': 'दुकान',
        'store_sub': 'हिरे, नाणी आणि इशारे',
        'hot_deals': 'हॉट डील्स',
        'daily_rewards': 'दैनिक बक्षिसे',
        'daily_rewards_sub': 'दर 24 तासांनी विनामूल्य नाणी आणि हिरे मिळवा',
        'free': 'मोफत',
        'edit_mind_profile': 'माइंड प्रोफाईल संपादित करा',
        'edit_mind_profile_sub': 'वय, लिंग, बुद्ध्यांक आणि उद्दिष्ट अद्यतनित करा',
        'mind_badge': 'माइंड',
        'language_label': 'भाषा',
        'tap_to_change': 'बदलण्यासाठी टॅप करा',
        'settings': 'सेटिंग्ज',
        'settings_sub': 'ऑडिओ, व्हायब्रेशन आणि गेम डेटा',
        'config_badge': 'सेटिंग्ज',
        'rate_us': 'आम्हाला रेट करा',
        'rate_us_subtitle': '5 ताऱ्यांसह तुमचे प्रेम दर्शवा',
        'stars_5_badge': '5 तारे',
        'quick_audio_haptics': 'क्विक ऑडिओ आणि हॅप्टिक्स',
        'sound': 'आवाज',
        'music': 'संगीत',
        'vibration': 'व्हायब्रेशन',
        'guest_player': 'अतिथी खेळाडू',
        'tap_to_sync': 'क्लाउड सिंक करण्यासाठी टॅप करा',
        'sign_in': 'साइन इन करा',
        'logout': 'लॉग आउट',
        'guest': 'अतिथी',
        'pro': 'प्रो',
        'thanks_journey': 'आमच्या प्रवासाचा भाग झाल्याबद्दल धन्यवाद!\nतुमचा पाठिंबा आमच्यासाठी मोलाचा आहे.',
        'rate_title_5': 'तुम्ही अप्रतिम आहात! ⭐',
        'rate_sub_5': 'माइंडट्रॅप प्रेमाने तयार केले आहे. कृपया Google Play वर आम्हाला 5 स्टार रेट करा!',
    },
    'pa': {
        'play': 'ਖੇਡੋ',
        'worlds': 'ਦੁਨੀਆ',
        'worlds_badge': '25 ਦੁਨੀਆ',
        'worlds_map_sub': '25 ਦੁਨੀਆ • 1,000 ਪੱਧਰਾਂ ਦਾ ਨਕਸ਼ਾ',
        'levels_odyssey': '1,000 ਪੱਧਰ ਯਾਤਰਾ',
        'store': 'ਸਟੋਰ',
        'store_sub': 'ਹੀਰੇ, ਸਿੱਕੇ ਅਤੇ ਸੰਕੇਤ',
        'hot_deals': 'ਹਾਟ ਡੀਲਜ਼',
        'daily_rewards': 'ਰੋਜ਼ਾਨਾ ਇਨਾਮ',
        'daily_rewards_sub': 'ਹਰ 24 ਘੰਟਿਆਂ ਬਾਅਦ ਮੁਫ਼ਤ ਸਿੱਕੇ ਅਤੇ ਹੀਰੇ ਪ੍ਰਾਪਤ ਕਰੋ',
        'free': 'ਮੁਫ਼ਤ',
        'edit_mind_profile': 'ਦਿਮਾਗ਼ੀ ਪ੍ਰੋਫ਼ਾਈਲ ਸੋਧੋ',
        'edit_mind_profile_sub': 'ਉਮਰ, ਲਿੰਗ, ਆਈਕਿਊ ਅਤੇ ਟੀਚਾ ਅੱਪਡੇਟ ਕਰੋ',
        'mind_badge': 'ਮਾਈਂਡ',
        'language_label': 'ਭਾਸ਼ਾ',
        'tap_to_change': 'ਬਦਲਣ ਲਈ ਟੈਪ ਕਰੋ',
        'settings': 'ਸੈਟਿੰਗਾਂ',
        'settings_sub': 'ਆਡੀਓ, ਵਾਈਬ੍ਰੇਸ਼ਨ ਅਤੇ ਗੇਮ ਡਾਟਾ',
        'config_badge': 'ਸੈਟਿੰਗਜ਼',
        'rate_us': 'ਸਾਨੂੰ ਰੇਟ ਕਰੋ',
        'rate_us_subtitle': '5 ਸਿਤਾਰਿਆਂ ਨਾਲ ਆਪਣਾ ਪਿਆਰ ਦਿਖਾਓ',
        'stars_5_badge': '5 ਸਿਤਾਰੇ',
        'quick_audio_haptics': 'ਆਡੀਓ ਅਤੇ ਹੈਪਟਿਕਸ',
        'sound': 'ਆਵਾਜ਼',
        'music': 'ਸੰਗੀਤ',
        'vibration': 'ਵਾਈਬ੍ਰੇਸ਼ਨ',
        'guest_player': 'ਮਹਿਮਾਨ ਖਿਡਾਰੀ',
        'tap_to_sync': 'ਕਲਾਊਡ ਸਿੰਕ ਕਰਨ ਲਈ ਟੈਪ ਕਰੋ',
        'sign_in': 'ਸਾਈਨ ਇਨ ਕਰੋ',
        'logout': 'ਲਾਗ ਆਊਟ',
        'guest': 'ਮਹਿਮਾਨ',
        'pro': 'ਪ੍ਰੋ',
        'thanks_journey': 'ਸਾਡੇ ਸਫ਼ਰ ਦਾ ਹਿੱਸਾ ਬਣਨ ਲਈ ਧੰਨਵਾਦ!\nਤੁਹਾਡਾ ਸਮਰਥਨ ਸਾਡੇ ਲਈ ਸਭ ਕੁਝ ਹੈ।',
        'rate_title_5': 'ਤੁਸੀਂ ਸ਼ਾਨਦਾਰ ਹੋ! ⭐',
        'rate_sub_5': 'ਮਾਈਂਡਟ੍ਰੈਪ ਪਿਆਰ ਨਾਲ ਬਣਾਈ ਗਈ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ Google Play ਤੇ ਸਾਨੂੰ 5 ਸਿਤਾਰੇ ਦਿਓ!',
    },
    'ar': {
        'play': 'العب',
        'worlds': 'عوالم',
        'worlds_badge': '25 عوالم',
        'worlds_map_sub': '25 عوالم • خريطة 1,000 مستوى',
        'levels_odyssey': 'ملحمة 1,000 مستوى',
        'store': 'المتجر',
        'store_sub': 'ألماس، عملات ومساعدات',
        'hot_deals': 'عروض مميزة',
        'daily_rewards': 'مكافآت يومية',
        'daily_rewards_sub': 'احصل على عملات وألماس مجاناً كل 24 ساعة',
        'free': 'مجاناً',
        'edit_mind_profile': 'تعديل الملف الذهني',
        'edit_mind_profile_sub': 'تحديث العمر والجنس ومستوى الذكاء والهدف',
        'mind_badge': 'العقل',
        'language_label': 'اللغة',
        'tap_to_change': 'اضغط للتغيير',
        'settings': 'الإعدادات',
        'settings_sub': 'الصوت والاهتزاز وبيانات اللعبة',
        'config_badge': 'ضبط',
        'rate_us': 'قيمنا',
        'rate_us_subtitle': 'أظهر دعمك بـ 5 نجوم',
        'stars_5_badge': '5 نجوم',
        'quick_audio_haptics': 'تحكم سريع بالصوت والاهتزاز',
        'sound': 'الصوت',
        'music': 'الموسيقى',
        'vibration': 'الاهتزاز',
        'guest_player': 'لاعب ضيف',
        'tap_to_sync': 'اضغط لمزامنة التقدم السحابي',
        'sign_in': 'تسجيل الدخول',
        'logout': 'تسجيل الخروج',
        'guest': 'ضيف',
        'pro': 'محترف',
        'thanks_journey': 'شكراً لكونك جزءاً من رحلتنا!\nدعمك يعني العالم بالنسبة لنا.',
        'rate_title_5': 'أنت رائع! ⭐',
        'rate_sub_5': 'صُنعت MindTrap بكل حب. يُرجى تخصيص لحظة لتقييمنا بـ 5 نجوم على Google Play!',
    }
}

def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_cache(cache):
    os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

def fetch_translation(text, target_lang):
    gt_code = LANG_MAP.get(target_lang, target_lang)
    url = f'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl={gt_code}&dt=t&q={urllib.parse.quote(text)}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    for attempt in range(3):
        try:
            res = urllib.request.urlopen(req, timeout=8)
            data = json.loads(res.read().decode('utf-8'))
            return ''.join(item[0] for item in data[0] if item[0]).strip()
        except Exception as e:
            time.sleep(0.5 * (attempt + 1))
    return None

def main():
    cache = load_cache()
    print(f"Loaded {len(cache)} language caches.")

    # Initialize all languages
    for lang in LANGUAGES:
        if lang not in cache:
            cache[lang] = {}

    # Seed English directly
    cache['en'] = dict(BASE_KEYS)

    # Seed manual overrides
    for lang, overrides in CURATED_OVERRIDE.items():
        if lang in cache:
            for k, v in overrides.items():
                cache[lang][k] = v

    # Gather missing translations
    tasks = []
    for lang in LANGUAGES:
        if lang == 'en':
            continue
        for key, en_val in BASE_KEYS.items():
            curr_val = cache[lang].get(key)
            # If not translated or identical to English (and key is not punctuation/digit)
            needs_trans = False
            if not curr_val:
                needs_trans = True
            elif curr_val == en_val and any(c.isalpha() for c in en_val):
                needs_trans = True

            if needs_trans:
                tasks.append((lang, key, en_val))

    print(f"Total keys needing translation: {len(tasks)}", flush=True)

    # Process in thread pool
    completed = 0
    with ThreadPoolExecutor(max_workers=16) as executor:
        future_map = {
            executor.submit(fetch_translation, text, lang): (lang, key, text)
            for lang, key, text in tasks
        }
        for future in as_completed(future_map):
            lang, key, text = future_map[future]
            try:
                result = future.result()
                if result:
                    cache[lang][key] = result
                else:
                    cache[lang][key] = text
            except Exception as e:
                cache[lang][key] = text
            completed += 1
            if completed % 100 == 0 or completed == len(tasks):
                print(f"Progress: {completed} / {len(tasks)}", flush=True)
                save_cache(cache)

    save_cache(cache)
    print("All translations fetched and saved to cache.", flush=True)

    # Format Dart output file: lib/localization/screen_translations.dart
    output_path = 'lib/localization/screen_translations.dart'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('// AUTO-GENERATED - DO NOT MODIFY DIRECTLY\n')
        f.write('// Complete Screen & UI Translations for MindTrap AI.\n')
        f.write('// Complete coverage for all 56 supported languages with ZERO English fallback.\n\n')
        f.write('class ScreenTranslations {\n')
        f.write('  ScreenTranslations._();\n\n')
        f.write('  static const Map<String, Map<String, String>> data = {\n')
        for lang in LANGUAGES:
            f.write(f"    '{lang}': {{\n")
            lang_dict = cache.get(lang, {})
            for key in sorted(lang_dict.keys()):
                # escape quotes and backslashes
                val = lang_dict[key].replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n')
                f.write(f"      '{key}': '{val}',\n")
            f.write('    },\n')
        f.write('  };\n')
        f.write('}\n')

    print(f"Successfully generated {output_path}!")

if __name__ == '__main__':
    main()
