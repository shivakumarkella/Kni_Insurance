from Pages_LOB.Locators import ApplicationLocators
from SeleniumActions import Actions



class HoFullQuoteAdditionalInfo():
    Locator = ApplicationLocators.HoFullQuoteAddinformation
    HOAddinfoSpinner_locator = list(Locator["SpinnerOverlay"].items())[0][1]
    HOAddinfoSpinner_locatorType = list(Locator["SpinnerOverlay"].items())[0][0]
    HOYearsAtCurrentAddress_locator = list(Locator["HOYearsAtCurrentAddress"].items())[0][1]
    HOYearsAtCurrentAddress_locatorType = list(Locator["HOYearsAtCurrentAddress"].items())[0][0]
    HOFirstTimeBuyer_locator = list(Locator["HOFirstTimeHomeBuyer"].items())[0][1]
    HOFirstTimeBuyer_locatorType = list(Locator["HOFirstTimeHomeBuyer"].items())[0][0]
    HOAddinfoContinue_locator = list(Locator["HOAddinfoContinueButton"].items())[0][1]
    HOAddinfoContinue_locatorType = list(Locator["HOAddinfoContinueButton"].items())[0][0]

    def __init__(self,driver):
        self.driver = driver
        self.obj_SeleniumActions = Actions.SeleniumActions(self.driver)




    def yearsatcurrentaddress(self, years):
        self.obj_SeleniumActions.sendKeys(locator=self.HOYearsAtCurrentAddress_locator,
                                          locatortype=self.HOYearsAtCurrentAddress_locatorType, message=years)

    def selectRBforFirsttimeBuyer(self):
        self.obj_SeleniumActions.waitForElementToClickOn(locator=self.HOFirstTimeBuyer_locator,
                                                         locatorType=self.HOFirstTimeBuyer_locatorType)

    def clickonAddinfoContinuebutton(self):
        self.obj_SeleniumActions.waitForElementToClickOn(locator=self.HOAddinfoContinue_locator,
                                                         locatorType=self.HOAddinfoContinue_locatorType)

    def completeStingraySpinning(self):
        self.obj_SeleniumActions.waitForElementToDisappear(timeout=15,locator=self.HOAddinfoSpinner_locator,
                                                            locatorType=self.HOAddinfoSpinner_locatorType)



    def addedAdditinalInfo(self,YearsAtCurrentAddress):
        self.completeStingraySpinning()
        self.yearsatcurrentaddress(YearsAtCurrentAddress)
        self.obj_SeleniumActions.sleepForWhile(2)
        self.selectRBforFirsttimeBuyer()
        self.clickonAddinfoContinuebutton()



