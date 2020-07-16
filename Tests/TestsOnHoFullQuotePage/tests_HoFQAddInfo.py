from Pages_LOB.HoFullQuote.HoFullQuoteAddInfoPage import HoFullQuoteAdditionalInfo
from Tests.testData import TestData as TD
from TestResults.customLogger import customLogger



class tests_HoFQAddinfo():

    def __init__(self,driver):
        self.log = customLogger()
        self.obj_HoFullQuoteAddInfoPage = HoFullQuoteAdditionalInfo(driver)


    def tests_ValidDtailsOnAddinfo(self):
        self.obj_HoFullQuoteAddInfoPage.addedAdditinalInfo(YearsAtCurrentAddress=TD.YearsAtCurrentAddress)
