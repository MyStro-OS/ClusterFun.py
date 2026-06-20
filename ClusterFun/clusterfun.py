import time
from modules.menu_helpers import clear, CYAN, YELLOW, RED, RESET
from modules.image_viewer import unicode_image_viewer
from modules.audio_selector import audio_file_selector
from modules.dancing_man import dancing_man
from modules.idle_game import idle_game
from modules.tsundere_text import tsundere_text
from modules.drunk_friend import drunk_friend
from modules.hacker_bg import hacker_background
from modules.dependency_check import dependency_check_mode

def main_menu():
    while True:
        clear()
        print(CYAN + "=== ClusterFun ===" + RESET)
        print(YELLOW + "1. Idle Game" + RESET)
        print(YELLOW + "2. Dancing Man" + RESET)
        print(YELLOW + "3. Drunk Friend" + RESET)
        print(YELLOW + "4. Tsundere Text" + RESET)
        print(YELLOW + "5. Hacker Background" + RESET)
        print(YELLOW + "6. Unicode Image Viewer" + RESET)
        print(YELLOW + "7. Rainbow Audio Visualizer" + RESET)
        print(RED + "8. Exit" + RESET)

        choice = input("\nChoose: ").strip()

        if choice == "1":
            idle_game()
        elif choice == "2":
            dancing_man()
        elif choice == "3":
            drunk_friend()
        elif choice == "4":
            tsundere_text()
        elif choice == "5":
            hacker_background()
        elif choice == "6":
            unicode_image_viewer()
        elif choice == "7":
            audio_file_selector()
        elif choice == "CHECK":
            dependency_check_mode()
        elif choice == "8":
            clear()
            print(RED + "Exiting ClusterFun..." + RESET)
            time.sleep(0.5)
            clear()
            break
        else:
            print(RED + "Invalid choice." + RESET)
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
