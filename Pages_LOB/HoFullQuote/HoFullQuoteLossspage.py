from Pages_LOB.Locators import ApplicationLocators
from SeleniumActions import Actions


class HoFullQuoteLosses():

    # Locators
    Locator = ApplicationLocators.HoFullQuoteLosses
    HOConstructionType_locator = list(Locator["HOConstructionClase"].items())[0][1]
    HOConstructionType_locatorType = list(Locator["HOConstructionClase"].items())[0][0]
    HONumberofFamilies_locator = list(Locator["HONumberOfFamilies"].items())[0][1]
    HONumberofFamilies_locatorType = list(Locator["HONumberOfFamilies"].items())[0][0]
    HOUsage_locator = list(Locator["HOUsage"].items())[0][1]
    HOUsage_locatorType = list(Locator["HOUsage"].items())[0][0]
    HOLossesContinue_locator = list(Locator["HOLossesContinueButton"].items())[0][1]
    HOLossesContinue_locatorType = list(Locator["HOLossesContinueButton"].items())[0][0]
    HOLossespinner_locator = list(Locator['SpinnerOverlay'].items())[0][1]
    HOLossespinner_locatorType = list(Locator['SpinnerOverlay'].items())[0][0]


    def __init__(self,driver):
        self.driver = driver
        self.obj_SeleniumActions = Actions.SeleniumActions(self.driver)


    def selectConstructiontype(self,selectvalue):
        self.obj_SeleniumActions.selectDropdown(locator=self.HOConstructionType_locator,
                                                         locatorType=self.HOConstructionType_locatorType,SelectValue=selectvalue)

    def selectNumberofFamilies(self,selectvalue):
        self.obj_SeleniumActions.selectDropdown(locator=self.HONumberofFamilies_locator,
                                                         locatorType=self.HONumberofFamilies_locatorType,SelectValue=selectvalue)

    def selectUsage(self,selectvalue):
        self.obj_SeleniumActions.selectDropdown(locator=self.HOUsage_locator,
                                                         locatorType=self.HOUsage_locatorType,SelectValue=selectvalue)

    def clickonLossesContinueButton(self):
        self.obj_SeleniumActions.waitForElementToClickOn(locator=self.HOLossesContinue_locator,
                                                         locatorType=self.HOLossesContinue_locatorType)


    def completeStingraySpinning(self):
        self.obj_SeleniumActions.waitForElementToDisappear(locator=self.HOLossespinner_locator,
                                                            locatorType=self.HOLossespinner_locatorType)

    def losses(self,selectvalueforConstruction,selectvalueforFamily,selectvalueforUsage):
        self.completeStingraySpinning()
        self.selectConstructiontype(selectvalueforConstruction)
        self.selectNumberofFamilies(selectvalueforFamily)
        self.selectUsage(selectvalueforUsage)
        self.clickonLossesContinueButton()
        self.completeStingraySpinning()
