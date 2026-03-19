# ============================================================
# Stage 4: Make the frame animate!
# ============================================================
# This is the most exciting stage yet!  Instead of one still
# picture, we are going to create lots of pictures and play
# them one after another -- just like a cartoon flip-book.
#
# New things you will learn in this stage:
#   - range()  (a handy way to count in a loop)
#   - Appending to a list  (building a list one item at a time)
#   - Saving a multi-frame (animated) GIF


import asyncio
from PIL import Image
from idotmatrix import ConnectionManager, Gif


# -----------------------------------------------------------
# THIS IS THE FUN PART -- try changing these!
# -----------------------------------------------------------

# The two colours that will take turns flashing.
colour_a = (255,   0, 255)   # pink / magenta
colour_b = (  0, 255, 255)   # cyan

# How many times to switch between the two colours.
# More blinks = longer animation before it loops.
number_of_blinks = 6

# How long each frame stays on screen, in milliseconds.
# 500 ms = half a second.  Try 200 (fast) or 1000 (slow).
frame_duration_ms = 500

# -----------------------------------------------------------
# Challenge: can you make it cycle through MORE than 2 colours?
# Hint: put all your colours in a list, then loop over them!
# -----------------------------------------------------------


FRAME_ADDRESS = "AF:32:CD:F6:81:30"


# -----------------------------------------------------------
# Everything below here makes the magic happen.
# -----------------------------------------------------------

async def show_animation(col_a, col_b, blinks, duration):
    # Step 1: Build a list of frames.
    # We start with an empty list and add one frame at a time.
    frames = []

    # range(blinks) counts from 0 up to (but not including) blinks.
    # So range(6) gives us: 0, 1, 2, 3, 4, 5
    for i in range(blinks):

        # i % 2 gives the remainder when dividing by 2.
        # Even numbers (0, 2, 4 ...) give remainder 0  -> colour A
        # Odd  numbers (1, 3, 5 ...) give remainder 1  -> colour B
        if i % 2 == 0:
            colour = col_a
        else:
            colour = col_b

        # Create a solid-colour frame and add it to our list.
        frame = Image.new("RGB", (64, 64), colour)
        frames.append(frame)   # append means "add to the end of the list"

    print(f"Created {len(frames)} frames.")

    # Step 2: Save all the frames as a single animated GIF.
    # save_all=True  tells Pillow to save every frame, not just the first.
    # append_images  is the list of extra frames after the first one.
    # loop=0         means "loop forever".
    # duration       is how long each frame lasts (in milliseconds).
    frames[0].save(
        "animation.gif",
        save_all=True,
        append_images=frames[1:],   # frames[1:] means "everything from index 1 onwards"
        loop=0,
        duration=duration,
        format="GIF",
    )
    print("Animated GIF saved!")

    # Step 3: Connect to the frame and send the animation.
    print("Connecting to the frame...")
    conn = ConnectionManager()
    await conn.connectByAddress(FRAME_ADDRESS)
    print("Connected!")

    gif = Gif()
    await gif.uploadUnprocessed("animation.gif")
    print("Done! Watch the frame flash! 💡")


asyncio.run(show_animation(colour_a, colour_b, number_of_blinks, frame_duration_ms))
