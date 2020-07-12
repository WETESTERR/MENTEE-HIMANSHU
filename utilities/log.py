import logging
import sys
import os

import pytest

class Logs():

    def logger(self):

        if not os.path.exists('C:\\Users\\Himanshu\\Python_Framework\\MENTEE-HIMANSHU\\logs'):
            os.mkdir('C:\\Users\\Himanshu\\Python_Framework\\MENTEE-HIMANSHU\\logs')

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)


        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")  # Message format.

        file_Handler = logging.FileHandler('C:\\Users\\Himanshu\\Python_Framework\\MENTEE-HIMANSHU\\logs\\logfile.log','w') #This is to create a log file in the folder.

        file_Handler.setFormatter(formatter)   #This is going to output the message in testLogs.log file.

        logger.addHandler(file_Handler)    #This will handle the logger file.

        logger.debug("A debug statement is executed.")
        logger.info("Information statement about the errors.")
        logger.warning("A warning has triggered.")
        logger.error("An error has occured.")
        logger.warning("A warning has triggered.")
        logger.critical("Any critical statement.")

        return logger



