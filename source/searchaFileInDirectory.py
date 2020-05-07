import os
from pathlib import Path


def findFilesInFolder(path, pathList, extension, subFolders=True):
    """  Recursive function to find all files of an extension type in a folder (and optionally in all subfolders too)

    path:        Base directory to find files
    pathList:    A list that stores all paths
    extension:   File extension to find
    subFolders:  Bool.  If True, find files in all subfolders under path. If False, only searches files in the specified folder
    """

    try:  # Trapping a OSError:  File permissions problem I believe
        for entry in os.scandir(path):
            if entry.is_file() and entry.path.endswith(extension):
                pathList.append(entry.path)
                p = Path(entry.path)
                print(p.parent)
            elif entry.is_dir() and subFolders:  # if its a directory, then repeat process as a nested function
                pathList = findFilesInFolder(entry.path, pathList, extension, subFolders)
    except OSError:
        print('Cannot access ' + path + '. Probably a permissions error')

    return pathList


dir_name = r'G:/shiva/Pics'
extension = ".MP4"
pathList = []
pathList = findFilesInFolder(dir_name, pathList, extension, True)
print("Total files found : "+str(len(pathList)))
print()
for file in pathList:
    print(file)
