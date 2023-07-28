from lsb import extract
from PIL import Image
import numpy as np


INPUT_IMAGE = "./sample_images/cat.png"
START_BIT = 0
END_BIT = 2
SAVE_EACH_BIT = False
COLOR = True

OUTPUT_DIR = "./output/"


def combine_bit_planes(bit_planes, start_bit, end_bit):
    combined_channel = np.zeros_like(bit_planes[0], dtype=np.uint8)
    for i in range(start_bit, end_bit + 1):
        combined_channel |= bit_planes[i]
    return combined_channel

def histogram_equalization(combined_channel):
    # Apply histogram equalization to enhance contrast
    hist, bins = np.histogram(combined_channel.flatten(), bins=256, range=[0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()
    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    enhanced_channel = cdf[combined_channel]

    return enhanced_channel

img = Image.open(INPUT_IMAGE)
data = np.array(img)

# Separate RGB channels
R, G, B = data[:, :, 0], data[:, :, 1], data[:, :, 2]

# Get bit planes for each channel
R_bit_planes = extract.get_bit_plane(R)
G_bit_planes = extract.get_bit_plane(G)
B_bit_planes = extract.get_bit_plane(B)
C_bit_planes = extract.get_bit_plane(R | G | B)

# Combine bit planes for each channel
R_combined = combine_bit_planes(R_bit_planes, START_BIT, END_BIT)
G_combined = combine_bit_planes(G_bit_planes, START_BIT, END_BIT)
B_combined = combine_bit_planes(B_bit_planes, START_BIT, END_BIT)
C_combined = combine_bit_planes(C_bit_planes, START_BIT, END_BIT)

# Enhance visibility for each color channel using histogram equalization
R_enhanced = histogram_equalization(R_combined)
G_enhanced = histogram_equalization(G_combined)
B_enhanced = histogram_equalization(B_combined)
C_enhanced = histogram_equalization(C_combined)

if COLOR:
    # Create secret images for each channel with the correct colors
    secret_R_img = Image.fromarray(np.stack((R_enhanced, np.zeros_like(G_enhanced), np.zeros_like(B_enhanced)), axis=2))
    secret_G_img = Image.fromarray(np.stack((np.zeros_like(R_enhanced), G_enhanced, np.zeros_like(B_enhanced)), axis=2))
    secret_B_img = Image.fromarray(np.stack((np.zeros_like(R_enhanced), np.zeros_like(G_enhanced), B_enhanced), axis=2))
    secret_C_img = Image.fromarray(np.stack((R_enhanced, G_enhanced, B_enhanced), axis=2))
else:
    secret_R_img = Image.fromarray(R_enhanced)
    secret_G_img = Image.fromarray(G_enhanced)
    secret_B_img = Image.fromarray(B_enhanced)
    secret_C_img = Image.fromarray(C_enhanced)

# Save the secret images to the output directory
secret_R_img.save(OUTPUT_DIR + "secret_red.png")
secret_G_img.save(OUTPUT_DIR + "secret_green.png")
secret_B_img.save(OUTPUT_DIR + "secret_blue.png")
secret_C_img.save(OUTPUT_DIR + "secret_combined.png")

if not SAVE_EACH_BIT:
    quit(0)

# Optionally, you can also save the combined bit planes as images for visual reference
for i in range(8):
    combined_img = Image.fromarray((combine_bit_planes(R_bit_planes, i, i) * 255).astype(np.uint8))
    combined_img.save(OUTPUT_DIR + f"R_bit_plane_{i}.png")
    
    combined_img = Image.fromarray((combine_bit_planes(G_bit_planes, i, i) * 255).astype(np.uint8))
    combined_img.save(OUTPUT_DIR + f"G_bit_plane_{i}.png")
    
    combined_img = Image.fromarray((combine_bit_planes(B_bit_planes, i, i) * 255).astype(np.uint8))
    combined_img.save(OUTPUT_DIR + f"B_bit_plane_{i}.png")
