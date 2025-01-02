from PIL import Image

BRAILLE_BASE = 0x2800


def image_to_braille(image_path, scale=0.5):
    """Render an image as Braille characters with True Color."""
    img = Image.open(image_path).convert("RGBA")

    # Resize the image based on the scale factor
    new_width = int(img.width * scale)
    new_height = int(img.height * scale)
    img = img.resize((new_width, new_height))

    # Ensure width is divisible by 2 and height is divisible by 4
    if new_width % 2 != 0:
        img = img.crop((0, 0, new_width - 1, new_height))
    if new_height % 4 != 0:
        img = img.crop((0, 0, new_width, new_height - (new_height % 4)))

    pixels = img.load()
    braille_lines = []
    for y in range(0, new_height, 4):
        line = []
        for x in range(0, new_width, 2):
            block_pixels = []
            for dy in range(4):
                for dx in range(2):
                    px = pixels[x + dx, y + dy]
                    block_pixels.append(px)
            braille_char = pixels_to_braille(block_pixels)
            r, g, b, _ = block_pixels[0]
            color = f"\033[38;2;{r};{g};{b}m"
            line.append(f"{color}{braille_char}\033[0m")
        braille_lines.append("".join(line))
    return "\n".join(braille_lines)


def pixels_to_braille(pixels):
    """Convert 2x4 pixel block to a Braille character."""
    braille_pattern = 0
    for i, (r, g, b, a) in enumerate(pixels):
        if a > 128:
            braille_pattern |= (1 << i)
    return chr(BRAILLE_BASE + braille_pattern)
