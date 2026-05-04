import numpy as np
import requests
from  PIL import Image



key = ''
q = ''
url = f"https://unsplash.com{q}&client_id{key}"

resp = requests.get(url)

if resp.status_code == 200:
    data = resp.json()
    first_image = data['results'][0]['urls']['regular']
    print(f"Image URL: {first_image}")
else:
    print(f"Error: {resp.status_code}")


def decrypt():
    # TODO: Fix the following source code, discuss with partners
    extracted = []
    with Image.open("this_img.png") as img:
        width, height = img.size
        byte = []
        for x in range(0, width):
            for y in range(0, height):
                pixel = list(img.getpizel((x,y)))
                for n in range(0,3):
                    extracted.append(pixel[n]&1)
    data = "".join([str(x) for x in extracted])
    return data