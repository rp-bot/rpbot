import shutil
from PIL import Image


def image_to_ascii(image_path, width=None):
    chars = "@%#*+=-:. "  # ASCII characters for brightness levels

    # Get terminal dimensions
    terminal_width, terminal_height = shutil.get_terminal_size()

    # Use the terminal width if `width` is not provided
    if width is None:
        width = terminal_width

    img = Image.open(image_path)

    # Resize image maintaining aspect ratio and considering terminal height
    aspect_ratio = img.height / img.width
    # Adjust for terminal's aspect ratio
    new_height = int(aspect_ratio * width * 0.55)

    # Scale down if the image height exceeds the terminal height
    if new_height > terminal_height - 3:  # Reserve space for controls
        scale_factor = (terminal_height - 3) / new_height
        width = int(width * scale_factor)
        new_height = int(new_height * scale_factor)

    img = img.resize((width, new_height))

    # Convert image to grayscale
    img = img.convert("L")

    # Map pixels to ASCII characters
    pixels = img.getdata()
    ascii_str = "".join(chars[pixel * len(chars) // 256] for pixel in pixels)

    # Split ASCII string into rows
    ascii_rows = [ascii_str[index:index + width]
                  for index in range(0, len(ascii_str), width)]
    return "\n".join(ascii_rows)
