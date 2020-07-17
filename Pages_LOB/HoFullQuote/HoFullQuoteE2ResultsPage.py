from Pages_LOB.Locators import ApplicationLocators
from SeleniumActions import Actions



class HoFullQuoteE2ValueResultPage():

    #Locators
    Locator = ApplicationLocators.HoFullQuoteE2ValueResult
    HOE2Resultpinner_locator = list(Locator['SpinnerOverlay'].items())[0][1]
    HOE2Resultpinner_locatorType = list(Locator['SpinnerOverlay'].items())[0][0]
    HoResultContinueButton_locator=list(Locator['HoE2valueResultContinueButton'].items())[0][1]
    HoResultContinueButtonType= list(Locator['HoE2valueResultContinueButton'].items())[0][0]

    def __init__(self, driver):
        self.driver = driver
        self.obj_SeleniumActions = Actions.SeleniumActions(self.driver)

    def completeStingraySpinning(self):
        self.obj_SeleniumActions.waitForElementToDisappear(locator=self.HOE2Resultpinner_locator,
                                                            locatorType=self.HOE2Resultpinner_locatorType)

    def e2ResultsContinueButton(self):
        self.obj_SeleniumActions.clickmethod(locator=self.HoResultContinueButton_locator,
                                             locatorType=self.HoResultContinueButtonType)


    def tests_clickoncontinuebuttonforE2Results(self):
        self.completeStingraySpinning()
        self.e2ResultsContinueButton()
