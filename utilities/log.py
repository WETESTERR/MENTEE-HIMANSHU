import logging
import sys

def testLogs():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler("logfile.log") #This is to create a log file in the folder.

    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name) :%(message)")  #Message format.
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)   #This is going to output the message in testLogs.log file.
    logger.addHandler(handler)    #This will handle the logger file.

    #logger.setLevel(logging.info())
    logger.debug("A debug statement is executed.")
    logger.info("Information statement about the errors.")
    logger.warning("A warning has triggered.")
    logger.error("An error has occured.")
    logger.warning("A warning has triggered.")
    logger.critical("Any critical statement.")