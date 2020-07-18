from Pages_LOB.Locators import ApplicationLocators
from SeleniumActions import Actions



class HoFullQuoteClueResultPage():

    #Locators
    Locator = ApplicationLocators.HoClueResults
    HOClueResultspinner_locator = list(Locator['SpinnerOverlay'].items())[0][1]
    HOClueResultspinner_locatorType = list(Locator['SpinnerOverlay'].items())[0][0]
    HoClueResultContinueButton_locator=list(Locator['HoE2valueResultContinueButton'].items())[0][1]
    HoClueResultContinueButton_locatorType= list(Locator['HoE2valueResultContinueButton'].items())[0][0]

    def __init__(self, driver):
        self.driver = driver
        self.obj_SeleniumActions = Actions.SeleniumActions(self.driver)

    def completeStingraySpinning(self):
        self.obj_SeleniumActions.waitForElementToDisappear(locator=self.HOClueResultspinner_locator,
                                                           locatorType=self.HOClueResultspinner_locatorType)

    def clueResultsContinueButton(self):
        self.obj_SeleniumActions.clickmethod(locator=self.HoClueResultContinueButton_locator,
                                             locatorType=self.HoClueResultContinueButton_locatorType)


    def tests_clickoncontinuebuttonforClueResults(self):
        self.completeStingraySpinning()
        self.clueResultsContinueButton()
