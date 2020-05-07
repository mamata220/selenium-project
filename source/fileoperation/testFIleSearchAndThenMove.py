import searchFileInDirectory as search
import moveFileToAnotherDir as mvf
import mylogging

logger = mylogging.getmylogger()
srcDirPathToSearchFile = r"D:\Videos" #r"G:\VIDEOS\CapturedVideos"   # r'G:\shiva\Pics'
extension = ".mp4"
#extTuple = (".mpg", ".mp4", ".mpeg", ".mov", ".3gp", ".avi", ".wmv", ".flv")
#extTuple = [".jpg"]
filesListToMove = []
initialDestFilePath = r"D:\pics" #r"G:\shiva\Pics"  #G:\VIDEOS\CapturedVideos
filesListToMove = search.findFilesInFolder(srcDirPathToSearchFile, filesListToMove, extension, True)

if len(filesListToMove) > 0:
    print("Total files found : " + str(len(filesListToMove)))
    for f in filesListToMove:
        print(f)
else:
    msg = "File with specified extension could not be found in the directory and subdirectories"
    logger.debug(msg)
    print(msg)
logger.debug("Total files found : " + str(len(filesListToMove)))
print()
logger.debug("\n")
#mvf.moveAListOfFilesToNewLocation(srcDirPathToSearchFile, filesListToMove, initialDestFilePath)

