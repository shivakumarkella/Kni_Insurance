from Pages_LOB.HoFullQuote.HoFullQuoteEndorsementPage import HoFullQuoteEndorsementPage
from TestResults.customLogger import customLogger
import logging

class tests_HoFQEndorsementPage():

    def __init__(self,driver):
        self.log = customLogger(logging.INFO)
        self.obj_HoFullQuoteEndorsement = HoFullQuoteEndorsementPage(driver)


    def tests_clickEndorsementContinuebutton(self):
        self.log.info('click successfull')
        self.obj_HoFullQuoteEndorsement.tests_clickoncontinuebuttonforEndorsement()

