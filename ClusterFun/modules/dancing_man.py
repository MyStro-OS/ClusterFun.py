import time
from modules.menu_helpers import clear, MAGENTA, CYAN, RESET

def dancing_man():
    clear()
    frames = [
        MAGENTA + " \\o/ \n  |  \n / \\ " + RESET,
        MAGENTA + " _o_ \n  |  \n / \\ " + RESET,
        MAGENTA + " \\o  \n  |  \n / \\ " + RESET,
        MAGENTA + "  o/ \n  |  \n / \\ " + RESET,
    ]
    print(CYAN + "Dancing Man! Press Ctrl+C to stop." + RESET)
    try:
        while True:
            for f in frames:
                clear()
                print(f)
                time.sleep(0.2)
    except KeyboardInterrupt:
        pass
