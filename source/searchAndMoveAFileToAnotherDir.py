import os
import shutil
from pathlib import Path
import pathlib


foundFilesList = ["G:\\shiva\\Pics\\USA\\Texas\\My Temp folder\\100_0008.MP4", "G:\\shiva\\Pics\\USA\\Texas\\My Temp folder\\100_0009.MP4", "G:\\shiva\\Pics\\USA\\Texas\\My Temp folder\\100_0010.MP4"]
inputDirPath = "G:\\shiva\\Pics\\"
initialDestFilePath = "G:\\VIDEOS\\CapturedVideos\\Temp\\"

for srcFilePath in foundFilesList:
    print("srcFilePath="+srcFilePath)
    pathToFile = Path(srcFilePath)
    fileName = pathToFile.name
    srcFileDirectory = pathToFile.parent
    print("srcFileDirectory="+str(srcFileDirectory))
    tempDestFileDirectory = str(srcFileDirectory)[len(inputDirPath):]
    finalDestFileDirectory = initialDestFilePath + tempDestFileDirectory
    finalDestPathOfFile = finalDestFileDirectory+"\\"+fileName
    print("finalDestFilePath : " + finalDestFileDirectory)

    if not os.path.isdir(finalDestFileDirectory):
        print("Path '"+finalDestFileDirectory+"' does not exist, creating the path..")
        pathlib.Path(finalDestFileDirectory).mkdir(parents=True, exist_ok=True)
    else:
        print("Path '" + finalDestFileDirectory + "' exist, moving the file to the destination..")

    #os.rename(srcFilePath, finalDestPathOfFile)
    try:
        shutil.move(srcFilePath, finalDestPathOfFile)
    except OSError:
        print("Failed to move file: '"+finalDestPathOfFile+"'")
    print()

# Move a file by renaming it's path
#os.rename('/Users/billy/d1/xfile.txt', '/Users/billy/d2/xfile.txt')

# Move a file from the directory d1 to d2
#shutil.move('/Users/billy/d1/xfile.txt', '/Users/billy/d2/xfile.txt')

"""" import os, shutil, pathlib, fnmatch

                
def move_dir(src: str, dst: str, pattern: str = '*'):
    if not os.path.isdir(dst):
        pathlib.Path(dst).mkdir(parents=True, exist_ok=True)
    for f in fnmatch.filter(os.listdir(src), pattern):
        shutil.move(os.path.join(src, f), os.path.join(dst, f))


move_dir(src="G:/shiva/Pics", dst="G:/VIDEOS/CapturedVideos/Temp", pattern="*.MP4") """