import os
from pathlib import Path
import curses
from rohit_prat_bot.ascii_converter import image_to_ascii
from rohit_prat_bot.navigator import Navigator


def main(stdscr):
    # Initialize curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()

    # Load images
    package_dir = Path(__file__).parent
    image_dir = package_dir / "images"
    image_paths = [os.path.join(image_dir, f) for f in os.listdir(
        image_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]

    if not image_paths:
        stdscr.addstr(0, 0, "No images found in the 'images' directory.")
        stdscr.refresh()
        stdscr.getch()
        return

    navigator = Navigator(image_paths)

    while True:
        # Get the current image and render ASCII art
        current_image = navigator.current_image()
        ascii_art = image_to_ascii(current_image)

        # Clear and display the ASCII art
        stdscr.clear()
        for idx, line in enumerate(ascii_art.split("\n")):
            try:
                stdscr.addstr(idx, 0, line)
            except curses.error:
                pass  # Ignore lines that exceed the terminal height

        # Show controls
        stdscr.addstr(
            curses.LINES - 2, 0,
            "←: Previous | →: Next | q: Quit"
        )
        stdscr.refresh()

        # Wait for key press
        key = stdscr.getch()

        if key == curses.KEY_RIGHT:  # Right arrow
            navigator.next_image()
        elif key == curses.KEY_LEFT:  # Left arrow
            navigator.previous_image()
        elif key == ord('q'):  # Quit
            break


if __name__ == "__main__":
    curses.wrapper(main)
