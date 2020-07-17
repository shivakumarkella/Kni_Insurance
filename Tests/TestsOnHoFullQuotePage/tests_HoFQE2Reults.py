from Pages_LOB.HoFullQuote.HoFullQuoteE2ResultsPage import HoFullQuoteE2ValueResultPage
from TestResults.customLogger import customLogger
import logging

class tests_HoFQE2ResultsPage():

    def __init__(self,driver):
        self.log = customLogger(logging.INFO)
        self.obj_HoFullQuoteE2Result = HoFullQuoteE2ValueResultPage(driver)


    def clickE2ResultContinuebutton(self):
        self.log.info('click successfull')
        self.obj_HoFullQuoteE2Result.tests_clickoncontinuebuttonforE2Results()