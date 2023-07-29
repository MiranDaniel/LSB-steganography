from PIL import Image
import numpy as np
import argparse

def _write_bit_plane(image_array, bit_plane_array, plane_number):
    return (image_array & ~(1 << plane_number)) | (bit_plane_array << plane_number)

def write(input_image, message, output):
    img = Image.open(input_image)
    data = np.array(img)

    binary_message = [int(bit) for char in message for bit in f"{ord(char):08b}"]

    if len(binary_message) > img.width * img.height * 3:
        raise ValueError("The secret message is too large to hide in the image.")

    # Add padding to the binary message to match the image size
    padding_length = img.width * img.height * 3 - len(binary_message)
    binary_message += [0] * padding_length

    # Reshape the binary message to match the image dimensions
    binary_message_array = np.array(binary_message).reshape(img.height, img.width, 3)

    # Write the binary message to the 0th bit plane of the image
    stego_image_data = _write_bit_plane(data, binary_message_array, plane_number=0)

    # Create a new image with the stego data
    stego_image = Image.fromarray(stego_image_data.astype(np.uint8))

    # Save the stego image
    stego_image.save(output)
