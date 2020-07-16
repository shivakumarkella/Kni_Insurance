from Pages_LOB.Locators import ApplicationLocators
from SeleniumActions import Actions


class HoFullQuoteCreditPage():
    Locator = ApplicationLocators.HoFullQuoteCreditPage
    HOCreditspinner_locator = list(Locator['SpinnerOverlay'].items())[0][1]
    HOCreditspinner_locatorType = list(Locator['SpinnerOverlay'].items())[0][0]
    HOCreditContinueButton_locator = list(Locator['HOCreditContinue'].items())[0][1]
    HOCreditContinueButton_locatorType = list(Locator['HOCreditContinue'].items())[0][0]


    def __init__(self, driver):
        self.driver = driver
        self.obj_SeleniumActions = Actions.SeleniumActions(self.driver)

    def completeStingraySpinning(self):
        self.obj_SeleniumActions.waitForElementToDisappear(locator=self.HOCreditspinner_locator,
                                                            locatorType=self.HOCreditspinner_locatorType)


    def clickonCreditContinuebutton(self):
        self.obj_SeleniumActions.clickmethod(locator=self.HOCreditContinueButton_locator,
                                                         locatorType=self.HOCreditContinueButton_locatorType)




    def creditscoredetails(self):
     self.completeStingraySpinning()
     self.obj_SeleniumActions.sleepForWhile(10)
     self.clickonCreditContinuebutton()