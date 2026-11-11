import os
import shutil
import zipfile

src_root = r"D:\mindtrap_ai-main"
target_dir = r"D:\MindTrap_PlayConsole_Release"
target_screens = os.path.join(target_dir, "phone_screenshots")
zip_path = r"D:\MindTrap_PlayConsole_Release.zip"

os.makedirs(target_screens, exist_ok=True)

# 1. Copy AAB
aab_src = os.path.join(src_root, r"build\app\outputs\bundle\release\app-release.aab")
if os.path.exists(aab_src):
    shutil.copy2(aab_src, os.path.join(target_dir, "MindTrap_Release.aab"))
    print("AAB copied.")

# 2. Copy APK
apk_src = os.path.join(src_root, r"build\app\outputs\flutter-apk\app-release.apk")
if os.path.exists(apk_src):
    shutil.copy2(apk_src, os.path.join(target_dir, "MindTrap_Release.apk"))
    print("APK copied.")

# 3. Copy Icon & Feature Graphic
icon_src = os.path.join(src_root, r"play_store_assets\icon_512x512.png")
fg_src = os.path.join(src_root, r"play_store_assets\feature_graphic_1024x500.png")
if os.path.exists(icon_src):
    shutil.copy2(icon_src, os.path.join(target_dir, "icon_512x512.png"))
if os.path.exists(fg_src):
    shutil.copy2(fg_src, os.path.join(target_dir, "feature_graphic_1024x500.png"))
print("Icon & Feature Graphic copied.")

# 4. Copy Phone Screenshots
screens_src = os.path.join(src_root, r"play_store_assets\phone_screenshots")
if os.path.exists(screens_src):
    for f in os.listdir(screens_src):
        full_f = os.path.join(screens_src, f)
        if os.path.isfile(full_f):
            shutil.copy2(full_f, os.path.join(target_screens, f))
print("Screenshots copied.")

# 5. Keystore file
keystore_src = os.path.join(src_root, r"android\app\upload-keystore.jks")
if os.path.exists(keystore_src):
    shutil.copy2(keystore_src, os.path.join(target_dir, "upload-keystore.jks"))
print("Keystore copied.")

# 6. Write MindTrap Specific Metadata Info
info_content = """# MindTrap AI - Google Play Console Release Details

============================================================
1. APP BASICS (Store Presence -> Main store listing)
============================================================
* App Name (Title - Max 30 chars):
  MindTrap: Brain Tricky Puzzle

* Short Description (Max 80 chars):
  Tricky brain riddles, mind games & daily logic puzzles to boost your IQ.

* Full Description:
Welcome to MindTrap AI!

Challenge your mind with the ultimate cognitive riddle and brain training puzzle game, playable in 56 native languages! Train your brain, solve tricky logic puzzles, and expand your problem-solving intelligence across worlds of imagination.

KEY FEATURES:
• 56 Native Languages Supported: Play seamlessly in English, Spanish, French, Dutch, Hindi, Urdu, Arabic, Bengali, and many more!
• Tricky Riddles & Brain Teasers: Hundreds of hand-crafted stages designed to test your lateral thinking and cognitive flexibility.
• Exciting World Progression: Explore unique thematic worlds like Sunset Meadow, Sunlit Forest, Tropical Lagoon, and Sakura Sanctuary.
• Daily Login Rewards: Earn gems and coins every day to unlock helpful hints and boosters.
• Cloud Sync & Guest Play: Save your progress securely or sign in with Google/Apple for cross-device synchronization.

Download MindTrap AI today and begin your global brain training journey!

* Category: Games > Puzzle / Trivia
* Tags / Keywords: Brain Games, Tricky Puzzles, Riddles, IQ Test, Multi-Language, Logic Games

============================================================
2. TECHNICAL SPECIFICATIONS
============================================================
* Package Name (Application ID): com.mindtrap.ai
* Version Name: 1.0.1
* Version Code: 2
* Target SDK: 36 (Android 16 / 17 ready)
* Min SDK: 21 (Android 5.0+)

============================================================
3. RELEASE SIGNING & KEYSTORE DETAILS (Play App Signing)
============================================================
* Keystore File: upload-keystore.jks
* Key Alias: upload
* Key Password: mindtrap_upload_key2026
* Store Password: mindtrap_upload_key2026
* SHA-256 Fingerprint:
  80:46:04:EE:41:81:06:7B:54:6C:58:BC:1A:C2:EA:48:92:8E:F0:D5:E4:D3:B7:40:1B:24:EF:67:48:7B:8A:DA
* SHA-1 Fingerprint:
  5F:78:CF:B2:58:2F:64:89:36:07:D4:ED:AC:AF:5B:7E:13:9D:8A:5E

============================================================
4. INCLUDED FILES IN THIS ZIP
============================================================
1. MindTrap_Release.aab   -> Play Console Production Release file (.aab)
2. MindTrap_Release.apk   -> Direct testing APK file
3. icon_512x512.png       -> High-Res App Icon (512x512 px)
4. feature_graphic_1024x500.png -> Play Store Banner Graphic (1024x500 px)
5. phone_screenshots/     -> 8 High-Res Screenshots (1080x1920 px)
6. upload-keystore.jks    -> Production App Signing Keystore backup
7. PLAY_CONSOLE_DETAILS.txt -> Full text details & credentials
"""

with open(os.path.join(target_dir, "PLAY_CONSOLE_DETAILS.txt"), "w", encoding="utf-8") as f:
    f.write(info_content)

# 7. Create ZIP File
print("Creating ZIP file...")
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, target_dir)
            zipf.write(file_path, arcname)

print(f"ZIP File successfully created at: {zip_path}")
print(f"ZIP Size: {os.path.getsize(zip_path) / (1024*1024):.2f} MB")
