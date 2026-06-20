import time
from modules.menu_helpers import clear, CYAN, YELLOW, GREEN, RESET

def idle_game():
    clear()
    print(CYAN + "=== IDLE GAME ===" + RESET)
    print("Press Ctrl+C to stop.\n")

    cookies = 0
    cps = 1  # cookies per second

    try:
        while True:
            clear()
            print(YELLOW + "Cookies: " + RESET + str(cookies))
            print(GREEN + "CPS: " + RESET + str(cps))
            cookies += cps
            time.sleep(1)
    except KeyboardInterrupt:
        clear()
        print(GREEN + "Idle game stopped." + RESET)
        time.sleep(1)
