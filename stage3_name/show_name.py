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
# THIS IS THE FUN PART -- change these things!
# -----------------------------------------------------------

first_name = "Nishtha"     # <-- your first name
last_name  = "???"         # <-- your last name

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

async def show_name(line1, line2, bg, fg):
    # Step 1: Create a picture filled with the background colour.
    image = Image.new("RGB", (64, 64), bg)

    # Step 2: Get a drawing pen.
    draw = ImageDraw.Draw(image)

    # Step 3: Load a font.
    # load_default() gives us a simple built-in font.
    # Each letter is 6 pixels wide and 8 pixels tall.
    font = ImageFont.load_default()

    # Step 4: Coordinates on the screen work like this:
    #
    #   (0,0) -----> x increases this way ---> (63, 0)
    #     |
    #     |  y increases downwards
    #     |
    #   (0,63)                                 (63,63)
    #
    # The frame is 64 pixels wide and 64 pixels tall.
    # Each letter is 6 pixels wide and 8 pixels tall.
    # There are two lines of text, so two separate (x, y) positions.

    # We have worked out x and y for the first line (top line).
    line1_width = len(line1) * 6
    x1 = (64 - line1_width) // 2    # centred horizontally
    y1 = 24                          # somewhere near the middle -- but is this right?

    # *** YOUR CHALLENGE ***
    # Work out x2 and y2 for the second line yourself!
    #
    # Hints:
    #   - x2 should centre the second word horizontally, just like x1.
    #     The formula is the same -- but use line2 instead of line1.
    #   - y2 should be BELOW y1.  Each line of text is 8 pixels tall,
    #     so how many pixels below y1 should y2 be?
    #
    # Replace the ??? below with your answers.

    line2_width = len(line2) * 6
    x2 = ???                          # <-- you figure this out!
    y2 = ???                          # <-- you figure this out!

    # Step 5: Draw both lines of text.
    draw.text((x1, y1), line1, font=font, fill=fg)
    draw.text((x2, y2), line2, font=font, fill=fg)

    # Step 6: Save and send!
    image.save("name.gif")
    print("Name picture created!")

    print("Connecting to the frame...")
    conn = ConnectionManager()
    await conn.connectByAddress(FRAME_ADDRESS)
    print("Connected!")

    gif = Gif()
    await gif.uploadUnprocessed("name.gif")
    print(f"Done! '{line1} {line2}' is on the frame! ✨")
    #   f"..."  is called an f-string.  Anything inside { } gets replaced
    #   with the actual value of the variable.  Pretty handy!


asyncio.run(show_name(first_name, last_name, background_colour, text_colour))
