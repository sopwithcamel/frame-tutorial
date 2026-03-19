# ============================================================
# Stage 3: Write your name on the frame!
# ============================================================
# You are doing brilliantly, Nishtha!  This stage will put
# text on the frame -- like a tiny LED name badge.
#
# New things you will learn in this stage:
#   - Strings  (text in Python, written inside " " quotes)
#   - Coordinates  (x and y positions on the screen)
#   - Using ImageDraw to write text


import asyncio
from PIL import Image, ImageDraw, ImageFont
from idotmatrix import ConnectionManager, Gif


# -----------------------------------------------------------
# THIS IS THE FUN PART -- change these three things!
# -----------------------------------------------------------

my_name = "Nishtha"           # <-- put your name here (keep the quotes)

background_colour = (  0,   0, 128)   # the colour behind the text (dark blue)
text_colour       = (255, 255,   0)   # the colour of the letters   (yellow)

# Colour ideas for the background:
#   (  0,   0,   0)  -- black
#   (128,   0,   0)  -- dark red
#   (  0, 128,   0)  -- dark green
#
# Colour ideas for the text:
#   (255, 255, 255)  -- white
#   (255, 165,   0)  -- orange
#   (255,   0, 255)  -- pink


FRAME_ADDRESS = "AF:32:CD:F6:81:30"


# -----------------------------------------------------------
# Everything below here makes the magic happen.
# -----------------------------------------------------------

async def show_name(name, bg, fg):
    # Step 1: Create a picture filled with the background colour.
    image = Image.new("RGB", (64, 64), bg)

    # Step 2: Get a drawing pen.
    draw = ImageDraw.Draw(image)

    # Step 3: Load a font.
    # load_default() gives us a simple built-in font.
    # Each letter is about 6 pixels wide and 8 pixels tall.
    font = ImageFont.load_default()

    # Step 4: Work out where to put the text so it is centred.
    # Coordinates on the screen work like this:
    #
    #   (0,0) -----> x increases this way ---> (63, 0)
    #     |
    #     |  y increases downwards
    #     |
    #   (0,63)                                 (63,63)
    #
    # We want the text to sit roughly in the middle.

    # getbbox tells us the size of the text before we draw it.
    bbox = font.getbbox(name)          # returns (left, top, right, bottom)
    text_width  = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (64 - text_width)  // 2       # centre horizontally
    y = (64 - text_height) // 2       # centre vertically

    # Step 5: Draw the text at position (x, y).
    draw.text((x, y), name, font=font, fill=fg)

    # Step 6: Save and send!
    image.save("name.gif")
    print("Name picture created!")

    print("Connecting to the frame...")
    conn = ConnectionManager()
    await conn.connectByAddress(FRAME_ADDRESS)
    print("Connected!")

    gif = Gif()
    await gif.uploadUnprocessed("name.gif")
    print(f"Done! '{name}' is on the frame! ✨")
    #   f"..."  is called an f-string.  Anything inside { } gets replaced
    #   with the actual value of the variable.  Pretty handy!


asyncio.run(show_name(my_name, background_colour, text_colour))
