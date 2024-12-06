import os
import subprocess
import sys

"""
This script recursively searches through all child folders starting from the specified directory
and looks for image files with the following extensions: .jpeg, .jpg, .JPG, .png, .gif.
When an image file is found, it runs the bash command "magick mogrify -strip <filename>"
against that file to remove all metadata.

Metadata in public repositories can contain sensitive information such as the location where the photo was taken,
the device used to take the photo, and other personal details. Stripping metadata helps protect
privacy and reduces the file size.

Usage:
    python3 mogrify_looper.py <relative_path>

Arguments:
    <relative_path>  The relative path to the directory where the script should start searching for image files.
"""
# Check if the path is provided as an argument
if len(sys.argv) != 2:
    print("Usage: python3 mogrify_looper.py <relative_path>")
    sys.exit(1)

# Get the relative path from the command line arguments
relative_path = sys.argv[1]

# Define the image extensions to look for
image_extensions = ('.jpeg', '.jpg', '.JPG', '.png', '.gif')

# Loop through all child folders
for root, dirs, files in os.walk(relative_path):
    for file in files:
        if file.endswith(image_extensions):
            file_path = os.path.join(root, file)
            # Run the bash command
            command = f'magick mogrify -strip "{file_path}"'
            subprocess.run(command, shell=True)
            # Echo to terminal
            print(f'Command run: {command}')