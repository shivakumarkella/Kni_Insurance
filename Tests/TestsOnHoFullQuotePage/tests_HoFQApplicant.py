from Pages_LOB.HoFullQuote.HoFullQuoteApplicantPage import HoFullQuoteApplicantPage
from Tests.testData import TestData as TD
from TestResults.customLogger import customLogger


class tests_HoFQApplicantPage():

    def __init__(self,driver):
        self.log = customLogger()
        self.obj_HoFullQuoteApplicantPage = HoFullQuoteApplicantPage(driver)


    def tests_ValidDetailsOnApplicant(self):
        self.obj_HoFullQuoteApplicantPage.fillDetailsForHoFullQuote(FirstName=TD.FirstName, LastName= TD.LastName,SSN= TD.SSN,
                                                                    Email=TD.Email,
                                                           DOB=TD.DOB,
                                                           propertyAddress1= TD.propertyAddress1,
                                                           propertyAddress2= TD.propertyAddress2,
                                                           propertyCity= TD.propertyCity, propertyState= TD.propertyState,
                                                           propertyZip=TD.propertyZip,
                                                           selectvalue=TD.selectvalueforagency,
                                                           selectgender=TD.selectgender,
                                                           selctcounty=TD.selectCounty)












