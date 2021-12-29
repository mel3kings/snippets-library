#!/usr/bin/python
import os

print("organize files....")

paths = ['/Users/melchor_tatlonghari/Desktop/', '/Users/melchor_tatlonghari/Downloads/']


def ensure_folder_exists(folders):
    print("checking folders exists {0}".format(folders))
    for folder in folders:
        if not os.path.isdir(folder):
            os.mkdir(folder)


def move_file(original_file_location, file_name, screenshots, ppt, pdf, others):
    print("trying to move " + file_name)
    to_directory = cleanup
    if original_file_location.endswith(".jpg") or original_file_location.endswith(
            ".png") or original_file_location.endswith(".jpeg"):
        to_directory = screenshots
    elif original_file_location.endswith(".ppt") or original_file_location.endswith(".pptx"):
        to_directory = ppt
    elif original_file_location.endswith(".pdf"):
        to_directory = pdf
    else:
        to_directory = others
    move_to = to_directory + file_name
    print("moving from" + original_file_location + " to " + move_to)
    os.rename(original_file_location, move_to)


for path in paths:
    try:
        os.chdir(path)
        cleanup = path + 'clean/'
        ppt_ = (cleanup + 'ppt/')
        others_ = (cleanup + 'others/')
        pdf_ = (cleanup + 'pdf/')
        screenshots_ = (cleanup + 'screenshots/')
        folders = [cleanup, ppt_, others_, pdf_, screenshots_]
        ensure_folder_exists(folders)
        print("Current working directory: {0}".format(os.getcwd()))
    except FileNotFoundError:
        print("Directory: {0} does not exist".format(path))
    except NotADirectoryError:
        print("{0} is not a directory".format(path))
    except PermissionError:
        print("You do not have permissions to change to {0}".format(path))
    arr = os.listdir(path)
    for a in arr:
        is_directory = os.path.isdir(a)
        if not is_directory:
            original_file = path + a
            move_file(original_file, a, screenshots_, ppt_, pdf_, others_)
print("done running command for {0}".format(os.getcwd()))
