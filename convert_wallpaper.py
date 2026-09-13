#!/usr/bin/env python3
"""
Image converter to the wall.bin wallpaper format for the watch (S3Watch).

File format:
  4 bytes  — magic "WBMP"
  2 bytes  — width (uint16, little-endian)
  2 bytes  — height (uint16, little-endian)
  then     — raw RGB565 pixels (little-endian), row by row

Usage:
  python3 convert_wallpaper.py input_image.jpg wall.bin

Copy the resulting wall.bin to the root of the watch's SD card.
Requires: pip install pillow
"""
import sys
import struct
from PIL import Image

TARGET_W = 410
TARGET_H = 502


def convert_to_wbmp(src_path, dst_path, target_w=TARGET_W, target_h=TARGET_H):
    im = Image.open(src_path).convert('RGB')
    w, h = im.size

    canvas = Image.new('RGB', (target_w, target_h), (0, 0, 0))
    resized = im.resize((target_w, int(h * target_w / w)), Image.LANCZOS) if w != target_w else im
    if resized.height > target_h:
        resized = resized.crop((0, 0, target_w, target_h))
    y_off = max(0, (target_h - resized.height) // 2)
    canvas.paste(resized, (0, y_off))

    px = canvas.load()
    with open(dst_path, 'wb') as f:
        f.write(b'WBMP')
        f.write(struct.pack('<HH', target_w, target_h))
        for y in range(target_h):
            row = bytearray()
            for x in range(target_w):
                r, g, b = px[x, y]
                rgb565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
                row += struct.pack('<H', rgb565)
            f.write(row)
    print(f"OK: {dst_path} ({target_w}x{target_h}, {target_w*target_h*2 + 8} bytes)")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 convert_wallpaper.py input_image.jpg wall.bin")
        sys.exit(1)
    convert_to_wbmp(sys.argv[1], sys.argv[2])
