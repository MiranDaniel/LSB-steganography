from lsb import extract
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("src", help="Source location")
args = parser.parse_args()
config = vars(args)

INPUT_IMAGE = config["src"]


img = Image.open(INPUT_IMAGE)
data = np.array(img)

R, G, B = data[:, :, 0], data[:, :, 1], data[:, :, 2]

R_bit_planes = [extract.get_bit_plane(R)]
G_bit_planes = [extract.get_bit_plane(G)]
B_bit_planes = [extract.get_bit_plane(B)]

combined_bit_planes = [extract.get_bit_plane(R | G | B)]

fig, axes = plt.subplots(4, 8, figsize=(15, 6))

for i in range(8):
    axes[0, i].imshow((R_bit_planes[0][i] * 255).astype(np.uint8), cmap='Reds')
    axes[0, i].axis('off')
    axes[0, i].set_title(f"R Bit {i}")
    
    axes[1, i].imshow((G_bit_planes[0][i] * 255).astype(np.uint8), cmap='Greens')
    axes[1, i].axis('off')
    axes[1, i].set_title(f"G Bit {i}")
    
    axes[2, i].imshow((B_bit_planes[0][i] * 255).astype(np.uint8), cmap='Blues')
    axes[2, i].axis('off')
    axes[2, i].set_title(f"B Bit {i}")
    
    axes[3, i].imshow((combined_bit_planes[0][i] * 255).astype(np.uint8), cmap='binary')
    axes[3, i].axis('off')
    axes[3, i].set_title(f"Combined Bit {i}")

plt.tight_layout()
plt.savefig("./output/bitplanes.png")
plt.show()
