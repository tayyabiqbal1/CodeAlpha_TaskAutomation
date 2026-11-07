"""Task Automation: Move all .jpg files into a new folder.
Concepts: os, shutil, file handling.

Usage:
    python move_jpg_files.py                      (asks for the folder)
    python move_jpg_files.py "C:/Users/me/Downloads"
"""

import os
import shutil
import sys

DESTINATION_NAME = "JPG_Images"  # name of the new folder


def unique_path(folder, filename):
    """If a file with the same name already exists, add _1, _2, ... to it."""
    base, ext = os.path.splitext(filename)
    path = os.path.join(folder, filename)
    counter = 1
    while os.path.exists(path):
        path = os.path.join(folder, f"{base}_{counter}{ext}")
        counter += 1
    return path


def move_jpg_files(source_folder):
    # Check that the source folder exists
    if not os.path.isdir(source_folder):
        print(f"Error: '{source_folder}' is not a valid folder.")
        return

    # Create the destination folder if it doesn't exist
    destination = os.path.join(source_folder, DESTINATION_NAME)
    os.makedirs(destination, exist_ok=True)

    moved = 0
    for filename in os.listdir(source_folder):
        full_path = os.path.join(source_folder, filename)

        # Only look at files (skip folders) ending in .jpg (case-insensitive)
        if os.path.isfile(full_path) and filename.lower().endswith(".jpg"):
            target = unique_path(destination, filename)
            shutil.move(full_path, target)
            print(f"Moved: {filename}")
            moved += 1

    if moved == 0:
        print("No .jpg files found.")
    else:
        print(f"\nDone! Moved {moved} file(s) to '{destination}'")


def main():
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = input("Enter the folder path: ").strip().strip('"')
    move_jpg_files(folder)


if __name__ == "__main__":
    main()