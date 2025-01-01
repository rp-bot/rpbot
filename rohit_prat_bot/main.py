import os
from rohit_prat_bot.ascii_converter import image_to_ascii
from rohit_prat_bot.navigator import Navigator
from rich.console import Console


def main():
    console = Console()
    image_dir = "images"
    image_paths = [os.path.join(image_dir, f) for f in os.listdir(
        image_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]

    if not image_paths:
        console.print(
            "[bold red]No images found in the 'images' directory.[/bold red]")
        return

    navigator = Navigator(image_paths)

    while True:
        current_image = navigator.current_image()
        ascii_art = image_to_ascii(current_image)
        console.clear()
        console.print(ascii_art)

        console.print(
            "\n[bold]Controls:[/bold] [blue]n[/blue] - Next, [blue]b[/blue] - Back, [blue]q[/blue] - Quit")
        choice = console.input("[bold]Choose an option: [/bold]").lower()

        if choice == 'n':
            navigator.next_image()
        elif choice == 'b':
            navigator.previous_image()
        elif choice == 'q':
            break
        else:
            console.print("[bold red]Invalid choice![/bold red]")


if __name__ == "__main__":
    main()
