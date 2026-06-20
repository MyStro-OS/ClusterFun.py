import time
import random
from modules.menu_helpers import clear, GREEN, RESET

def hacker_background():
    clear()
    print(GREEN + "=== HACKER BACKGROUND ===" + RESET)
    print("Press Ctrl+C to stop.\n")

    chars = "#@(){}[]<>*$01"
    width = 80

    try:
        while True:
            line = "".join(random.choice(chars) for _ in range(width))
            print(GREEN + line + RESET)
            time.sleep(0.05)
    except KeyboardInterrupt:
        clear()
        print(GREEN + "Matrix stream ended." + RESET)
        time.sleep(1)
