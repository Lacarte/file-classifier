import os
import shutil
from datetime import datetime
from pathlib import Path
import logging

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
            mode="a",
        ),
        logging.StreamHandler(),
    ],
)

# Source directory
src_dir = os.path.expanduser("~/Desktop")

# Validate source directory exists
if not os.path.exists(src_dir):
    logging.error(f"Source directory {src_dir} does not exist")
    exit(1)

# Base target path
base_path = "d:/@Classifier"

# Mapping of file extensions to directories
ext_to_dir = {
    ".torrent": os.path.join(base_path, "torrent-file"),
    ".zip": os.path.join(base_path, "compressed"),
    ".rar": os.path.join(base_path, "compressed"),
    ".gz": os.path.join(base_path, "compressed"),
    ".tar": os.path.join(base_path, "compressed"),
    ".7z": os.path.join(base_path, "compressed"),
    ".bz2": os.path.join(base_path, "compressed"),
    ".jpg": os.path.join(base_path, "images"),
    ".jpeg": os.path.join(base_path, "images"),
    ".gif": os.path.join(base_path, "images"),
    ".png": os.path.join(base_path, "images"),
    ".bmp": os.path.join(base_path, "images"),
    ".webp": os.path.join(base_path, "images"),
    ".avif": os.path.join(base_path, "images"),
    ".jfif": os.path.join(base_path, "images"),
    ".jpg-large": os.path.join(base_path, "images"),
    ".doc": os.path.join(base_path, "documents"),
    ".docx": os.path.join(base_path, "documents"),
    ".rtf": os.path.join(base_path, "documents"),
    ".xls": os.path.join(base_path, "documents"),
    ".xlsx": os.path.join(base_path, "documents"),
    ".md": os.path.join(base_path, "documents"),
    ".txt": os.path.join(base_path, "documents"),
    ".xl": os.path.join(base_path, "documents"),
    ".ppt": os.path.join(base_path, "documents"),
    ".pps": os.path.join(base_path, "documents"),
    ".pptx": os.path.join(base_path, "documents"),
    ".pdf": os.path.join(base_path, "pdf"),
    ".html": os.path.join(base_path, "documents"),
    ".exe": os.path.join(base_path, "exe"),
    ".msi": os.path.join(base_path, "exe"),
    ".appxbundle": os.path.join(base_path, "exe"),
    ".bat": os.path.join(base_path, "exe"),
    ".apk": os.path.join(base_path, "apk"),
    ".mp3": os.path.join(base_path, "audio"),
    ".wma": os.path.join(base_path, "audio"),
    ".ogg": os.path.join(base_path, "audio"),
    ".midi": os.path.join(base_path, "audio"),
    ".mid": os.path.join(base_path, "audio"),
    ".m4a": os.path.join(base_path, "audio"),
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
        try:
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

            if os.path.exists(dest_path):
                logging.warning(f"File {new_file_name} already exists at {dest_path}, skipping")
                continue

            logging.info(f"Moving file {new_file_name} to {dest_path}")
            shutil.move(file_path, dest_path)
            files_moved += 1
        except Exception as e:
            logging.error(f"Error moving file {file_name}: {e}")

if files_moved:
    logging.info(f"{files_moved} file(s) moved successfully.")
else:
    logging.info("No files were moved.")

import time

for remaining in range(10, 0, -1):
    print(f"{remaining} seconds to exit...", end="\r")
    time.sleep(1)
