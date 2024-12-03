import os
import shutil

def move_screen(filename, folder_name):
    
    # Check if the file exists
    if not os.path.exists(filename):
        print(f"The file {filename} cannot be found.")
        return
    
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Construct the destination path
    destination = os.path.join(folder_name, filename)
    
    # Move the file
    try:
        shutil.move(filename, destination)
    except Exception as e:
        print(f"Error while moving the image: {e}")
