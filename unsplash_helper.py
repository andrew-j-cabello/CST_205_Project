import os
from io import BytesIO
import requests
from PIL import Image

'''
This should return a random image from unsplash
'''
def fetch_unsplash__image(access_key=None, query=None):
    key = access_key or os.environ.get("UNSPLASH_ACCESS_KEY")
    if not key:
        raise ValueError("Set UNSPLASH_ACCESS_KEY or pass access_key=...")

    params = {"query": query} if query else None
    meta = requests.get(
        "https://api.unsplash.com/photos/random",
        headers={"Authorization": f"Client-ID {key}"},
        params=params,
        timeout=30,
    ).json()

    src = (meta.get("urls") or {}).get("regular")
    if not src:
        raise RuntimeError("Unsplash response had no image URL.")

    img_bytes = requests.get(src, timeout=30).content
    return Image.open(BytesIO(img_bytes)).convert("RGB")
