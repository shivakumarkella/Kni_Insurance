from Pages_LOB.HoFullQuote.HoFullQuotePropertyPage import HoFullQuotePropertyPage
from Tests.testData import TestData as TD
from TestResults.customLogger import customLogger
import logging

class tests_HoFQPropertyPage():

    def __init__(self,driver):
        self.log = customLogger(logging.INFO)
        self.obj_HoFullQuotePropertyPage =HoFullQuotePropertyPage (driver)


    def tests_ValidDetailsOnPropertyPage(self):
        # self.log.info('Started Filling The Ho Full Quote by using :: Method fillDetailsForHoFullQuote ')
        self.obj_HoFullQuotePropertyPage.filldetailsforPropertypage(valueforOccupancy=TD.slectvalueforOccupancy,
                                                                    distancefromfoire=TD.distanceFromFire,
                                                                    primaryHeatingSource=TD.selectvalueforPrimaryheatingsource,
                                                                    fuelType=TD.selectvalueforFuelType)