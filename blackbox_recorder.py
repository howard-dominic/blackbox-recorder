#!/usr/bin/env python3
import os
import time
from pathlib import Path
from datetime import datetime
from PIL import ImageGrab  # for screenshots (requires pillow)
import imageio

# ==============================
# BlackBox Recorder — Humanly-written, pro & visually addictive
# ==============================

def snapshot(folder, tag="before"):
    """Take screenshot of folder"""
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = f"{folder}/bb_{tag}_{now}.png"
    img = ImageGrab.grab()
    img.save(fname)
    print(f"[+] Screenshot saved: {fname}")
    return fname

def replay(files, target_folder="replay_output"):
    """Replay recorded files/actions"""
    os.makedirs(target_folder, exist_ok=True)
    gif_frames = []
    for i, f in enumerate(files):
        dest = Path(target_folder) / Path(f).name
        if Path(f).is_file():
            os.system(f"cp '{f}' '{dest}'")
        print(f"Replaying {f} -> {dest}")
        time.sleep(0.3)
        # Optional: capture frame
        img = ImageGrab.grab()
        gif_frames.append(img)
    # Save GIF
    gif_path = Path(target_folder) / "replay.gif"
    gif_frames[0].save(gif_path, save_all=True, append_images=gif_frames[1:], duration=300, loop=0)
    print(f"[+] Replay GIF created: {gif_path}")

def main():
    folder = Path.home() / "demo_folder"
    folder.mkdir(exist_ok=True)
    files = [folder / f"file{i}.txt" for i in range(1,4)]
    # Create dummy files
    for f in files:
        f.write_text(f"Sample content for {f.name}")
        print(f"[+] Created {f}")
        time.sleep(0.3)
    # Take 'before' snapshot
    before = snapshot(str(folder), tag="before")
    # Example folder changes (organizing)
    organized = folder / "organized"
    organized.mkdir(exist_ok=True)
    for f in files:
        f.rename(organized / f.name)
    # Take 'after' snapshot
    after = snapshot(str(folder), tag="after")
    # Replay demo + GIF
    replay(list(organized.glob("*")))

if __name__ == "__main__":
    main()
