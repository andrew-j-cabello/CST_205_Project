import os
from io import BytesIO
import requests
from PIL import Image

'''
This should return a random image from unsplash
'''
def fetch_unsplash_cover_image(access_key=None, query=None):
    key = access_key or os.environ.get("UNSPLASH_ACCESS_KEY")
    if not key:
        raise ValueError("Set UNSPLASH_ACCESS_KEY or pass access_key=...")

    q = query or "(no query, random photo)"
    print(f"[unsplash] Requesting random photo: {q}")
    params = {"query": query} if query else None
    meta = requests.get(
        "https://api.unsplash.com/photos/random",
        headers={"Authorization": f"Client-ID {key}"},
        params=params,
        timeout=30,
    ).json()

    photo_id = meta.get("id", "?")
    src = (meta.get("urls") or {}).get("regular")
    if not src:
        raise RuntimeError("Unsplash response had no image URL.")

    print(f"Got photo id={photo_id}, downloading image bytes...")
    img_bytes = requests.get(src, timeout=30).content
    print(f"Downloaded opening as RGB")
    return Image.open(BytesIO(img_bytes)).convert("RGB")
