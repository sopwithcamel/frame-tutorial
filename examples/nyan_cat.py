import asyncio
import urllib.request
from idotmatrix import ConnectionManager, Gif
from PIL import Image

GIF_URL = "https://media.giphy.com/media/sIIhZliB2McAo/giphy.gif"
GIF_PATH = "nyancat.gif"
GIF_RESIZED = "nyancat_64.gif"

def resize_gif(input_path, output_path, size=(64, 64)):
    gif = Image.open(input_path)
    frames = []
    durations = []
    try:
        while True:
            frame = gif.copy().convert("RGB")
            frame = frame.resize(size, Image.LANCZOS)
            frames.append(frame)
            durations.append(gif.info.get("duration", 100))
            gif.seek(gif.tell() + 1)
    except EOFError:
        pass

    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        loop=0,
        duration=durations,
        format="GIF"
    )
    print(f"Resized {len(frames)} frames to 64x64 -> {output_path}")

async def main():
    print("Downloading nyan cat GIF...")
    urllib.request.urlretrieve(GIF_URL, GIF_PATH)

    print("Resizing to 64x64...")
    resize_gif(GIF_PATH, GIF_RESIZED)

    print("Connecting to display...")
    conn = ConnectionManager()
    await conn.connectByAddress("AF:32:CD:F6:81:30")
    print("Connected!")

    gif = Gif()
    await gif.uploadUnprocessed(GIF_RESIZED)
    print("Nyan cat sent! 🌈🐱")

if __name__ == "__main__":
    asyncio.run(main())
