import os

IMAGE_EXT = (".png", ".jpg", ".jpeg", ".bmp", ".gif", ".webp")
AUDIO_EXT = (".mp3", ".wav", ".ogg", ".flac")

def browse_for_file(start=".", exts=None):
    cwd = os.path.abspath(start)
    exts = exts or ()

    while True:
        files = os.listdir(cwd)
        dirs = [f for f in files if os.path.isdir(os.path.join(cwd, f))]
        matches = [f for f in files
                   if os.path.isfile(os.path.join(cwd, f))
                   and (not exts or f.lower().endswith(exts))]

        print(f"\nDirectory: {cwd}\n")
        print("Folders:")
        for i, d in enumerate(dirs):
            print(f"  {i+1}. [DIR] {d}")

        print("\nFiles:")
        for i, f in enumerate(matches):
            print(f"  {i+1+len(dirs)}. {f}")

        print("\n0. Go up one folder")
        print("X. Cancel")

        choice = input("\nChoose: ").strip().lower()

        if choice == "x":
            return None
        if choice == "0":
            cwd = os.path.dirname(cwd)
            continue

        try:
            idx = int(choice) - 1
        except ValueError:
            continue

        if idx < len(dirs):
            cwd = os.path.join(cwd, dirs[idx])
        else:
            fidx = idx - len(dirs)
            if 0 <= fidx < len(matches):
                return os.path.join(cwd, matches[fidx])
