from PIL import Image
import sys
sys.stdout.reconfigure(encoding='utf-8')

im = Image.open('assets/images/setting-banner.png')
print("Image size:", im.size)
print("Image mode:", im.mode)

# Let's inspect center vs edges
# Let's save a thumbnail or inspect average colors
center_crop = im.crop((im.width*0.2, im.height*0.2, im.width*0.8, im.height*0.8))
colors = im.getcolors(maxcolors=100000)
print("Unique colors:", len(colors) if colors else "> 100000")
