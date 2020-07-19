import inspect
import logging
from datetime import datetime
from pytz import timezone
from tzlocal import get_localzone
from Tests.testData import TestData as TD


def customLogger(logLevel=logging.DEBUG):
    # Gets the name of the class / method from where this method is called
    format = "%Y_%m_%d_%H_%M_%S"
    timeStamp = (datetime.now(timezone(str(get_localzone()).upper()))).strftime(format)
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    AutomationFileName =TD.AutomationFileName + str(timeStamp)+'.log'
    pathToSaveAutomationLog = TD.pathToSaveAutomationLog+AutomationFileName
    fileHandler = logging.FileHandler(pathToSaveAutomationLog, mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
