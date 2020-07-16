from Pages_LOB.HoFullQuote.HoFullQuoteAcceptTAndCPage import HoFQTandCPage
from Tests.testData import TestData as TD
from TestResults.customLogger import customLogger


class tests_HoFQTandC():

    def __init__(self,driver):
        self.log = customLogger()
        self.ob=HoFQTandCPage(driver)
        # self.obj_HoFullQuoteAcceptTermsAndConditionPage = HoFQTandCPage(driver)

    def tests_ValidDeatilsonTandC(self):
        self.ob.acceptTermsAndCondition()


