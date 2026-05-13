"""
LSB image-in-image hiding compatible with `Decrypter.decrypt`.

Format written into cover image LSBs:
1) 32 bits: hidden image width
2) 32 bits: hidden image height
3) hidden image RGB bytes (8 bits per channel)
"""

from pathlib import Path

from PIL import Image
from unsplash_helper import fetch_unsplash__image


def _hidden_image_bits(hidden_img):
    rgb = hidden_img.convert("RGB")
    w, h = rgb.size
    return f"{w:032b}{h:032b}" + "".join(
        f"{channel:08b}" for px in rgb.get_flattened_data() for channel in px
    )


def encrypt(cover_img, hidden_img):
    cover = cover_img.convert("RGB")
    bits = _hidden_image_bits(hidden_img)

    capacity = cover.width * cover.height * 3
    if len(bits) > capacity:
        raise ValueError(
            f"Cover image too small. Need {len(bits)} bits, but only {capacity} bits available."
        )

    bit_index = 0
    updated_pixels = []
    for r, g, b in cover.get_flattened_data():
        channels = [r, g, b]
        for i in range(3):
            if bit_index < len(bits):
                channels[i] = (channels[i] & ~1) | int(bits[bit_index])
                bit_index += 1
        updated_pixels.append(tuple(channels))

    stego = Image.new("RGB", cover.size)
    stego.putdata(updated_pixels)
    return stego


def encrypt_from_paths(cover_path, hidden_path, output_path):
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    cover_img = Image.open(cover_path).convert("RGB")
    hidden_img = Image.open(hidden_path).convert("RGB")
    encrypt(cover_img, hidden_img).save(out, format="PNG")


def encrypt_from_unsplash(
    hidden_path,
    output_path,
    access_key=None,
    query=None,
):
    cover = fetch_unsplash__image(access_key=access_key, query=query)
    hidden_img = Image.open(hidden_path).convert("RGB")
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    encrypt(cover, hidden_img).save(out, format="PNG")
