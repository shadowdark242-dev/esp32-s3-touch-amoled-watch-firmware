# Flashing instructions

This guide explains how to install `S3Watch_flash.bin` using Espressif Flash Download Tool.

## Before you start

You will need:

- Waveshare ESP32-S3-Touch-AMOLED-2.06 watch development board
- USB data cable
- Espressif Flash Download Tool
- Firmware file: `S3Watch_flash.bin`

Download the firmware from the **Assets** section of the latest GitHub Release.

Download Flash Download Tool from the [official Espressif tools page](https://www.espressif.com/en/support/download/other-tools).

## 1. Connect the watch

1. Connect the watch to your computer with a USB data cable.
2. Open Windows Device Manager.
3. Find the new COM port and note its number.

If no COM port appears, try another USB cable or check whether the required USB-UART driver is installed.

## 2. Open Flash Download Tool

Start Flash Download Tool.

Select these options:

- **ChipType:** `ESP32-S3`
- **WorkMode:** `Develop`

Click **OK**.

## 3. Select the firmware file

In the file list:

1. Click the file selection field in the first row.
2. Select `S3Watch_flash.bin`.
3. Enter `0x0` in the address field next to it.
4. Check the box at the left of that row to enable the file.

Use this single firmware file. Do not add the old file name `S3Watch_merged.bin`.

## 4. Set the flashing options

Set the options on the right:

- **SPI SPEED:** `40MHz`
- **SPI MODE:** `DIO`
- **COM:** the port identified in Step 1
- **BAUD:** `115200` or `460800`

You can try `460800` for a faster flash. If flashing fails, select `115200` and try again.

If you have previously flashed this same watch with the tool, you can use the same settings that worked before.

## 5. Flash the firmware

1. Double-check the selected file, address, COM port, and settings.
2. Click **START**.
3. Wait until the tool reports `FINISH`.

Do not disconnect the watch while flashing is in progress.

## 6. Restart and check the watch

When flashing is complete:

1. Disconnect and reconnect the watch, or press its reset button if available.
2. Wait for the watch to start.
3. Check that the display and expected firmware features work.

## Troubleshooting

### “Failed to connect”

Try holding the board's **BOOT** button while clicking **START**. Release it a second or two after flashing begins.

### COM port not found

Check Windows Device Manager. A USB-UART driver may be required, depending on the board and USB interface.

### Flashing freezes or fails partway through

- Try a lower baud rate: `115200`.
- Try a shorter or better-quality USB cable.
- Check that no other program is using the COM port.

If the problem continues, note the exact error message and the settings used.

## Important

Use this firmware only with the intended Waveshare ESP32-S3-Touch-AMOLED-2.06 board. Flashing custom firmware may erase existing data or affect device behavior.

The firmware source code is not currently published.
