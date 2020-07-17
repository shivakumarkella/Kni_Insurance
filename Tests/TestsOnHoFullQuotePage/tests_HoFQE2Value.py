from Pages_LOB.HoFullQuote.HoFullQuoteE2ValuePage import HoFullQuoteE2ValuePage
from Tests.testData import TestData as TD
from TestResults.customLogger import customLogger
import logging

class tests_HoFQE2ValuePage():

    def __init__(self,driver):
        self.log = customLogger(logging.INFO)
        self.obj_HoFullQuoteE2ValuePage = HoFullQuoteE2ValuePage(driver)


    def tests_ValidDetailsOnE2ValuePage(self):
        self.log.info('Started Filling The Ho Full Quote by using :: Method fillDetailsForHoFullQuote ')
        self.obj_HoFullQuoteE2ValuePage.filldetailsforE2value(coverageAvalue=TD.coverageAvalue,
                                                              livingArea=TD.livingArea,
                                                              ConstructionYear=TD.ConstructionYear,
                                                              selectreplacementcost=TD.selectvalueforReplacementcosttype,
                                                              selectpropertyLocation=TD.selectvalueforPropertyLocation,
                                                              selectdwellingtype=TD.selectvalueforDwellingType,
                                                              selectconstructiontype=TD.selectConstructiontype,
                                                              selectconstructionquality=TD.selectconstructionquality,
                                                              selectgeneralCondition=TD.selectvalueforGeneralcondition,
                                                              selectroofcondition=TD.selectvalueforRoofcondition,
                                                              selectdwellingshape=TD.selectvalueforDwellingshape,
                                                              selectprimaryExterior=TD.selectvalueforPrimaryexterior,
                                                              selectprimaryroof=TD.selectvalueforRoofcovering,
                                                              selectwallcondition=TD.selectvalueforWallcondition,
                                                              selectfoundationcondition=TD.selectvalueforFoundationcondition)