# ============================================================
# Module 2: Wand Sparks!
# ============================================================
# Welcome to Charms Class! Today we will learn about coordinates.
# The screen is like a grid of 64 columns and 64 rows.
# (0, 0) is the top-left corner.
# (63, 63) is the bottom-right corner.

import asyncio
from PIL import Image
from idotmatrix import ConnectionManager, Gif

FRAME_ADDRESS = "AF:32:CD:F6:81:30"

async def cast_sparks():
    # We start with a dark screen (black)
    background_color = (0, 0, 0)
    image = Image.new("RGB", (64, 64), background_color)
    
    # -----------------------------------------------------------
    # ADD YOUR WAND SPARKS HERE!
    # -----------------------------------------------------------
    # Use image.putpixel((x, y), (R, G, B)) to turn on specific dots.
    # Replace the x and y with numbers between 0 and 63.
    # Replace R, G, B with your favorite colors!
    
    # Example spark:
    image.putpixel((10, 10), (255, 255, 0)) # A yellow spark near the top-left
    
    # Add more sparks!
    image.putpixel((32, 32), (255, 0, 255)) # A pink spark in the middle
    image.putpixel((50, 50), (0, 255, 255)) # A cyan spark near the bottom-right
    
    # Try adding 5 more sparks of your own below!
    
    
    
    # -----------------------------------------------------------
    # Send the magic to the frame
    # -----------------------------------------------------------
    image.save("sparks.gif")
    print("Casting the spell...")
    conn = ConnectionManager()
    await conn.connectByAddress(FRAME_ADDRESS)
    
    gif = Gif()
    await gif.uploadUnprocessed("sparks.gif")
    print("Sparks are flying! ✨ Check the frame!")

asyncio.run(cast_sparks())
