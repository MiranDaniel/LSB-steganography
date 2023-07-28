from PIL import Image
from lsb import extract
import numpy as np

INPUT_IMAGE = "./sample_images/lichtenstein_message.png"
START_BIT = 0
END_BIT = 0

def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')

img = Image.open(INPUT_IMAGE)
data = np.array(img)

R, G, B = data[:, :, 0], data[:, :, 1], data[:, :, 2]

bit_planes_r = extract.get_bit_plane(R)
bit_planes_g = extract.get_bit_plane(G)
bit_planes_b = extract.get_bit_plane(B)

# Combine the LSBs to reconstruct the hidden message
def get_message_from_bit_plane(bit_plane_red, bit_plane_green, bit_plane_blue):
    bits = []
    for i in range(img.height):
        for j in range(img.width):
            bits.append(bit_plane_red[i][j] & 1)
            bits.append(bit_plane_green[i][j] & 1)
            bits.append(bit_plane_blue[i][j] & 1)

    bytes_ = bitstring_to_bytes("".join([str(i) for i in bits]))
    return bytes_.decode("utf-8", "ignore")

message = ""
for i in range(START_BIT, END_BIT+1):
    message += get_message_from_bit_plane(
        bit_planes_r[i],
        bit_planes_g[i],
        bit_planes_b[i],
    )
print(message)
