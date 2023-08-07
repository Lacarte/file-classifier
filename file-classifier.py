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
            mode="w",
        ),
        logging.StreamHandler(),
    ],
)


# Source directory
src_dir = os.path.expanduser("~/Desktop")


# Base target path
base_path = "d:/classifier"


# Mapping of file extensions to directories
ext_to_dir = {
    
    ".zip": base_path + "/compressed",
    ".rar": base_path + "/compressed",
    ".gz": base_path + "/compressed",
    ".tar": base_path + "/compressed",
    ".7z": base_path + "/compressed",
    ".bz2": base_path + "/compressed",
  
    ".jpg": base_path + "/images",
    ".jpeg": base_path + "/images",
    ".png": base_path + "/images",
    ".bmp": base_path + "/images",
    ".webp": base_path + "/images",
    ".jfif": base_path + "/images",
    ".webp": base_path + "/images",
    ".jpg-large": base_path + "/images",
    
    ".doc": base_path + "/documents",
    ".docx": base_path + "/documents",
    ".rtf": base_path + "/documents",
    ".xls": base_path + "/documents",
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
    
    ".mp3": src_dir + "/[audio]",
    ".wma": src_dir + "/[audio]",
    ".ogg": src_dir + "/[audio]",
    ".midi": src_dir + "/[audio]",
    ".mid": src_dir + "/[audio]",
    ".ogg": src_dir + "/[audio]",
    ".m4a": src_dir + "/[audio]",
  
   
    ".mp4": src_dir + "/[video]",
    ".avi": src_dir + "/[video]",
    ".mov": src_dir + "/[video]",
    ".mpg": src_dir + "/[video]",
    ".flv": src_dir + "/[video]",
    ".wmv": src_dir + "/[video]",
    ".webm": src_dir + "/[video]",
    ".f4v": src_dir + "/[video]",
    ".3gp": src_dir + "/[video]",
    ".mpeg": src_dir + "/[video]",



}

# Get the current date to append to filename
date_str = datetime.now().strftime("%Y-%m-%d")

# Iterate over all files in source directory
files_move = 0
for file_name in os.listdir(src_dir):
    file_path = os.path.join(src_dir, file_name)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Get the file extension
    ext = Path(file_path).suffix.lower()

    # Check if this extension is in our mapping
    if ext in ext_to_dir:
        dest_dir = ext_to_dir[ext]
        files_move += 1

        # Make sure the destination directory exists
        os.makedirs(dest_dir, exist_ok=True)

        # Append the date to the filename
        base_name = Path(file_name).stem
        new_file_name = f"{base_name}_{date_str}{ext}"
        dest_path = os.path.join(dest_dir, new_file_name)
        logging.info(f"Moving {file_path} to {dest_path}")
        # Move the file to the destination directory
        shutil.move(file_path, dest_path)

if (files_move > 0):
    logging.info(f"{files_move} file(s) moved successfully.")
else:
    logging.info("No files were found.")
