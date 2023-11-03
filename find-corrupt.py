import os
import zipfile

source_folder = 'EU34_Reuploaded'  # Adjust your source folder path

# ANSI escape codes for colored text
RED = '\033[91m'
RESET = '\033[0m'

def scan_zip_files_for_corruption(source_folder):
    for zip_filename in os.listdir(source_folder):
        if zip_filename.endswith('.zip'):
            zip_filepath = os.path.join(source_folder, zip_filename)
            with zipfile.ZipFile(zip_filepath, 'r') as zipf:
                # Check if the zip file is empty
                if not zipf.namelist():
                    print(RED + f"The zip file '{zip_filename}' is empty." + RESET)
                # Check if the zip file is corrupt
                elif zipf.testzip() is not None:
                    print(RED + f"The zip file '{zip_filename}' is corrupt." + RESET)
                else:
                    print(f"The zip file '{zip_filename}' is valid.")

# Call the function to scan the zip files
scan_zip_files_for_corruption(source_folder)
