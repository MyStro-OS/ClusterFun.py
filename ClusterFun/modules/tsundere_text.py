import time
from modules.menu_helpers import clear, MAGENTA, RESET

def tsundere_text():
    clear()
    lines = [
        "I-It’s not like I wanted to talk to you or anything…",
        "B-Baka…",
        "I just happened to be here, okay?",
        "Don’t get the wrong idea!",
        "Hmph…"
    ]

    print(MAGENTA + "=== TSUNDERE TEXT ===" + RESET)
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            for line in lines:
                clear()
                print(MAGENTA + line + RESET)
                time.sleep(1.5)
    except KeyboardInterrupt:
        clear()
        print(MAGENTA + "Hmph… whatever." + RESET)
        time.sleep(1)
