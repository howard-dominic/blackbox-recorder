# Blackbox Recorder — Terminal Activity Tracker

**Description:**  
Blackbox Recorder logs file operations and generates visual proofs. Ideal for auditing, demos, and professional documentation.

---

## Features

- Record file actions: `create`, `delete`, `move`, `rename`.
- Replay recorded sessions exactly as they happened.
- Generate GIF proofs of terminal actions.
- Stats of recorded actions for auditing.
- Safe dummy file usage — your real files are untouched.
- Professional-ready documentation.

---

## Requirements

```bash
python3 -m venv blackbox-venv
source blackbox-venv/bin/activate
pip install -r requirements.txt
pip install blackbox-recorder==1.0.0

Usage Guide
1️⃣ Record Dummy Session

cd ~/blackbox-dummy

bb record create dummy_files/file1.txt
bb record create dummy_files/file2.txt
bb record create dummy_files/file3.txt
bb record create dummy_files/file4.txt
bb record delete dummy_files/file2.txt
bb record move dummy_files/file3.txt dummy_files/folder1/
bb record move dummy_files/file4.txt dummy_files/folder2/
bb record move dummy_files/file1.txt dummy_files/file1_renamed.txt

2️⃣ Replay Session

LATEST_SESSION=$(ls -t blackbox_logs | grep session | head -n1)
bb replay blackbox_logs/$LATEST_SESSION

3️⃣ Generate GIF Proof

bb visualize blackbox_logs/$LATEST_SESSION

GIF saved at:
~/blackbox-dummy/blackbox_logs/session_XXXX.gif
Proofs (Screenshots & GIF)

Screenshots:

    Initial dummy file creation:
    assets/screenshot1.png

    Delete & move operations:
    assets/screenshot2.png

    Stats output:
    assets/screenshot3.png

    Replay output:
    assets/screenshot4.png

    GIF generation success:
    assets/screenshot5.png

GIF Proof (from terminal or screenshots):

assets/session_demo.gif

    Note: GIF shows a frame per action to highlight each step clearly.

Recommended Git Ignore

blackbox-venv/
__pycache__/
*.pyc
blackbox_logs/*.json
blackbox_logs/*.gif
assets/*.png

Notes

    Keep README clean, professional, minimal emojis.

    Dummy files ensure safety of your real data.

    Screenshots + GIF showcase repo power and workflow.

    Version: 1.0.0
