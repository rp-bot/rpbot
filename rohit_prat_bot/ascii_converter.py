from PIL import Image


def image_to_ascii(image_path, width=80):
    chars = "@%#*+=-:. "  # ASCII characters for brightness levels
    img = Image.open(image_path)

    # Resize image maintaining aspect ratio
    aspect_ratio = img.height / img.width
    new_height = int(aspect_ratio * width * 0.55)
    img = img.resize((width, new_height))

    # Convert image to grayscale
    img = img.convert("L")

    # Map pixels to ASCII characters
    pixels = img.getdata()
    ascii_str = "".join(chars[pixel // 25] for pixel in pixels)

    # Split ASCII string into rows
    ascii_rows = [ascii_str[index:index + width]
                  for index in range(0, len(ascii_str), width)]
    return "\n".join(ascii_rows)
