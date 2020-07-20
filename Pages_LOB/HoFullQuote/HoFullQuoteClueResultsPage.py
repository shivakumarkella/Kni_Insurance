from Pages_LOB.Locators import ApplicationLocators
from SeleniumActions import Actions



class HoFullQuoteClueResultPage():

    #Locators
    Locator = ApplicationLocators.HoClueResults
    HOClueResultspinner_locator = list(Locator['SpinnerOverlay'].items())[0][1]
    HOClueResultspinner_locatorType = list(Locator['SpinnerOverlay'].items())[0][0]
    HOProgress_locator = list(Locator['HoProgressBar'].items())[0][1]
    HOProgress_locatorType = list(Locator['HoProgressBar'].items())[0][0]
    HoClueResultContinueButton_locator=list(Locator['HoClueResultContinueButton'].items())[0][1]
    HoClueResultContinueButton_locatorType= list(Locator['HoClueResultContinueButton'].items())[0][0]
    HoClueResultFullRight_locator = list(Locator['HoClueResultFullRight'].items())[0][1]
    HoClueResultFullRight_locatorType = list(Locator['HoClueResultFullRight'].items())[0][0]

    def __init__(self, driver):
        self.driver = driver
        self.obj_SeleniumActions = Actions.SeleniumActions(self.driver)

    def completeStingraySpinning(self):
        self.obj_SeleniumActions.waitForElementToDisappear(timeout=30,locator=self.HOClueResultspinner_locator,
                                                           locatorType=self.HOClueResultspinner_locatorType)

    def completeProgressbar(self):
        self.obj_SeleniumActions.waitForElementToDisappear(timeout=30, locator=self.HOProgress_locator,
                                                           locatorType=self.HOProgress_locatorType)

    def clueResultsContinueButton(self):
        self.obj_SeleniumActions.clickmethod(locator=self.HoClueResultContinueButton_locator,
                                             locatorType=self.HoClueResultContinueButton_locatorType)

    def screenShot(self,screenShotName='Default'):
        self.obj_SeleniumActions.takeScreenShot(screenShotName=screenShotName)

    def scrollTheResultsTableToRight(self):
        self.obj_SeleniumActions.scrollLeftInWebElement(cssSelector=self.HoClueResultFullRight_locator)


    def tests_clickoncontinuebuttonforClueResults(self):
        self.completeStingraySpinning()
        self.obj_SeleniumActions.sleepForWhile(30)
        self.screenShot(screenShotName='ClueResultsLeft')
        self.obj_SeleniumActions.sleepForWhile(1)
        self.scrollTheResultsTableToRight()
        self.screenShot(screenShotName='ClueResultsRight')
        self.obj_SeleniumActions.sleepForWhile(1)
        self.clueResultsContinueButton()
