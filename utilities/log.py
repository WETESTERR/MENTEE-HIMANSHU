import logging
import sys
import os

import pytest
import config


class Logs():

    def logger(self):
        if not os.path.exists(config.logs_path):
            os.mkdir(config.logs_path)

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")  # Message format.

        file_Handler = logging.FileHandler(config.logs_path + '\\logfile.log',
                                           'w')  # This is to create a log file in the folder.

        file_Handler.setFormatter(formatter)  # This is going to output the message in testLogs.log file.
        logger.addHandler(file_Handler)  # This will handle the logger file.

        return logger
