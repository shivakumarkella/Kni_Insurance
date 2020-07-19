from Pages_LOB.HoFullQuote.HoFullQuoteAddingInvoicePage import HoFullQuoteAddingInvoice
from Tests.testData import TestData as TD
from TestResults.customLogger import customLogger
import logging

class tests_HoFQBillingInfoPage():

    def __init__(self,driver):
        self.log = customLogger(logging.INFO)
        self.obj_HoFullQuoteAddingInvoicePage = HoFullQuoteAddingInvoice(driver)


    def tests_ValidDetailsOnBillingInfoPage(self):
        self.log.info('Started Filling The Ho Full Quote by using :: Method fillDetailsForHoFullQuote ')
        self.obj_HoFullQuoteAddingInvoicePage.filldetailsforAddingBill()


