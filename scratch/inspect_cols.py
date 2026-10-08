from PIL import Image
import sys
sys.stdout.reconfigure(encoding='utf-8')

im = Image.open('assets/images/setting-banner.png')
w, h = im.size

# Let's inspect column x=270 (just before the first letter 'S') and x=1070 (just after the last letter 'S')
col_left = [im.getpixel((270, y)) for y in range(h)]
col_right = [im.getpixel((1070, y)) for y in range(h)]

print("Banner height at x=270:", sum(1 for p in col_left if p[3] > 100))
print("Banner height at x=1070:", sum(1 for p in col_right if p[3] > 100))
