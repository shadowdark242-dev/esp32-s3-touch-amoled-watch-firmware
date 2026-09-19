# ESP32-S3 Touch AMOLED Watch Firmware

Custom firmware for the **Waveshare ESP32-S3-Touch-AMOLED-2.06** smartwatch development board.

This project provides a ready-to-flash firmware build with custom watch functionality and additional customization options.

## Features

- Custom watch interface
- Touchscreen support
- AMOLED display support
- Wi-Fi configuration
- Custom watch wallpapers
- Wallpaper conversion tool
- SD card based wallpaper configuration
- Firmware updates using Espressif Flash Download Tool

## Supported device

**Waveshare ESP32-S3-Touch-AMOLED-2.06**

The firmware is intended for this board.

## Download

The firmware is **free to download and use**.

Download the latest firmware from the **Releases** section:

**[Download the latest release](../../releases/latest)**

Firmware file:

```text
S3Watch_flash.bin
```

## Installation

The firmware is installed using **Espressif Flash Download Tool**.

See:

**[Flashing instructions](docs/FLASHING.md)**

Current flashing settings:

- Chip: `ESP32-S3`
- Work mode: `Develop`
- Firmware address: `0x0`
- SPI mode: `DIO`
- SPI speed: `40MHz`
- Baud rate: `115200` or `460800`

## Custom wallpapers

The watch can load a custom wallpaper from the SD card.

The wallpaper file must be named:

```text
wall.bin
```

and placed in the **root** of the SD card.

A Python conversion script is included in this repository:

```text
convert_wallpaper.py
```

The converter prepares an image for the watch display at **410 × 502 pixels** and converts it to the required RGB565 format.

See:

**[Wallpaper instructions](docs/WALLPAPER.md)**

## Wi-Fi configuration

Wi-Fi networks can be configured using a `wifi.txt` file on the root of the SD card.

Format:

```text
SSID;PASSWORD
```

One network can be specified per line.

See:

**[Wi-Fi instructions](docs/WIFI.md)**

## Documentation

| Document | Description |
|---|---|
| [Flashing instructions](docs/FLASHING.md) | Install the firmware using Flash Download Tool |
| [Wallpaper instructions](docs/WALLPAPER.md) | Create and install custom wallpapers |
| [Wi-Fi instructions](docs/WIFI.md) | Configure Wi-Fi using the SD card |
| [Changelog](CHANGELOG.md) | Firmware release history |

## Source code

The firmware source code is **not currently published**.

Only the compiled firmware is provided publicly at this time.

## Firmware

| File | Description |
|---|---|
| `S3Watch_flash.bin` | Compiled firmware for Waveshare ESP32-S3-Touch-AMOLED-2.06 |

## Important

This firmware is intended for the **Waveshare ESP32-S3-Touch-AMOLED-2.06** board.

Do not flash it to another device unless compatibility has been confirmed.

Flashing custom firmware can erase existing data or change the behavior of the device. Follow the flashing instructions carefully.

## Support the project

The firmware is free.

If you find it useful and would like to support development, you can optionally support the developer on Gumroad:

**[Support the project on Gumroad](https://shadowcaster304.gumroad.com/l/vcynfp)**

Support is voluntary. The firmware remains free.

## License

License information will be added later.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for the release history.
