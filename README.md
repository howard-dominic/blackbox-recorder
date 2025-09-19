# Blackbox Recorder — Terminal Activity Tracker

**Description**  
Blackbox Recorder logs file operations and generates visual proofs. Ideal for auditing, demos, and professional documentation.

---

## Features

- Record file actions: `create`, `delete`, `move`, `rename`.
- Replay recorded sessions exactly as they happened.
- Generate GIF proofs of terminal actions.
- View stats of recorded actions for auditing.
- Safe dummy file usage — real files remain untouched.
- Professional-ready documentation for recruiters and clients.

---

## Requirements

```bash
python3 -m venv blackbox-venv
source blackbox-venv/bin/activate
pip install -r requirements.txt
pip install blackbox-recorder==1.0.0

Usage Guide
1️⃣ Record a dummy session

cd ~/blackbox-dummy
bb record create dummy_files/file1.txt
bb record create dummy_files/file2.txt
bb record create dummy_files/file3.txt
bb record create dummy_files/file4.txt
bb record delete dummy_files/file2.txt
bb record move dummy_files/file3.txt dummy_files/folder1/
bb record move dummy_files/file4.txt dummy_files/folder2/
bb record move dummy_files/file1.txt dummy_files/file1_renamed.txt

2️⃣ Replay the latest session

LATEST_SESSION=$(ls -t blackbox_logs | grep session | head -n1)
bb replay blackbox_logs/$LATEST_SESSION

3️⃣ Generate the GIF proof

bb visualize blackbox_logs/$LATEST_SESSION

The GIF is saved in the repo under assets/.

## 📸 Proofs (Screenshots & GIF)

### Step 1 — Initial dummy file creation
![Step 1](assets/screenshot1.png)

### Step 2 — Delete & move operations
![Step 2](assets/screenshot2.png)

### Step 3 — Stats output
![Step 3](assets/screenshot3.png)

### Step 4 — Replay output
![Step 4](assets/screenshot4.png)

### Step 5 — GIF generation success
![Step 5](assets/screenshot5.png)

---

### 🎞️ GIF Proof — Full Session Demo
![Session Demo](assets/blackbox_demo.gif)

    🔎 GIF shows one frame per action to highlight each step clearly.

Recommended .gitignore

blackbox-venv/
__pycache__/
*.pyc
blackbox_logs/*.json
blackbox_logs/*.gif

⚠️ Do not ignore assets/ — otherwise screenshots/GIF won’t show up in GitHub README.
License & Version

    License: MIT

    Version: 1.0.0

Notes

    Keep README clean, professional, recruiter-friendly.

    Dummy files ensure safety of your real data.

    Screenshots + GIF = the visual proof that makes this repo stand out.
