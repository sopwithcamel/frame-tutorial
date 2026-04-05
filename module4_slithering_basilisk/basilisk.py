# ============================================================
# Module 4: The Slithering Basilisk!
# ============================================================
# In this module, you will learn about 'for' loops to do things
# over and over again perfectly. We will use a for loop to make
# a snake grow frame by frame and save it as an animation.

import asyncio
from PIL import Image
from idotmatrix import ConnectionManager, Gif

FRAME_ADDRESS = "AF:32:CD:F6:81:30"

async def summon_basilisk():
    frames = []
    
    # -----------------------------------------------------------
    # WATCH THE BASILISK GROW!
    # -----------------------------------------------------------
    # We will make the snake start at column 0 and end at column 40.
    # The 'range(40)' gives us numbers 0, 1, 2... up to 39.
    
    for length in range(40):
        # Create a new blank frame for this moment in time
        background = (0, 0, 0)
        image = Image.new("RGB", (64, 64), background)
        
        # Now draw the snake up to the current 'length'
        for i in range(length):
            # The snake Slithers across row 32, turning those pixels green
            image.putpixel((i, 32), (0, 255, 0)) # Green Basilisk!
            
        # Add this picture to our list of frames
        frames.append(image)

    print(f"Created {len(frames)} frames of the snake slithering.")

    # -----------------------------------------------------------
    # Save the animation and send to frame
    # -----------------------------------------------------------
    frames[0].save(
        "basilisk.gif",
        save_all=True,
        append_images=frames[1:],
        loop=0,
        duration=100, # 100 milliseconds per frame
        format="GIF",
    )
    print("Animation saved!")
    
    # Connect and upload
    print("Connecting to frame...")
    conn = ConnectionManager()
    await conn.connectByAddress(FRAME_ADDRESS)
    
    gif = Gif()
    await gif.uploadUnprocessed("basilisk.gif")
    print("The Chamber of Secrets is open! Watch the Basilisk slither... 🐍")

asyncio.run(summon_basilisk())
