from Pages_LOB.Locators import ApplicationLocators
from SeleniumActions import Actions



class HoFullQuoteEndorsementPage():

    #Locators
    Locator = ApplicationLocators.HoEndorsementPage
    HOEndorsementspinner_locator = list(Locator['SpinnerOverlay'].items())[0][1]
    HOEndorsementspinner_locatorType = list(Locator['SpinnerOverlay'].items())[0][0]
    HoEndorsementContinueButton_locator=list(Locator['HoEndorsmentContinueButton'].items())[0][1]
    HoEndorsementContinueButton_locatorType= list(Locator['HoEndorsmentContinueButton'].items())[0][0]

    def __init__(self, driver):
        self.driver = driver
        self.obj_SeleniumActions = Actions.SeleniumActions(self.driver)

    def completeStingraySpinning(self):
        self.obj_SeleniumActions.waitForElementToDisappear(locator=self.HOEndorsementspinner_locator,
                                                           locatorType=self.HOEndorsementspinner_locatorType)

    def endorsementContinueButton(self):
        self.obj_SeleniumActions.clickmethod(locator=self.HoEndorsementContinueButton_locator,
                                             locatorType=self.HoEndorsementContinueButton_locatorType)


    def tests_clickoncontinuebuttonforEndorsement(self):
        self.completeStingraySpinning()
        self.endorsementContinueButton()
