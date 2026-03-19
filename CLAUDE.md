# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A Python project for controlling an iDotMatrix 64x64 LED matrix display over Bluetooth. Uses the `idotmatrix` library and `asyncio` for async Bluetooth communication.

## Running Code

```bash
python3 stage1_colour/show_colour.py   # Display a solid color
python3 examples/nyan_cat.py           # Fetch and display animated Nyan Cat GIF
```

No build step, no tests, no linter configured.

## Dependencies

Install manually (no requirements.txt):
```bash
pip install idotmatrix Pillow
```

## Architecture

Both scripts follow the same pattern:
1. Create or fetch an image (PIL/Pillow)
2. Save/convert to GIF format
3. Connect to the iDotMatrix device via Bluetooth using `asyncio.run()`
4. Send the image using the `idotmatrix` client

**Device address** (hardcoded in both files): `AF:32:CD:F6:81:30`
**Display resolution**: 64×64 pixels

The `idotmatrix` library handles the Bluetooth protocol. All device interaction is async.
