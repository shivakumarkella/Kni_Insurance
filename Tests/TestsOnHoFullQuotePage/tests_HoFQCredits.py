from Pages_LOB.HoFullQuote.HoFullQuoteCreditPage import HoFullQuoteCreditPage
from Tests.testData import TestData as TD
from TestResults.customLogger import customLogger


class tests_HoFQCredits():

    def __init__(self,driver):
        self.log = customLogger()
        self.obj_HoFullQuoteCreditPage = HoFullQuoteCreditPage(driver)

    def tests_ValidDeatilsonCredit(self):
        self.obj_HoFullQuoteCreditPage.creditscoredetails()
