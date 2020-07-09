import logging
import sys

def logs():
    logger = logging.getLogger(__name__)

    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")  # Message format.
    file_Handler = logging.FileHandler('logfile.log') #This is to create a log file in the folder.


    file_Handler.setFormatter(formatter)   #This is going to output the message in testLogs.log file.
    logger.addHandler(file_Handler)    #This will handle the logger file.

    logging.basicConfig(filename='logfile123.log',level=logging.info(),
                        format='%(asctime)s :%(levelname)s :%(name) :%(message)')

    #logger.setLevel(logging.info())
    logger.debug("A debug statement is executed.")
    logger.info("Information statement about the errors.")
    logger.warning("A warning has triggered.")
    logger.error("An error has occured.")
    logger.warning("A warning has triggered.")
    logger.critical("Any critical statement.")