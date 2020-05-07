import os

def findFilesInDirctory(directory, pathList, extension, subFolders=True):
    ext = (".mpg", ".mp4", ".mpeg",".mov")
    for folder, subfolders, filename in os.walk(directory):
        if any([filename.lower().endswith(tuple(ext)) for filename in filenames]):