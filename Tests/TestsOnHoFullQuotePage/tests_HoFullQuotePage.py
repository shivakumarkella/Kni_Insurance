from Pages_LOB.HoFullQuotePage import HoFullQuotePage
from Tests.testData import TestData as TD
from TestResults.customLogger import customLogger


class tests_HoFullQuotePage():

    def __init__(self,driver):
        self.log = customLogger()
        self.obj_HoFullQuotePage = HoFullQuotePage(driver)


    def testCase1_ValidDetailsOnHoFQ(self):
        self.obj_HoFullQuotePage.fillDetailsForHoFullQuote()
