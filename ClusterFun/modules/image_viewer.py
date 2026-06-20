import time
from PIL import Image
from modules.menu_helpers import clear, RESET, CYAN
from modules.file_browser import browse_for_file

def unicode_image_viewer():
    clear()
    print(CYAN + "=== UNICODE IMAGE VIEWER ===" + RESET)
    print("Select an image.\n")

    path = browse_for_file(".", exts=(".png", ".jpg", ".jpeg", ".bmp", ".gif", ".webp"))
    if not path:
        print("No image selected.")
        time.sleep(1)
        return

    try:
        img = Image.open(path).convert("RGB")
    except Exception as e:
        print(f"Failed to load image: {e}")
        time.sleep(2)
        return

    width = 80
    aspect = img.height / img.width
    height = int(width * aspect * 0.5)
    img = img.resize((width, height))

    for y in range(0, img.height - 1, 2):
        line = ""
        for x in range(img.width):
            top = img.getpixel((x, y))
            bottom = img.getpixel((x, y + 1))
            line += (
                f"\033[38;2;{top[0]};{top[1]};{top[2]}m"
                f"\033[48;2;{bottom[0]};{bottom[1]};{bottom[2]}m▀"
            )
        print(line + RESET)

    input("\nPress Enter to return...")
