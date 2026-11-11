import os
import shutil

src_root = r"D:\mindtrap_ai-main"
dest = r"D:\Word_Puzzle_Language_Quest_PlayConsole"
screens_dest = os.path.join(dest, "screenshots")

os.makedirs(screens_dest, exist_ok=True)

# Copy .aab and .apk
aab_src = os.path.join(src_root, r"build\app\outputs\bundle\release\app-release.aab")
apk_src = os.path.join(src_root, r"build\app\outputs\flutter-apk\app-release.apk")

if os.path.exists(aab_src):
    shutil.copy2(aab_src, os.path.join(dest, "app-release.aab"))
if os.path.exists(apk_src):
    shutil.copy2(apk_src, os.path.join(dest, "app-release.apk"))

# Copy icon and feature graphic
icon_src = os.path.join(src_root, r"play_store_assets\icon_512x512.png")
fg_src = os.path.join(src_root, r"play_store_assets\feature_graphic_1024x500.png")

if os.path.exists(icon_src):
    shutil.copy2(icon_src, os.path.join(dest, "icon_512x512.png"))
if os.path.exists(fg_src):
    shutil.copy2(fg_src, os.path.join(dest, "feature_graphic_1024x500.png"))

# Copy screenshots
screens_src = os.path.join(src_root, r"play_store_assets\phone_screenshots")
if os.path.exists(screens_src):
    for f in os.listdir(screens_src):
        full_f = os.path.join(screens_src, f)
        if os.path.isfile(full_f):
            shutil.copy2(full_f, os.path.join(screens_dest, f))

# Keystore backup
keystore_src = os.path.join(src_root, r"android\app\upload-keystore.jks")
if os.path.exists(keystore_src):
    shutil.copy2(keystore_src, os.path.join(dest, "upload-keystore.jks"))

print("Copied files successfully!")
