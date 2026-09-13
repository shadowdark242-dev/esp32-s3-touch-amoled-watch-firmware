HOW TO CHANGE THE WATCH WALLPAPER
====================================

The watch reads a file called /wall.bin from the SD card and shows it
as the watchface background. If the file is missing (or corrupted /
wrong size) — it falls back to the built-in image from the firmware.

You do NOT need to reflash the firmware — just replace the file on
the card.


STEP 1. Install Python and Pillow (one-time setup)
------------------------------------------------------
If you don't have Python yet — download it from
https://www.python.org
During installation, check the box "Add Python to PATH".

Then, in Command Prompt / PowerShell, run this once:

    pip install pillow


STEP 2. Convert your image
------------------------------
You'll need the convert_wallpaper.py script (provided separately).

Put your image (jpg/png — any size, the script will resize it) next
to the script, then run in the command line:

    python convert_wallpaper.py my_picture.jpg wall.bin

The script will automatically:
  - resize the image to fit the screen (410 x 502)
  - crop/pad the edges if the proportions don't match
  - convert it to the format the watch understands (RGB565)

This produces a file called wall.bin — that's the one you need to
copy to the card.


STEP 3. Copy the file to the SD card
----------------------------------------
  1. Remove the SD card from the watch (or connect it via a USB
     card reader)
  2. Copy wall.bin to the ROOT of the card (not into a folder!)
  3. If there's already an old wall.bin there — just overwrite it


STEP 4. Put the card back in and turn the watch on
-------------------------------------------------------
The new wallpaper will appear right away on the next boot.

If the picture didn't change — possible reasons:
  - the file isn't named exactly "wall.bin" (double-check the exact
    name on the card)
  - the file is inside a subfolder instead of the root
  - the file is corrupted / wasn't copied completely
  - the card isn't seated properly / bad contact

Important: the filename must be EXACTLY "wall.bin", not longer.
A longer name (like "wallpaper.bin") won't be found — the card is
formatted without long filename support, so only short names
(max 8 characters before the dot) are visible.

In any of these cases the watch will simply show the regular
built-in picture instead — there's no crash or freeze from a bad
file.


TECHNICAL DETAILS (for reference, not required reading)
-------------------------------------------------------------
wall.bin format:
  bytes 0-3   — magic signature "WBMP"
  bytes 4-5   — image width, 2-byte number
  bytes 6-7   — image height, 2-byte number
  after that  — the raw pixels, RGB565 format, no compression

Expected size: exactly 410 x 502 pixels (matching the watch screen).
Resulting file size: about 400 KB.
