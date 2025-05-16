# pip install Pillow

from PIL import Image

# === Step 1: Load your logo ===
img = Image.open("./ukubona-dark.png").convert("RGBA")
pixels = img.load()
width, height = img.size

# === Step 2: Detect background color ===
bg_color = pixels[0, 0]  # Sample top-left pixel (assumed background)

# === Step 3: Make background transparent ===
for y in range(height):
    for x in range(width):
        if pixels[x, y][:3] == bg_color[:3]:  # Ignore alpha when comparing
            pixels[x, y] = (0, 0, 0, 0)  # Fully transparent

# === Step 4: Save new PNG ===
img.save("./ukubona-dark-transparent.png")
