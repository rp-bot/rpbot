import shutil
from PIL import Image


def image_to_blocks(image_path, scale=None):
    """Render an image using block characters, dynamically scaling to fit terminal."""
    upper_block = "▀"  # Represents top half of the block
    lower_block = "▄"  # Represents bottom half of the block
    full_block = "█"   # Represents full block

    # Get terminal dimensions
    terminal_width, _ = shutil.get_terminal_size()

    img = Image.open(image_path)

    # Calculate dynamic scale to fit terminal width if scale is not provided
    if scale is None:
        scale = terminal_width / img.width

    # Calculate new dimensions
    new_width = int(img.width * scale)
    # Adjust for terminal's 2:1 aspect ratio
    new_height = int(img.height * scale * 2)
    img = img.resize((new_width, new_height))

    # Convert to grayscale for brightness levels
    img = img.convert("L")  # "L" mode converts to grayscale
    pixels = img.load()

    output = []
    for y in range(0, new_height, 2):  # Process two rows at a time
        line = []
        for x in range(new_width):
            # Get brightness of the top and bottom pixels
            top_pixel = pixels[x, y]
            bottom_pixel = pixels[x, y + 1] if y + 1 < new_height else 0

            # Choose block character based on brightness comparison
            if top_pixel > bottom_pixel:
                block = upper_block
            elif bottom_pixel > top_pixel:
                block = lower_block
            else:
                block = full_block

            line.append(block)
        output.append("".join(line))
    return "\n".join(output)
