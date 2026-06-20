import os
import time
import numpy as np
from pydub import AudioSegment
from modules.menu_helpers import CYAN, RESET

RAINBOW = [
    (255, 0, 0),
    (255, 127, 0),
    (255, 255, 0),
    (0, 255, 0),
    (0, 255, 255),
    (0, 0, 255),
    (139, 0, 255),
]

def rainbow_bar(level, width=50):
    blocks = int(level * width)
    out = ""
    for i in range(blocks):
        r, g, b = RAINBOW[i % len(RAINBOW)]
        out += f"\033[38;2;{r};{g};{b}m█{RESET}"
    return out

def _play_audio(path):
    os.system(
        f"ffplay -nodisp -autoexit -loglevel quiet '{path}' >/dev/null 2>&1 &"
    )

def visualize_audio(path):
    audio = AudioSegment.from_file(path)
    samples = np.array(audio.get_array_of_samples()).astype(float)
    chunk = 2048

    _play_audio(path)

    print(CYAN + "=== RAINBOW AUDIO VISUALIZER ===" + RESET)
    print("Press Ctrl+C to stop.\n")

    try:
        for i in range(0, len(samples), chunk):
            frame = samples[i:i+chunk]
            if len(frame) < chunk:
                break

            level = min(1.0, abs(frame).mean() / 20000)
            print(rainbow_bar(level))
            time.sleep(0.03)
    except KeyboardInterrupt:
        pass
