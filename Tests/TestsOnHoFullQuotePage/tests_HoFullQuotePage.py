from Pages_LOB.HoFullQuotePage import HoFullQuotePage
from Tests.testData import TestData as TD
from TestResults.customLogger import customLogger


class tests_HoFullQuotePage():

    def __init__(self,driver):
        self.log = customLogger()
        self.obj_HoFullQuotePage = HoFullQuotePage(driver)


    def testCase1_ValidDetailsOnHoFQ(self):
        self.obj_HoFullQuotePage.fillDetailsForHoFullQuote(FirstName=TD.FirstName, LastName= TD.LastName,SSN= TD.SSN,Email=TD.Email,
                                                           DOB=TD.DOB,
                                                           propertyAddress1= TD.propertyAddress1, propertyAddress2= TD.propertyAddress2,
                                                           propertyCity= TD.propertyCity, propertyState= TD.propertyState,
                                                           propertyZip=TD.propertyZip,YearsAtCurrentAddress=TD.YearsAtCurrentAddress)




