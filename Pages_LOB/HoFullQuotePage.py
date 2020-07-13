from Pages_LOB.Locators import ApplicationLocators
from SeleniumActions import Actions



class HoFullQuotePage():

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

    # HOspinner_locator = list(Locator['SpinnerOverlay'].items())[0][1]
    # HOspinner_locatorType = list(Locator['SpinnerOverlay'].items())[0][0]





    def __init__(self,driver):
        self.driver = driver
        self.obj_SeleniumActions = Actions.SeleniumActions(self.driver)

    def quoteValidFor60Days(self):
        self.obj_SeleniumActions.waitForElementToClickOn(locator=self.Ho6oDaysPopUp_locator,
                                                         locatorType=self.Ho6oDaysPopUp_locatorType)

    def gotoHoFullQuotePage(self):
        self.obj_SeleniumActions.waitForElementToClickOn(locator=self.HOFullQuoteLink_locator,
                                                         locatorType=self.HOFullQuoteLink_locatorType)

    def selectAgency(self):
        self.obj_SeleniumActions.selectDropdown(locator=self.HOAgecny_locator,
                                                         locatorType=self.HOAgecny_locatorType)

    def selectRBforSecondInsuredPerson(self):
        self.obj_SeleniumActions.waitForElementToClickOn(locator=self.HONA_locator,
                                                         locatorType=self.HONA_locatorType)

    def selectGender(self):
        self.obj_SeleniumActions.waitForElementToClickOn(locator=self.HOGender_locator,
                                                locatorType=self.HOGender_locatorType)


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

    # def completeStingraySpinning(self):
    #     self.obj_SeleniumActions.waitForElementToDisappear(locator=self.HOspinner_locator,
    #                                                        locatorType=self.HOspinner_locatorType)











    def fillDetailsForHoFullQuote(self,FirstName="Test",LastName="Test",SSN="123321000",DOB="10/31/1990",Email="test@test.com",
                                  propertyAddress1="171 Test Road",propertyAddress2="Not Required",propertyCity="MOUNT VERNON",
                                  propertyState="KY",
                                  propertyZip="40456-7345"):
        self.gotoHoFullQuotePage()
        self.quoteValidFor60Days()
        self.selectAgency()
        self.selectGender()
        self.selectRBforSecondInsuredPerson()
        self.firstname(firstname=FirstName)
        self.lastname(lastname=LastName)
        self.ssn(ssn=SSN)
        self.dobofFirstInsuredPerson(dob=DOB)
        self.emailAddress(email=Email)
        self.selectMailingAddress()
        self.selectOccupidBy()
        self.propertyAddress1(propertyAddress1=propertyAddress1)
        self.propertyAddress2(propertyAddress2=propertyAddress2)
        self.propertyCity(propertyCity=propertyCity)
        self.propertyState(propertyState=propertyState)
        self.propertyZip(propertyZip=propertyZip)










