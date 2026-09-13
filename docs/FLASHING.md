# Flashing instructions

This guide describes the general workflow for flashing `S3Watch_flash.bin` with ESP Flash Download Tool.

## Before you start

- Waveshare ESP32-S3-Touch-AMOLED-2.06 board
- USB data cable
- ESP Flash Download Tool
- `S3Watch_flash.bin` from the matching GitHub release

Use a cable that supports data, not charging only.

## Important: flash settings

The correct flash address and other settings depend on the exact firmware build.

**Use the address and settings explicitly provided in the release notes or in a configuration file included with that release. Do not guess them.** If no address or settings are provided, stop and ask the firmware maintainer before flashing.

## General procedure

1. Download `S3Watch_flash.bin` from the release's **Assets** section.
2. Start ESP Flash Download Tool.
3. Select the ESP32-S3 target if the tool asks for the chip.
4. Add the downloaded `S3Watch_flash.bin` to the file list.
5. Enter the flash address and select other options exactly as specified for that release.
6. Connect the watch to the computer with a USB data cable.
7. Select the correct serial port.
8. Start the flashing process and wait for the tool to report success.
9. Disconnect or restart the board as appropriate for the tool and board.
10. Check that the watch starts and that the expected features work.

## If flashing fails

- Confirm that the USB cable supports data.
- Check that the selected serial port belongs to the connected board.
- Close other programs that may be using the serial port.
- Recheck the chip selection and the release-specific flash settings.
- Do not try random flash addresses or settings.

If the problem continues, open a GitHub issue and include the release version, the error message, and the steps that led to the failure. Do not include private information.
