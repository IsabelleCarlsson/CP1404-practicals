"""
CP1404/CP5632 Practical 9
From Scratch v2 - Sort files into directories per extension specified by user
"""


import os
import shutil


DIRECTORY = 'FilesToSort'


def main():
    os.chdir(DIRECTORY)

    directory_files = get_directory_filenames()

    extensions = get_extensions(directory_files)

    if not directory_files:
        print("No files could be found!")
    else:
        user_folders = []
        folder_sorting = {}
        for extension in extensions:
            user_folder = input("What category would you like to sort {} files into? ".format(extension))
            if user_folder not in user_folders:
                user_folders.append(user_folder)
            folder_sorting[extension] = user_folder

        make_directories(user_folders)

        move_files(folder_sorting)

        print("\nSorting complete!")


def get_directory_filenames():
    """Get current files in directory"""
    filenames = []
    for filename in os.listdir('.'):
        if not os.path.isdir(filename):
            filenames.append(filename)
    return filenames


def get_extensions(files):
    """Get extensions from files in directory"""
    extensions = []
    for file in files:
        for i, char in enumerate(file):
            if char == '.':
                new_extension = file[i + 1: len(file)]
                if new_extension not in extensions:
                    extensions.append(new_extension)
    return extensions


def make_directories(folders):
    """Make directories from list"""
    for folder in folders:
        if folder not in os.listdir('.'):
            os.mkdir(folder)


def move_files(sorting_dictionary):
    """Moves files to folder according to dictionary"""
    for file in get_directory_filenames():
        for i, char in enumerate(file):
            if char == '.':
                file_extension = file[i + 1: len(file)]
                shutil.move(file, sorting_dictionary[file_extension])


main()
