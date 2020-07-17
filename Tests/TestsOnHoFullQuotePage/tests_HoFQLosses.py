from Pages_LOB.HoFullQuote.HoFullQuoteLossspage import HoFullQuoteLosses
from Tests.testData import TestData as TD
from TestResults.customLogger import customLogger




class tests_HoFQLossesPage():

    def __init__(self,driver):
        self.log = customLogger()
        self.obj_HoFullQuoteLossspage = HoFullQuoteLosses(driver)

    def tests_ValidDtailsOnLosses(self):
        self.obj_HoFullQuoteLossspage.losses(selectvalueforFamily=TD.selectvalueforFamily,selectvalueforUsage=TD.selectvalueforUsage,
                                             selectvalueforConstruction=TD.selectvalueforConstruction)

