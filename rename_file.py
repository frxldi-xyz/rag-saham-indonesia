import os

def rename_pdfs_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            new_filename = filename
            # Remove "modified_" if it exists
            if new_filename.startswith("modified_"):
                new_filename = new_filename[len("modified_"):]
            # Convert to uppercase
            new_filename = new_filename.upper()
            # Rename the file
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {filename} to {new_filename}')

# Set the folder path
folder_path = 'dataset'

# Rename all PDFs in the folder
rename_pdfs_in_folder(folder_path)