from Pages_LOB.HoFullQuote.HoFullQuoteCoveragesPage import HoFullQuoteCoveragesPage
from Tests.testData import TestData as TD
from TestResults.customLogger import customLogger
import logging

class tests_HoFQCoveragePage():

    def __init__(self,driver):
        self.log = customLogger(logging.INFO)
        self.obj_HoFullQuoteCoveragesPage =HoFullQuoteCoveragesPage (driver)


    def tests_ValidDetailsOnCoveragesPage(self):
        self.log.info('Started Filling The Ho Full Quote by using :: Method fillDetailsForHoFullQuote ')
        self.obj_HoFullQuoteCoveragesPage.filldetailsforCoverages(coverageEvalue=TD.selctvalueforCoverageE,
                                                                  coverageFvalue=TD.selectvalueforCoverageF,
                                                                  policydeductble=TD.selctvalueforPolicyDeductible)