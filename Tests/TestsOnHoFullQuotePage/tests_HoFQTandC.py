from Pages_LOB.HoFullQuote.HoFullQuoteAcceptTAndCPage import HoFullQuoteAcceptTermsAndConditionPage
from Tests.testData import TestData as TD
from TestResults.customLogger import customLogger


class tests_HoFQTandC():

    def __init__(self,driver):
        self.log = customLogger()
        self.obj_HoFullQuoteAcceptTermsAndConditionPage = HoFullQuoteAcceptTermsAndConditionPage(driver)

    def tests_ValidDeatilsonTandC(self):
        self.obj_HoFullQuoteAcceptTermsAndConditionPage.acceptTermsAndCondition()


