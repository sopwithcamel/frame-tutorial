# ============================================================
# Stage 2: Paint the frame with colourful stripes!
# ============================================================
# Great work on Stage 1, Nishtha! Now we are going to draw
# stripes instead of one solid colour.
#
# New things you will learn in this stage:
#   - Lists  (a way to store lots of values together)
#   - for loops  (a way to do something many times)
#   - Drawing shapes with ImageDraw


import asyncio
from PIL import Image, ImageDraw           # ImageDraw lets us draw shapes
from idotmatrix import ConnectionManager, Gif


# -----------------------------------------------------------
# THIS IS THE FUN PART -- change the colours in this list!
# -----------------------------------------------------------
# This is a LIST.  Lists use square brackets [ ] and commas.
# Each item here is one stripe colour, from top to bottom.
# You can add more colours (more stripes!) or remove some.
# You can use any RGB colours from Stage 1.

stripe_colours = [
    (255,   0,   0),   # red
    (255, 165,   0),   # orange
    (255, 255,   0),   # yellow
    (  0, 255,   0),   # green
    (  0,   0, 255),   # blue
    (148,   0, 211),   # purple
]

# Try making it just two colours -- your two favourites!
# Or try 8 stripes, or even 64 (one pixel each)!


FRAME_ADDRESS = "AF:32:CD:F6:81:30"


# -----------------------------------------------------------
# Everything below here makes the magic happen.
# -----------------------------------------------------------

async def show_stripes(colours):
    # Step 1: Create a blank 64x64 picture.
    image = Image.new("RGB", (64, 64))

    # Step 2: Get a "pen" we can use to draw on the picture.
    draw = ImageDraw.Draw(image)

    # Step 3: Work out how tall each stripe should be.
    # We have 64 rows of pixels and we want to share them equally.
    stripe_height = 64 // len(colours)
    #   //  means "divide and throw away the remainder".
    #   So if we have 6 colours: 64 // 6 = 10 pixels each.

    # Step 4: Draw each stripe using a FOR LOOP.
    # A for loop repeats the indented code once for every item in the list.
    # Each time around, "i" is the position (0, 1, 2 ...) and
    # "colour" is the actual colour tuple for that stripe.
    for i, colour in enumerate(colours):
        top    = i * stripe_height          # where this stripe starts
        bottom = top + stripe_height - 1    # where this stripe ends

        # draw.rectangle draws a filled rectangle.
        # We give it the top-left corner and bottom-right corner.
        draw.rectangle([0, top, 63, bottom], fill=colour)

    # Step 5: Save the picture.
    image.save("stripes.gif")
    print("Stripe picture created!")

    # Step 6: Connect to the frame and send the picture.
    print("Connecting to the frame...")
    conn = ConnectionManager()
    await conn.connectByAddress(FRAME_ADDRESS)
    print("Connected!")

    gif = Gif()
    await gif.uploadUnprocessed("stripes.gif")
    print("Done! Your stripes are on the frame! 🌈")


asyncio.run(show_stripes(stripe_colours))
