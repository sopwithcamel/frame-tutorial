# ============================================================
# Module 3: Potions Class!
# ============================================================
# Time to mix some potions using Python Math!
# You can use +, -, * and / to change your colors.

import asyncio
from PIL import Image
from idotmatrix import ConnectionManager, Gif

FRAME_ADDRESS = "AF:32:CD:F6:81:30"

async def brew_potion():
    # We start with a base of water (clear/black)
    base_red = 0
    base_green = 0
    base_blue = 0
    
    # -----------------------------------------------------------
    # ADD YOUR INGREDIENTS HERE!
    # -----------------------------------------------------------
    print("Brewing a Polyjuice Potion...")
    
    # Recipe Step 1: Add some Lacewing Flies (adds 50 Green)
    base_green = base_green + 50
    
    # Recipe Step 2: Add Leeches (adds 100 Red)
    base_red = base_red + 100
    
    # Recipe Step 3: Add Boomslang Skin (multiplies Green by 2!)
    base_green = base_green * 2
    
    # Recipe Step 4: Create your own ingredient!
    # Tip: Make sure no single color goes above 255 or below 0.
    
    
    # -----------------------------------------------------------
    # The cauldron finishes brewing
    # -----------------------------------------------------------
    final_potion = (base_red, base_green, base_blue)
    print(f"Your final potion color is: {final_potion}")
    
    image = Image.new("RGB", (64, 64), final_potion)
    image.save("potion.gif")
    
    conn = ConnectionManager()
    await conn.connectByAddress(FRAME_ADDRESS)
    gif = Gif()
    await gif.uploadUnprocessed("potion.gif")
    print("Potion complete! Check the cauldron (frame) 🧪")

asyncio.run(brew_potion())
