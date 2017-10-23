"""
CP1404/CP5632 Practical 9
Walkthrough Example - Renaming Files
"""

import os


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('Lyrics/')

    # creates a list of the subdirectory
    subdir_list = os.listdir('.')

    rename_files(subdir_list)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    filename_chars = list(filename)

    for i, char in enumerate(filename_chars):
        if i > 0 and char.isupper() and filename_chars[i - 1].isalpha():
            filename_chars.insert(i, "_")
        filename = "".join(filename_chars)

    filename = filename.title().replace(".Txt", ".txt")
    return filename


def rename_files(dir_list):
    """Renames files in subdirectories"""
    for dir in dir_list:
        os.chdir(str(dir))
        for filename in os.listdir('.'):
            if not os.path.isdir(filename):
                new_name = get_fixed_filename(filename)
                os.rename(filename, new_name)

        os.chdir('..')

main()
