"""
CP1404/CP5632 Practical 9
From Scratch - Sort files into directories per extension
"""


import os
import shutil


DIRECTORY = 'FilesToSort'


def main():
    os.chdir(DIRECTORY)

    directory_files = get_directory_filenames()

    extensions = get_extensions(directory_files)

    make_directories(extensions)

    move_files(extensions)


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


def make_directories(extensions):
    """Make directories from list"""
    for extension in extensions:
        if extension not in os.listdir('.'):
            os.mkdir(extension)


def move_files(extensions):
    """Move files to list according to extension"""
    for extension in extensions:
        for file in get_directory_filenames():
            for i, char in enumerate(file):
                if char == '.':
                    file_extension = file[i + 1: len(file)]
                    if extension == file_extension:
                        shutil.move(file, extension)

main()
