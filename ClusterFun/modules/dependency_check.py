import importlib.util
from modules.menu_helpers import clear, CYAN, GREEN, YELLOW, RED, RESET
import shutil
import time

def _has_module(name):
    return importlib.util.find_spec(name) is not None

def run_dependency_check():
    missing = []
    if not _has_module("PIL"):
        missing.append("Pillow (python-pillow)")
    if not _has_module("pydub"):
        missing.append("pydub (pip install pydub)")
    if not _has_module("numpy"):
        missing.append("numpy (pip install numpy)")
    if shutil.which("ffplay") is None:
        missing.append("ffmpeg / ffplay (sudo pacman -S ffmpeg)")
    return missing

def dependency_check_mode():
    clear()
    print(CYAN + "=== DEPENDENCY CHECK ===" + RESET)
    missing = run_dependency_check()
    if not missing:
        print(GREEN + "All dependencies are installed!" + RESET)
    else:
        print(RED + "Missing dependencies:" + RESET)
        for m in missing:
            print(YELLOW + "- " + m + RESET)
    input("\nPress Enter to return...")
