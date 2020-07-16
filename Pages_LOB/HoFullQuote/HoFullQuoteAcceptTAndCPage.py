from Pages_LOB.Locators import ApplicationLocators
from SeleniumActions import Actions


class HoFullQuoteAcceptTermsAndConditionPage():

    # Locators
    Locator = ApplicationLocators.HoFullQuoteAcceptAgrement
    HOAcceptSpinner_locator = list(Locator["SpinnerOverlay"].items())[0][1]
    HOAcceptSpinner_locatorType = list(Locator["SpinnerOverlay"].items())[0][0]
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

    def clickOnAcceptAgrementContinueButton(self):
        self.obj_SeleniumActions.waitForElementToClickOn(locator=self.HOAcceptAgreementContinueButton_locator,
                                                         locatorType=self.HOAcceptAgreementContinueButton_locatorType)

    def completeStingraySpinning(self):
        self.obj_SeleniumActions.waitForElementToDisappear(locator=self.HOAcceptSpinner_locator,
                                                            locatorType=self.HOAcceptSpinner_locatorType)

    def acceptTermsAndCondition(self):
        self.completeStingraySpinning()
        self.selectAcceptAgrementRB()
        self.clickOnAcceptAgrementContinueButton()
