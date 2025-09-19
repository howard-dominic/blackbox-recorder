KBlackbox Recorder — Terminal Activity Tracker

Track your terminal file actions like a pro — create, move, delete, and replay them visually. Perfect for demos, auditing, and professional documentation.

🚀 Features

Record file actions: create, delete, move, rename

Replay recorded sessions exactly as they happened

Generate GIF proofs of terminal actions

View stats of recorded actions

Safe dummy file usage — real files stay untouched

Professional-ready documentation for recruiters and clients

🛠️ Requirements
python3 -m venv blackbox-venv
source blackbox-venv/bin/activate
pip install -r requirements.txt
pip install blackbox-recorder==1.0.0

🎯 Usage Guide
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

LATEST_SESSION=$(ls -t ../blackbox_logs | grep session | head -n1)
bb replay ../blackbox_logs/$LATEST_SESSION

3️⃣ Generate the GIF proof

bb visualize ../blackbox_logs/$LATEST_SESSION

📸 Proofs (Screenshots & GIF)

(Attach images here; filenames must match your assets folder.)

Step 1 — Initial Dummy File Creation
![Step 1](assets/screenshot1.png)

Step 2 — Delete & Move Operations
![Step 2](assets/screenshot2.png)

Step 3 — Stats Output
![Step 3](assets/screenshot3.png)

Step 4 — Replay Output
![Step 4](assets/screenshot4.png)

Step 5 — GIF Generation Success
![Step 5](assets/screenshot5.png)

Full Session Demo GIF
![Session Demo](assets/blackbox_demo.gif)

    🔎 Each GIF frame highlights one action — perfect for demonstrations.

⚠️ Recommended .gitignore

blackbox-venv/
__pycache__/
*.pyc
blackbox_logs/*.json
blackbox_logs/*.gif
# ⚠️ Do NOT ignore assets/

📄 License & Version

    License: MIT

    Version: 1.0.0
