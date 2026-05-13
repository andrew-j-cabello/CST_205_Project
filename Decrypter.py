import os
import numpy as np
from  PIL import Image
import Encrypter 
from unsplash_helper import fetch_unsplash_cover_image

API_KEY = os.getenv("UNSPLASH_API_KEY", "rxYLq6DqM9Deb7nARI5sHGdqY7bHaDj5r5Enp2sFYsI")


def decrypt(img):
    width, height = img.size
    extracted = []

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            for color in range(3):
                extracted.append(str(pixel[color] & 1))
    

    width_bits = "".join(extracted[0:32])
    height_bits = "".join(extracted[32:64])

    hidden_width = int(width_bits, 2)
    hidden_height = int(height_bits, 2)

    if hidden_width <= 0 or hidden_height <= 0 or hidden_width > width or hidden_height > height:
        raise ValueError("Extracted invalid dimensions. Is the image corrupted or unencrypted?")

    total = hidden_width * hidden_height * 3 * 8
    start = 64
    end = start + total

    pixel_bits = extracted[start:end]

    bytes_list = ["".join(pixel_bits[i:i+8]) for i in range(0, len(pixel_bits), 8)]
    pixel_values = [int(b, 2) for b in bytes_list]

    pixel_arr = np.array(pixel_values, dtype=np.uint8).reshape((hidden_height, hidden_width, 3))

    return Image.fromarray(pixel_arr)



print(f"Describe the image you want to hide:")
q = str(input())
print("Describe the carrier:")
q2 = str(input())

try:
    print("Fetching images from Unsplash API...")
    secret = fetch_unsplash_cover_image(API_KEY, q).resize((200, 150))
    carrier = fetch_unsplash_cover_image(API_KEY, q2).resize((800, 600))
    
    print(f"Hiding the {q} image inside the of the {q2} image...")
    stego_result = Encrypter.encrypt(carrier, secret)
    
    print("Extracting hidden image...")
    recovered_secret = decrypt(stego_result)
    
    print("\nProcess Complete!")
    stego_result.show(title="Carrier containing secret")
    recovered_secret.show(title="Extracted Secret")
except Exception as e:
    print(f"Failed: {e}")
