from Pages_LOB.Locators import ApplicationLocators
from SeleniumActions import Actions


class HoFQTandCPage():

    # Locators
    Locator = ApplicationLocators.HoFullQuoteAcceptAgrement
    HOAddressspinner_locator = list(Locator['SpinnerOverlay'].items())[0][1]
    HOAddressspinner_locatorType = list(Locator['SpinnerOverlay'].items())[0][0]
    HOAcceptAgreementRB_locator = list(Locator['HOAcceptAgreementRB'].items())[0][1]
    HOAcceptAgreementRB_locatorType = list(Locator['HOAcceptAgreementRB'].items())[0][0]
    HOAcceptAgreementContinueButton_locator = list(Locator['HOAcceptAgreementContinueButton'].items())[0][1]
    HOAcceptAgreementContinueButton_locatorType = list(Locator['HOAcceptAgreementContinueButton'].items())[0][0]


    def __init__(self,driver):
        self.driver = driver
        self.obj_SeleniumActions = Actions.SeleniumActions(self.driver)

    def selectAcceptAgrementRB(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HOAcceptAgreementRB_locator,
                                                   locatorType=self.HOAcceptAgreementRB_locatorType)
        self.obj_SeleniumActions.sleepForWhile(5)

    def clickOnAcceptAgrementContinueButton(self):
        self.obj_SeleniumActions.clickmethod(locator=self.HOAcceptAgreementContinueButton_locator,
                                                         locatorType=self.HOAcceptAgreementContinueButton_locatorType)

    def completeStingraySpinning(self):
        self.obj_SeleniumActions.waitForElementToDisappear(timeout=5,locator=self.HOAddressspinner_locator,
                                                            locatorType=self.HOAddressspinner_locatorType)



    def acceptTermsAndCondition(self):
        self.completeStingraySpinning()
        # self.clickOnAcceptAgrementContinueButton()
        # self.obj_SeleniumActions.sleepForWhile(5)
        self.clickOnAcceptAgrementContinueButton()
        self.obj_SeleniumActions.sleepForWhile(5)
        self.obj_SeleniumActions.handlingalert()
        self.obj_SeleniumActions.sleepForWhile(5)
        self.selectAcceptAgrementRB()
        self.clickOnAcceptAgrementContinueButton()
        self.obj_SeleniumActions.sleepForWhile(5)
        # self.clickOnAcceptAgrementContinueButton()
