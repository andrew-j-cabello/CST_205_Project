import numpy as np
import requests
from  PIL import Image
from io import BytesIO
import Encrypter
import GUI

key = "rxYLq6DqM9Deb7nARI5sHGdqY7bHaDj5r5Enp2sFYsI"
# q = "Large neon city"
# q2 = "Small quiet town"

def get_unsplash_image(api_key, search_query):
    url = "https://api.unsplash.com/search/photos"

    params = {
        "query": search_query,
        "client_id": api_key,
        "per_page": 1
    }
    
    resp = requests.get(url, params=params)
    if resp.status_code != 200:
        raise Exception(f"API Error: {resp.status_code} - {resp.text}")
        
    data = resp.json()
    if not data['results']:
        raise Exception("No images found for this query.")
        
    image_url = data['results'][0]['urls']['regular']

    img_resp = requests.get(image_url)
    return Image.open(BytesIO(img_resp.content)).convert("RGB")


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


# def stego_encrypt(carrier_img, secret_img):
#     c_width, c_height = carrier_img.size
#     s_width, s_height = secret_img.size
    
#     header = f"{s_width:032b}{s_height:032b}"
    
#     secret_data = list(secret_img.getdata())
#     pixel_bits = "".join([f"{c:08b}" for p in secret_data for c in p])
    
#     all_bits = header + pixel_bits
#     if len(all_bits) > c_width * c_height * 3:
#         raise ValueError("Secret image too large.")
        
#     stego_img = carrier_img.copy()
#     pixels = list(stego_img.getdata())
#     new_pixels = []
    
#     bit_idx = 0
#     for p in pixels:
#         new_p = list(p)
#         for i in range(3):
#             if bit_idx < len(all_bits):
#                 new_p[i] = (new_p[i] & ~1) | int(all_bits[bit_idx])
#                 bit_idx += 1
#         new_pixels.append(tuple(new_p))
        
#     stego_img.putdata(new_pixels)
#     return stego_img

# try:
#     print("Fetching images from Unsplash API...")
#     secret = get_unsplash_image(key, q).resize((200, 150))
#     carrier = get_unsplash_image(key, q2).resize((800, 600))
    
#     print("Hiding the beach image inside the forest image...")
#     stego_result = stego_encrypt(carrier, secret)
    
#     print("Extracting hidden image...")
#     recovered_secret = decrypt(stego_result)
    
#     print("\nProcess Complete!")
#     stego_result.show(title="Carrier containing secret")
#     recovered_secret.show(title="Extracted Secret")
# except Exception as e:
#     print(f"Failed: {e}")
