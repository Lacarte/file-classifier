# File Classifier Python Script

This Python script scans a source directory (e.g., the Desktop) for files, checks their file type, and then moves them to a corresponding target directory based on their type. It has built-in support for .jpg, .png, .bmp, .doc, and .docx file extensions, grouping them into 'images' and 'documents' categories respectively.

The script appends the current date to each file's name during the move to maintain a record of when the file was moved.

## Setup and Execution

1. **Python**: Ensure you have Python installed on your system. If not, download it from the official website (https://www.python.org/downloads/). This script was written using Python 3.7, but it should work with other 3.x versions.

2. **Administrator Privileges**: This script might require administrator privileges to run, depending on the locations of the source and destination directories.

3. **Script Configuration**: Open the Python script in a text editor. Adjust the `src_dir` variable to point to your source directory. This is set to the Desktop by default. The `base_path` variable is the base path where the files will be moved. This is set to "d:/classifier" by default. The `ext_to_dir` dictionary is where you can map other extensions to directories if needed.

```python
src_dir = os.path.expanduser("~/Desktop")  # Source directory
base_path = "d:/classifier"  # Base target path
ext_to_dir = {  # Mapping of file extensions to directories
    ".jpg": base_path + "/images",
    ".png": base_path + "/images",
    ".bmp": base_path + "/images",
    ".doc": base_path + "/documents",
    ".docx": base_path + "/documents",
}


4.  **Run the Script**: After making the necessary adjustments, save the script, open your command prompt or terminal, navigate to the directory where the script is located and run the following command: `python file_classifier.py`.

After running the script, it will move the files from the source directory to their corresponding directories as per the `ext_to_dir` mapping. If a directory does not exist, the script will create it. The script will append the current date to the moved files' names. The format is "original_filename_YYYY-MM-DD.extension".

## Note

The script only checks for .jpg, .png, .bmp, .doc, .docx file types by default. If you need to move other types of files, you can add them to the `ext_to_dir` dictionary. Simply add a new key-value pair where the key is the file extension (including the dot) and the value is the full path to the directory where these files should be moved.

Remember to back up your data before running this or any other file manipulation script. Always test the script on a small set of files to ensure it's working as expected before using it on important files.
