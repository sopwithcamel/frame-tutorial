# ============================================================
# Module 1: The Sorting Hat!
# ============================================================
# Welcome, Nishtha! You are about to be sorted into your
# Hogwarts House!
#
# In Python, we have tools to pick things randomly, like the Hat does!

import asyncio
import random
from PIL import Image
from idotmatrix import ConnectionManager, Gif

# This is the "address" of our LED frame, the Marauder's Map to finding it.
FRAME_ADDRESS = "AF:32:CD:F6:81:30"

# -----------------------------------------------------------
# UNDERSTANDING RANDOM NUMBERS!
# -----------------------------------------------------------
# We have a list of all 4 Hogwarts house colors.
# Lists always start counting from 0 instead of 1 in Python!
house_colors = [
    (255, 0, 0),    # 0 = Gryffindor (Red)
    (0, 255, 0),    # 1 = Slytherin (Green)
    (0, 0, 255),    # 2 = Ravenclaw (Blue)
    (255, 255, 0)   # 3 = Hufflepuff (Yellow)
]

# Pick a random number between 0 and 3
# Challenge: Can you change the numbers here so it only picks 
# between Gryffindor (0) and Slytherin (1)?
random_number = random.randint(0, 3) 

# We use the random number to select a color from our 'house_colors' list
chosen_color = house_colors[random_number]

# -----------------------------------------------------------
# The Magic Spell (Don't change this part yet!)
# -----------------------------------------------------------
async def sorting_hat(color, house_number):
    print("Connecting to the magical frame...")
    conn = ConnectionManager()
    await conn.connectByAddress(FRAME_ADDRESS)
    print("Connected!")
    
    gif = Gif()

    # Step 1: Open the Sorting Hat picture and show it!
    # (Make sure 'sorting_hat.png' is saved in this folder!)
    try:
        hat_image = Image.open("sorting_hat.png").convert("RGB")
        # Resize it to perfectly fit the 64x64 frame
        hat_image = hat_image.resize((64, 64))
        hat_image.save("hat_resized.gif")
        
        await gif.uploadUnprocessed("hat_resized.gif")
        print("The Sorting Hat is thinking...")
        
        # Wait in suspense for 3 seconds!
        await asyncio.sleep(3)
    except FileNotFoundError:
        print("Could not find sorting_hat.png, but the hat is still thinking...")

    # Step 2: Show your new House color!
    color_image = Image.new("RGB", (64, 64), color)
    color_image.save("house_color.gif")
    await gif.uploadUnprocessed("house_color.gif")
    
    # Step 3: Let's announce the house!
    if house_number == 0:
        print("Ah, right then... I see... G R Y F F I N D O R !")
    elif house_number == 1:
        print("Hm, very cunning... S L Y T H E R I N !")
    elif house_number == 2:
        print("Very clever indeed... R A V E N C L A W !")
    elif house_number == 3:
        print("Loyal and just... H U F F L E P U F F !")

# Cast the spell!
asyncio.run(sorting_hat(chosen_color, random_number))
