from Pages_LOB.HoFullQuote.HoFullQuoteRatesPage import HoFullQuoteRatesPage
from TestResults.customLogger import customLogger
import logging

class tests_HoFQRatesPage():

    def __init__(self,driver):
        self.log = customLogger(logging.INFO)
        self.obj_HoFullQuoteRatesPage=HoFullQuoteRatesPage(driver)


    def tests_ValidDetailsOnRatesPage(self):
        # self.log.info('Started Filling The Ho Full Quote by using :: Method fillDetailsForHoFullQuote ')
        self.obj_HoFullQuoteRatesPage.filldetailsforRatespage()
