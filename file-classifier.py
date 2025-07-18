import os
import shutil
from datetime import datetime
from pathlib import Path
import logging
import time

# Create the "logs" directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(
            f"logs/log-{datetime.now().strftime('%Y-%m-%d')}.log",
            mode="w",
        ),
        logging.StreamHandler(),
    ],
)

# Source directory
src_dir = os.path.expanduser("~/Desktop")

# Base target path
base_path = "d:/@Classifier"

# Mapping of file extensions to directories
ext_to_dir = {
    ".torrent": base_path + "/torrent-file",
    ".zip": base_path + "/compressed",
    ".rar": base_path + "/compressed",
    ".gz": base_path + "/compressed",
    ".tar": base_path + "/compressed",
    ".7z": base_path + "/compressed",
    ".bz2": base_path + "/compressed",
    ".jpg": base_path + "/images",
    ".jpeg": base_path + "/images",
    ".gif": base_path + "/images",
    ".png": base_path + "/images",
    ".bmp": base_path + "/images",
    ".webp": base_path + "/images",
    ".avif": base_path + "/images",
    ".jfif": base_path + "/images",
    ".jpg-large": base_path + "/images",
    ".doc": base_path + "/documents",
    ".docx": base_path + "/documents",
    ".rtf": base_path + "/documents",
    ".xls": base_path + "/documents",
    ".xlsx": base_path + "/documents",
    ".md": base_path + "/documents",
    ".xl": base_path + "/documents",
    ".ppt": base_path + "/documents",
    ".ppts": base_path + "/documents",
    ".pps": base_path + "/documents",
    ".pptx": base_path + "/documents",
    ".pdf": base_path + "/pdf",
    ".exe": base_path + "/exe",
    ".msi": base_path + "/exe",
    ".AppxBundle": base_path + "/exe",
    ".bat": base_path + "/exe",
    ".apk": base_path + "/apk",
    ".mp3": base_path + "/audio",
    ".wma": base_path + "/audio",
    ".ogg": base_path + "/audio",
    ".midi": base_path + "/audio",
    ".mid": base_path + "/audio",
    ".m4a": base_path + "/audio",
    ".mp4": src_dir + "/@videos",
    ".avi": src_dir + "/@videos",
    ".mov": src_dir + "/@videos",
    ".mpg": src_dir + "/@videos",
    ".flv": src_dir + "/@videos",
    ".wmv": src_dir + "/@videos",
    ".webm": src_dir + "/@videos",
    ".f4v": src_dir + "/@videos",
    ".3gp": src_dir + "/@videos",
    ".mpeg": src_dir + "/@videos",
}

# Get current date to append to filename
date_str = datetime.now().strftime("%Y-%m-%d")

files_moved = 0

for file_name in os.listdir(src_dir):
    file_path = os.path.join(src_dir, file_name)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    ext = Path(file_path).suffix.lower()

    if ext in ext_to_dir:
        dest_dir = ext_to_dir[ext]
        os.makedirs(dest_dir, exist_ok=True)

        # Check available disk space on destination drive
        dest_drive = os.path.splitdrive(dest_dir)[0] or "/"
        free_space = shutil.disk_usage(dest_drive).free
        file_size = os.path.getsize(file_path)

        if free_space < file_size:
            logging.warning(f"Not enough space to move {file_name} to {dest_dir}")
            continue

        base_name = Path(file_name).stem
        new_file_name = f"{base_name}_{date_str}{ext}"
        dest_path = os.path.join(dest_dir, new_file_name)

        logging.info(f"Moving file {new_file_name} to {dest_path}")
        shutil.move(file_path, dest_path)
        files_moved += 1

if files_moved:
    logging.info(f"{files_moved} file(s) moved successfully.")
else:
    logging.info("No files were moved.")

# Simple countdown timer
for remaining in range(2, 0, -1):
    print(f"\033[92m{remaining} seconds\033[0m", end="\r")
    time.sleep(1)
