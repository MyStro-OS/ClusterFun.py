import time
from modules.menu_helpers import clear, CYAN, RED, RESET
from modules.file_browser import browse_for_file
from modules.audio_visualizer import visualize_audio

def audio_file_selector():
    clear()
    print(CYAN + "Select an audio file (.mp3, .wav, .ogg)" + RESET)
    path = browse_for_file(".", exts=(".mp3", ".wav", ".ogg", ".flac"))

    if path:
        visualize_audio(path)
    else:
        print(RED + "No file selected." + RESET)
        time.sleep(1)
