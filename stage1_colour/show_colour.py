# ============================================================
# Stage 1: Light up the frame with your favourite colour!
# ============================================================
# Welcome, Nishtha! This is your very first Python programme.
# In Python, lines that start with # are called "comments".
# The computer ignores them -- they are just notes for humans.


# First, we bring in some tools that other people wrote for us.
# This is like borrowing someone's art set instead of making
# your own from scratch.
import asyncio                        # helps us wait for things
from PIL import Image                 # lets us create pictures
from idotmatrix import ConnectionManager, Gif  # talks to our frame


# -----------------------------------------------------------
# THIS IS THE FUN PART -- change this to change the colour!
# -----------------------------------------------------------
# A colour is made of three numbers, each between 0 and 255.
# The first number is how much RED.
# The second number is how much GREEN.
# The third number is how much BLUE.
#
# Try these out:
#   (255,   0,   0)  -- bright red
#   (  0, 255,   0)  -- bright green
#   (  0,   0, 255)  -- bright blue
#   (255, 255,   0)  -- yellow
#   (255,   0, 255)  -- pink / magenta
#   (  0, 255, 255)  -- cyan
#   (255, 165,   0)  -- orange
#   (255, 255, 255)  -- white
#   (  0,   0,   0)  -- off (black)

my_colour = (255, 0, 255)  # <-- change me!


# This is the "address" of our LED frame -- like its phone number.
# We need it so the Raspberry Pi knows which device to talk to.
FRAME_ADDRESS = "AF:32:CD:F6:81:30"


# -----------------------------------------------------------
# Everything below here makes the magic happen.
# You don't need to change any of this for Stage 1.
# -----------------------------------------------------------

async def show_colour(colour):
    # Step 1: Create a 64x64 picture filled with our colour.
    # 64x64 means 64 dots across and 64 dots tall.
    image = Image.new("RGB", (64, 64), colour)

    # Step 2: Save that picture as a file on the Pi.
    image.save("my_colour.gif")
    print("Colour picture created!")

    # Step 3: Connect to the frame over Bluetooth.
    print("Connecting to the frame...")
    conn = ConnectionManager()
    await conn.connectByAddress(FRAME_ADDRESS)
    print("Connected!")

    # Step 4: Send our picture to the frame.
    gif = Gif()
    await gif.uploadUnprocessed("my_colour.gif")
    print("Done! Look at the frame! 🎨")


# This line is the "on" switch -- it starts the whole programme.
asyncio.run(show_colour(my_colour))
