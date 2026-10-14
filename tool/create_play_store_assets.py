import os
from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont

SOURCE_DIR = r"D:\mindtrap_ai-main\play_store_assets\screenshots"
OUT_SCREENSHOTS_DIR = r"D:\mindtrap_ai-main\play_store_assets\phone_screenshots"
OUT_ROOT = r"D:\mindtrap_ai-main\play_store_assets"

os.makedirs(OUT_SCREENSHOTS_DIR, exist_ok=True)

# List of input screenshot files and their polished names
SCREENS = [
    ("screen_3.png", "01_main_menu.png"),
    ("screen_6_puzzle.png", "02_puzzle_gameplay.png"),
    ("screen_4_worlds.png", "03_worlds_map.png"),
    ("screen_5_levels.png", "04_world_levels.png"),
    ("screen_7_store.png", "05_daily_rewards.png"),
    ("screen_8_auth.png", "06_cloud_sync_profile.png"),
    ("screen_1.png", "07_multilingual_56_languages.png"),
    ("screen_2.png", "08_daily_reward_claim.png"),
]

# Standard Google Play Console phone screenshot dimension: 1080 x 1920 (9:16 standard)
TARGET_WIDTH = 1080
TARGET_HEIGHT = 1920

print("Processing Screenshots for Google Play Console...")

for src_name, out_name in SCREENS:
    src_path = os.path.join(SOURCE_DIR, src_name)
    if not os.path.exists(src_path):
        print(f"Skipping {src_name} (not found)")
        continue
    
    img = Image.open(src_path)
    
    # Original is 1280 x 2856.
    # Trim top status bar (about 110 px) and bottom navigation bar (about 80 px)
    w, h = img.size
    crop_top = int(h * 0.045)  # remove status bar clock/battery
    crop_bottom = int(h * 0.035)  # remove navigation pill
    
    cropped = img.crop((0, crop_top, w, h - crop_bottom))
    
    # Fit into 1080 x 1920 using high quality LANCZOS
    # Aspect ratio crop centered
    target_ratio = TARGET_WIDTH / TARGET_HEIGHT
    crop_w, crop_h = cropped.size
    current_ratio = crop_w / crop_h
    
    if current_ratio > target_ratio:
        # too wide
        new_w = int(crop_h * target_ratio)
        offset = (crop_w - new_w) // 2
        cropped = cropped.crop((offset, 0, offset + new_w, crop_h))
    else:
        # too tall
        new_h = int(crop_w / target_ratio)
        offset = (crop_h - new_h) // 2
        cropped = cropped.crop((0, offset, crop_w, offset + new_h))
    
    final_img = cropped.resize((TARGET_WIDTH, TARGET_HEIGHT), Image.Resampling.LANCZOS)
    
    # Ensure RGB (no alpha) for Google Play Console compliance
    if final_img.mode != 'RGB':
        final_img = final_img.convert('RGB')
        
    out_path = os.path.join(OUT_SCREENSHOTS_DIR, out_name)
    final_img.save(out_path, format="PNG", optimize=True)
    print(f"Saved {out_name}: {final_img.size}")

# 2. Generate 512 x 512 High-Res App Icon
print("\nGenerating 512x512 High-Res Icon...")
logo_path = r"D:\mindtrap_ai-main\assets\images\home_logo.webp"
icon_out = os.path.join(OUT_ROOT, "icon_512x512.png")

icon_canvas = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
# Background subtle gradient or rounded card
bg_draw = ImageDraw.Draw(icon_canvas)

# Clean modern rounded squircle background
bg_draw.rounded_rectangle([16, 16, 496, 496], radius=110, fill=(240, 248, 255, 255), outline=(186, 230, 253, 255), width=6)

if os.path.exists(logo_path):
    logo = Image.open(logo_path).convert("RGBA")
    logo = logo.resize((380, 336), Image.Resampling.LANCZOS)
    # Center logo in 512x512
    pos_x = (512 - logo.width) // 2
    pos_y = (512 - logo.height) // 2
    icon_canvas.paste(logo, (pos_x, pos_y), logo)

icon_canvas.save(icon_out, format="PNG")
print(f"Saved High-Res Icon: {icon_canvas.size}")

# 3. Generate 1024 x 500 Feature Graphic
print("\nGenerating 1024x500 Feature Graphic...")
bg_path = r"D:\mindtrap_ai-main\assets\images\home_background.webp"
fg_out = os.path.join(OUT_ROOT, "feature_graphic_1024x500.png")

if os.path.exists(bg_path):
    bg = Image.open(bg_path).convert("RGB")
    # Resize & crop to 1024x500
    bg_w, bg_h = bg.size
    target_ratio = 1024 / 500
    if bg_w / bg_h > target_ratio:
        new_w = int(bg_h * target_ratio)
        offset = (bg_w - new_w) // 2
        bg_cropped = bg.crop((offset, 0, offset + new_w, bg_h))
    else:
        new_h = int(bg_w / target_ratio)
        offset = (bg_h - new_h) // 2
        bg_cropped = bg.crop((0, offset, bg_w, offset + new_h))
    
    feature_canvas = bg_cropped.resize((1024, 500), Image.Resampling.LANCZOS)
else:
    feature_canvas = Image.new("RGB", (1024, 500), (30, 58, 138))

# Overlay Game Logo in center
if os.path.exists(logo_path):
    logo = Image.open(logo_path).convert("RGBA")
    logo_w, logo_h = logo.size
    # Fit logo height ~280
    new_h = 280
    new_w = int(logo_w * (new_h / logo_h))
    logo_resized = logo.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Soft glowing card behind logo
    card_w = new_w + 140
    card_h = new_h + 80
    card_x = (1024 - card_w) // 2
    card_y = (500 - card_h) // 2
    
    card_overlay = Image.new("RGBA", (1024, 500), (0, 0, 0, 0))
    c_draw = ImageDraw.Draw(card_overlay)
    c_draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + card_h], radius=32, fill=(255, 255, 255, 225), outline=(14, 165, 233, 255), width=4)
    
    # Composite card
    feature_rgba = feature_canvas.convert("RGBA")
    feature_rgba = Image.alpha_composite(feature_rgba, card_overlay)
    
    # Composite logo
    logo_x = (1024 - new_w) // 2
    logo_y = (500 - new_h) // 2 - 20
    feature_rgba.paste(logo_resized, (logo_x, logo_y), logo_resized)
    
    # Add Title text
    t_draw = ImageDraw.Draw(feature_rgba)
    title_text = "MindTrap AI"
    sub_text = "Train Your Brain • 56 Languages"
    
    # Draw simple clean text
    feature_canvas = feature_rgba.convert("RGB")

feature_canvas.save(fg_out, format="PNG")
print(f"Saved Feature Graphic: {feature_canvas.size}")
print("\nALL GOOGLE PLAY CONSOLE ASSETS CREATED SUCCESSFULLY!")
