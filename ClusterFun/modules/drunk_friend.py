import time
import random
from modules.menu_helpers import clear, YELLOW, RESET

def drunk_friend():
    clear()
    print(YELLOW + "=== DRUNK FRIEND TEXT ===" + RESET)
    print("Press Ctrl+C to stop.\n")

    phrases = [
        "Broooo… you’re my best friend…",
        "Listen… LISTEN… I love you man…",
        "Why is the room spinning?",
        "I swear I’m not drunk… you’re drunk.",
        "We should start a band.",
        "Do you think pigeons have feelings?"
    ]

    try:
        while True:
            clear()
            print(YELLOW + random.choice(phrases) + RESET)
            time.sleep(2)
    except KeyboardInterrupt:
        clear()
        print(YELLOW + "Bro… don’t leave me…" + RESET)
        time.sleep(1)
