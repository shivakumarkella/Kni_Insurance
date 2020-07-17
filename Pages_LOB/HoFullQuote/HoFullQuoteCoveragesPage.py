from Pages_LOB.Locators import ApplicationLocators
from SeleniumActions import Actions



class HoFullQuoteCoveragesPage():

    #Locators
    Locator = ApplicationLocators.HoFullQuoteCoverages
    HoCoverageE_locator=list(Locator['HoCoverageE'].items())[0][1]
    HoCoverageE_locatorType= list(Locator['HoCoverageE'].items())[0][0]
    HoCoverageF_locator = list(Locator['HoCoverageF'].items())[0][1]
    HoCoverageF_locatorType = list(Locator['HoCoverageF'].items())[0][0]
    HoPolicyDedcutble_locator = list(Locator['HoPolicyDeductble'].items())[0][1]
    HoPolicyDedcutble_locatorType = list(Locator['HoPolicyDeductble'].items())[0][0]
    HoCoveragesContinueButton_locator = list(Locator['HoCoveragesContinueButton'].items())[0][1]
    HoCoveragesContinueButton_locatorType = list(Locator['HoCoveragesContinueButton'].items())[0][0]
    HOCoveragespinner_locator = list(Locator['SpinnerOverlay'].items())[0][1]
    HOCoveragespinner_locatorType = list(Locator['SpinnerOverlay'].items())[0][0]


    def __init__(self,driver):
        self.driver = driver
        self.obj_SeleniumActions = Actions.SeleniumActions(self.driver)



    def completeStingraySpinning(self):
        self.obj_SeleniumActions.waitForElementToDisappear(locator=self.HOCoveragespinner_locator,
                                                            locatorType=self.HOCoveragespinner_locatorType)



    def coverageEvalue(self, selectvalue):
       self.obj_SeleniumActions.selectDropdown(locator=self.HoCoverageE_locator,
                                                locatorType=self.HoCoverageE_locatorType,SelectValue=selectvalue)


    def coverageFvalue(self, selectvalue):
       self.obj_SeleniumActions.selectDropdown(locator=self.HoCoverageF_locator,
                                                locatorType=self.HoCoverageF_locatorType,SelectValue=selectvalue)

    def policyDeductble(self, selectvalue):
       self.obj_SeleniumActions.selectDropdown(locator=self.HoPolicyDedcutble_locator,
                                                locatorType=self.HoPolicyDedcutble_locatorType,SelectValue=selectvalue)

    def coverageContinueButton(self):
       self.obj_SeleniumActions.clickmethod(locator=self.HoCoveragesContinueButton_locator,
                                                locatorType=self.HoCoveragesContinueButton_locatorType)


    def filldetailsforCoverages(self, coverageEvalue, coverageFvalue, policydeductble):

        self.obj_SeleniumActions.LoadtheDomCompletely()
        self.completeStingraySpinning()
        self.coverageEvalue(coverageEvalue)
        self.coverageFvalue(coverageFvalue)
        self.policyDeductble(policydeductble)
        self.coverageContinueButton()

