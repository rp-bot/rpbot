from PIL import Image

BRAILLE_BASE = 0x2800


def image_to_braille(image_path, width=80):
    """Render an image as Braille characters, preserving aspect ratio."""
    img = Image.open(image_path).convert("L")  # Convert to grayscale

    # Calculate new dimensions maintaining aspect ratio
    aspect_ratio = img.height / img.width
    # Compensate for Braille grid compression
    adjusted_width = int(width * 0.5)
    # Adjust for Braille's 2:4 ratio
    new_height = int(aspect_ratio * adjusted_width * 4)
    img = img.resize((adjusted_width, new_height))

    # Ensure width is divisible by 2 and height is divisible by 4
    if adjusted_width % 2 != 0:
        img = img.crop((0, 0, adjusted_width - 1, new_height))
    if new_height % 4 != 0:
        img = img.crop((0, 0, adjusted_width, new_height - (new_height % 4)))

    pixels = img.load()
    braille_lines = []
    for y in range(0, new_height, 4):  # Process blocks of 4 rows
        line = []
        for x in range(0, adjusted_width, 2):  # Process blocks of 2 columns
            block_pixels = []
            for dy in range(4):
                for dx in range(2):
                    px = pixels[x + dx, y + dy]
                    block_pixels.append(px)
            braille_char = pixels_to_braille(block_pixels)
            line.append(braille_char)
        braille_lines.append("".join(line))
    return "\n".join(braille_lines)


def pixels_to_braille(pixels):
    """Convert a 2x4 pixel block to a Braille character."""
    braille_pattern = 0
    for i, pixel in enumerate(pixels):
        # Convert pixel intensity to binary pattern
        if pixel > 128:  # Threshold for determining pixel activation
            braille_pattern |= (1 << i)
    return chr(BRAILLE_BASE + braille_pattern)
