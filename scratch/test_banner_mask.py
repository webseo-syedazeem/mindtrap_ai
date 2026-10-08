from PIL import Image
import numpy as np

im = Image.open('assets/images/setting-banner.png')
arr = np.array(im)

# Let's inspect the shape
print("Array shape:", arr.shape)

# Let's find white/bright pixels in the center region (x from 280 to 1060)
center_mask = np.zeros(arr.shape[:2], dtype=bool)
center_mask[50:300, 270:1070] = True

# Letters are white (high R, G, B) and their dark outline
# In arr: R, G, B, A
r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
# White text pixels: r > 200, g > 200, b > 200
white_text = (r > 200) & (g > 200) & (b > 200) & center_mask
print("White text pixels:", np.sum(white_text))
