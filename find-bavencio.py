import os
import zipfile
import re

source_folder = 'EU33_Reuploaded'  # Adjust your source folder path

# The target strings to search for in the zip files and file names
target_strings = ["Bavencio", "bavencio"]

# ANSI escape codes for colored text
RED = '\033[91m'
RESET = '\033[0m'

def scan_zip_files_for_strings(source_folder, target_strings):
    for zip_filename in os.listdir(source_folder):
        if zip_filename.endswith('.zip'):
            zip_filepath = os.path.join(source_folder, zip_filename)
            with zipfile.ZipFile(zip_filepath, 'r') as zipf:
                # Check if the zip file name contains any of the target strings
                for target_string in target_strings:
                    if re.search(target_string, zip_filename, re.IGNORECASE):
                        print(RED + f"The zip file name '{zip_filename}' contains the string '{target_string}'." + RESET)
                # Check if any of the file names within the zip contain any of the target strings
                for file_name in zipf.namelist():
                    for target_string in target_strings:
                        if re.search(target_string, file_name, re.IGNORECASE):
                            print(RED + f"The file name '{file_name}' within '{zip_filename}' contains the string '{target_string}'." + RESET)

# The target strings to search for in the zip files and file names
target_strings = ["Bavencio", "bavencio"]

scan_zip_files_for_strings(source_folder, target_strings)
print ("done")
