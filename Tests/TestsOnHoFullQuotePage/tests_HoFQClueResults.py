from Pages_LOB.HoFullQuote.HoFullQuoteClueResultsPage import HoFullQuoteClueResultPage
from TestResults.customLogger import customLogger
import logging

class tests_HoFQClueresultsPage():

    def __init__(self,driver):
        self.log = customLogger(logging.INFO)
        self.obj_HoFullQuoteClueResult = HoFullQuoteClueResultPage(driver)


    def tests_clickClueContinuebutton(self):
        self.log.info('click successfull')
        self.obj_HoFullQuoteClueResult.tests_clickoncontinuebuttonforClueResults()