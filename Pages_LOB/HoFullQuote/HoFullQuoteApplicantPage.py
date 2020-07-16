from Pages_LOB.Locators import ApplicationLocators
from SeleniumActions import Actions



class HoFullQuoteApplicantPage():

    #Locators
    Locator = ApplicationLocators.HoFullQuote
    Ho6oDaysPopUp_locator=list(Locator['Days60PopUpButton'].items())[0][1]
    Ho6oDaysPopUp_locatorType= list(Locator['Days60PopUpButton'].items())[0][0]
    HOFullQuoteLink_locator = list(Locator['HOFullQuoteLink'].items())[0][1]
    HOFullQuoteLink_locatorType = list(Locator['HOFullQuoteLink'].items())[0][0]
    HOAgecny_locator = list(Locator['HOSelectAgency'].items())[0][1]
    HOAgecny_locatorType = list(Locator['HOSelectAgency'].items())[0][0]
    HOGender_locator = list(Locator['HOGender'].items())[0][1]
    HOGender_locatorType = list(Locator['HOGender'].items())[0][0]
    HONA_locator = list(Locator['HONA'].items())[0][1]
    HONA_locatorType = list(Locator['HONA'].items())[0][0]
    HOFirstName_locator = list(Locator['HOFirstName'].items())[0][1]
    HOFirstName_locatorType = list(Locator['HOFirstName'].items())[0][0]
    HOLastName_locator = list(Locator['HOLastName'].items())[0][1]
    HOLastName_locatorType = list(Locator['HOLastName'].items())[0][0]
    HOSSN_locator = list(Locator['HOSsn'].items())[0][1]
    HOSSN_locatorType = list(Locator['HOSsn'].items())[0][0]
    HODOB_locator = list(Locator['HODob'].items())[0][1]
    HODOB_locatorType = list(Locator['HODob'].items())[0][0]
    HOEmail_locator = list(Locator['HOEmail'].items())[0][1]
    HOEmail_locatorType = list(Locator['HOEmail'].items())[0][0]
    HOOccupiedBy_locator = list(Locator['HOOccupiedBy'].items())[0][1]
    HOOccupiedBy_locatorType = list(Locator['HOOccupiedBy'].items())[0][0]
    HOMailingAddress_locator = list(Locator['HOMailingAddress'].items())[0][1]
    HOMailingAddress_locatorType = list(Locator['HOMailingAddress'].items())[0][0]
    HOPropertyAddress_locator = list(Locator['HOPropertyAddress1'].items())[0][1]
    HOProprtyAddress_locatorType = list(Locator['HOPropertyAddress1'].items())[0][0]
    HOPropertyAddress2_locator = list(Locator['HOPropertyAddress2'].items())[0][1]
    HOPropertyAddress2_locatorType = list(Locator['HOPropertyAddress2'].items())[0][0]
    HOPropertyCity_locator = list(Locator['HOPropertyCity'].items())[0][1]
    HOPropertyCity_locatorType = list(Locator['HOPropertyCity'].items())[0][0]
    HOPropertyState_locator = list(Locator['HOState'].items())[0][1]
    HOPropertyState_locatorType = list(Locator['HOState'].items())[0][0]
    HOZip_locator = list(Locator['HOZip'].items())[0][1]
    HOZip_locatorType = list(Locator['HOZip'].items())[0][0]
    HOSuggestion_locator = list(Locator['HOSuggestionBox'].items())[0][1]
    HOSuggestion_locatorType = list(Locator['HOSuggestionBox'].items())[0][0]
    HOEmptybox_locator = list(Locator['HOEmptyBox'].items())[0][1]
    HOEmptybox_locatorType =list(Locator['HOEmptyBox'].items())[0][0]
    HOApplicantContinue_locator = list(Locator['HOApplicantContinue'].items())[0][1]
    HOApplicantContinue_locatorType =list(Locator['HOApplicantContinue'].items())[0][0]
    HOAddressspinner_locator = list(Locator['HOAddressSpinnerOverlay'].items())[0][1]
    HOAddressspinner_locatorType = list(Locator['HOAddressSpinnerOverlay'].items())[0][0]
    MMInsuredManagement_locator = list(Locator['MMInsuredManagement'].items())[0][1]
    MMInsuredManagement_locatorType = list(Locator['MMInsuredManagement'].items())[0][0]
    HOCounty_locator = list(Locator['HOCounty'].items())[0][1]
    HOCounty_locatorType = list(Locator['HOCounty'].items())[0][0]




    def __init__(self,driver):
        self.driver = driver
        self.obj_SeleniumActions = Actions.SeleniumActions(self.driver)

    def quoteValidFor60Days(self):
        self.obj_SeleniumActions.waitForElementToClickOn(locator=self.Ho6oDaysPopUp_locator,
                                                         locatorType=self.Ho6oDaysPopUp_locatorType)

    def gotoHoFullQuotePage(self):
        self.obj_SeleniumActions.waitForElementToClickOn(locator=self.HOFullQuoteLink_locator,
                                                         locatorType=self.HOFullQuoteLink_locatorType)


    def selectAgency(self,selectvalue):
        self.obj_SeleniumActions.selectDropdown(locator=self.HOAgecny_locator,
                                                         locatorType=self.HOAgecny_locatorType,SelectValue=selectvalue)

    def selectRBforSecondInsuredPerson(self):
        self.obj_SeleniumActions.waitForElementToClickOn(locator=self.HONA_locator,
                                                         locatorType=self.HONA_locatorType)

    def selectGender(self,selectvalue):
        self.obj_SeleniumActions.selectDropdown(locator=self.HOGender_locator,
                                                locatorType=self.HOGender_locatorType,SelectValue=selectvalue)


    def firstname(self,firstname):
        self.obj_SeleniumActions.sendKeys(locator=self.HOFirstName_locator,
                                          locatortype=self.HOFirstName_locatorType, message=firstname)

    def lastname(self,lastname):
        self.obj_SeleniumActions.sendKeys(locator=self.HOLastName_locator,
                                          locatortype=self.HOLastName_locatorType,message=lastname)
    def ssn(self,ssn):
        self.obj_SeleniumActions.sendKeys(locator=self.HOSSN_locator,
                                          locatortype=self.HOSSN_locatorType,message=ssn)

    def dobofFirstInsuredPerson(self,dob):
        self.obj_SeleniumActions.sendKeys(locator=self.HODOB_locator,
                                          locatortype=self.HODOB_locatorType,message=dob)

    def emailAddress(self,email):
        self.obj_SeleniumActions.sendKeys(locator=self.HOEmail_locator,
                                          locatortype=self.HOEmail_locatorType,message=email)

    def selectOccupidBy(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HOOccupiedBy_locator,
                                                   locatorType=self.HOOccupiedBy_locatorType)

    def selectMailingAddress(self):
        self.obj_SeleniumActions.selectCheckbox(locator=self.HOMailingAddress_locator,
                                                         locatorType=self.HOMailingAddress_locatorType)


    def propertyAddress1(self,propertyAddress1):
        self.obj_SeleniumActions.sendKeys(locator=self.HOPropertyAddress_locator,
                                          locatortype=self.HOProprtyAddress_locatorType,message=propertyAddress1)

    def propertyAddress2(self,propertyAddress2):
        self.obj_SeleniumActions.sendKeys(locator=self.HOPropertyAddress2_locator,
                                          locatortype=self.HOPropertyAddress2_locatorType,message=propertyAddress2)

    def propertyCity(self, propertyCity):
        self.obj_SeleniumActions.sendKeys(locator=self.HOPropertyCity_locator,
                                          locatortype=self.HOPropertyCity_locatorType, message=propertyCity)

    def propertyState(self, propertyState):
        self.obj_SeleniumActions.sendKeys(locator=self.HOPropertyState_locator,
                                          locatortype=self.HOPropertyState_locatorType, message=propertyState)

    def propertyZip(self, propertyZip):
        self.obj_SeleniumActions.sendKeys(locator=self.HOZip_locator,
                                          locatortype=self.HOZip_locatorType, message=propertyZip)

    def suggestionBox(self):
        self.obj_SeleniumActions.waitForElementToClickOn(locator=self.HOSuggestion_locator,
                                                         locatorType=self.HOSuggestion_locatorType)

    def emptyBox(self):
        self.obj_SeleniumActions.waitForElementToClickOn(locator=self.HOEmptybox_locator,
                                                         locatorType=self.HOEmptybox_locatorType)

    def completeStingraySpinning(self):
        self.obj_SeleniumActions.waitForElementToDisappear(locator=self.HOAddressspinner_locator,
                                                            locatorType=self.HOAddressspinner_locatorType)

    def clickonApplicantContinuebutton(self):
        self.obj_SeleniumActions.waitForElementToClickOn(locator=self.HOApplicantContinue_locator,
                                                         locatorType=self.HOApplicantContinue_locatorType)



    def selectCountybyValue(self,selectvalue):
        self.obj_SeleniumActions.selectDropdown(locatorType=self.HOCounty_locatorType,locator=self.HOCounty_locator,
                                                SelectValue=selectvalue)


    def countySelectedValue(self):
        selectedValue=self.obj_SeleniumActions.getTheDropDownSelectedValue(locatorType=self.HOCounty_locatorType,locator=self.HOCounty_locator)
        return selectedValue






    def fillDetailsForHoFullQuote(self,FirstName,LastName,SSN,DOB,Email,propertyAddress1,propertyAddress2,propertyCity,
                                  propertyState,propertyZip,selectvalue,selectgender,selctcounty):

        self.obj_SeleniumActions.LoadtheDomCompletely()
        self.completeStingraySpinning()
        self.completeStingraySpinning()

        self.gotoHoFullQuotePage()
        self.quoteValidFor60Days()
        self.obj_SeleniumActions.LoadtheDomCompletely()
        self.firstname(FirstName)
        self.lastname(LastName)
        self.ssn(SSN)
        self.dobofFirstInsuredPerson(DOB)
        self.completeStingraySpinning()
        self.selectAgency(selectvalue)
        self.completeStingraySpinning()
        self.selectGender(selectgender)
        self.selectRBforSecondInsuredPerson()
        self.emailAddress(Email)
        self.selectMailingAddress()
        self.selectOccupidBy()
        self.propertyAddress1(propertyAddress1)
        self.propertyAddress2(propertyAddress2)
        self.propertyCity(propertyCity)
        self.propertyState(propertyState)
        self.propertyZip(propertyZip)
        self.suggestionBox()
        self.completeStingraySpinning()
        self.obj_SeleniumActions.sleepForWhile(sleepTime=3)
        countySelectedValue=self.countySelectedValue()
        if countySelectedValue=='-1':
            self.selectCountybyValue(selectvalue=selctcounty)
        else:
            self.emptyBox()
        self.completeStingraySpinning()
        self.clickonApplicantContinuebutton()
