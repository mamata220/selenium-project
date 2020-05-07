import os
import shutil
from pathlib import Path
import pathlib
import mylogging

logger = mylogging.getmylogger()

'''foundFilesList = ["G:\\shiva\\Pics\\USA\\Texas\\My Temp folder\\100_0008.MP4",
                  "G:\\shiva\\Pics\\USA\\Texas\\My Temp folder\\100_0009.MP4",
                  "G:\\shiva\\Pics\\USA\\Texas\\My Temp folder\\100_0010.MP4"]
inputDirPath = "G:\\shiva\\Pics\\" #srcDirPathToSearchFile
initialDestFilePath = "G:\\VIDEOS\\CapturedVideos\\Temp\\"
'''


def moveAListOfFilesToNewLocation(srcDirPathToSearchFile, filesListToMove, initialDestFilePath):
    for srcFilePath in filesListToMove:
        msg = "srcFilePath=" + srcFilePath
        print(msg)
        logger.debug(msg)
        pathToFile = Path(srcFilePath)
        fileName = pathToFile.name
        srcFileDirectory = pathToFile.parent
        msg = "srcFileDirectory=" + str(srcFileDirectory)
        print(msg)
        logger.debug(msg)
        tempDestFileDirectory = str(srcFileDirectory)[len(srcDirPathToSearchFile):]
        finalDestFileDirectory = initialDestFilePath + tempDestFileDirectory
        finalDestPathOfFile = finalDestFileDirectory + "\\" + fileName
        msg = "finalDestFilePath : " + finalDestFileDirectory
        print(msg)
        logger.debug(msg)

        if not os.path.isdir(finalDestFileDirectory):
            msg = "Path '" + finalDestFileDirectory + "' does not exist, creating the path.."
            print(msg)
            logger.debug(msg)
            pathlib.Path(finalDestFileDirectory).mkdir(parents=True, exist_ok=True)
        else:
            msg = "Path '" + finalDestFileDirectory + "' exist."
            print(msg)
            logger.debug(msg)

        # os.rename(srcFilePath, finalDestPathOfFile)
        try:
            msg = "Trying to move the file: '" + finalDestPathOfFile + "' to the destination."
            print(msg)
            logger.debug(msg)
            shutil.move(srcFilePath, finalDestPathOfFile)
            msg = "File move was successful!"
            logger.debug(msg)
            print(msg)
        except OSError:
            msg = "Failed to move file: '" + finalDestPathOfFile + "'"
            logger.debug(msg)
            print(msg)
        print()
        logger.debug("\n")
