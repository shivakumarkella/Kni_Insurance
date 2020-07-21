from Pages_LOB.Locators import ApplicationLocators
from SeleniumActions import Actions



class HoFullQuoteRatesPage():

    #Locators

    Locator = ApplicationLocators.HoFullQuoteRatesPage
    HoPaymentPlan_locator=list(Locator['HoPaymentPlan'].items())[0][1]
    HoHoPaymentPlan_locatorType= list(Locator['HoPaymentPlan'].items())[0][0]
    HoAnnualPlanPayment_locator = list(Locator['HoAnnualPlanPayment'].items())[0][1]
    HoAnnualPlanPayment_locatorType = list(Locator['HoAnnualPlanPayment'].items())[0][0]
    HoRatesSaveAndExitButton_locator = list(Locator['HoRatesSaveAndExitButton'].items())[0][1]
    HoRatesSaveAndExitButton_locatorType = list(Locator['HoRatesSaveAndExitButton'].items())[0][0]
    HoRatesspinner_locator = list(Locator['SpinnerOverlay'].items())[0][1]
    HoRatesspinner_locatorType = list(Locator['SpinnerOverlay'].items())[0][0]



    def __init__(self, driver):
        self.driver = driver
        self.obj_SeleniumActions = Actions.SeleniumActions(self.driver)


    def paymentPlan(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HoPaymentPlan_locator,
                                                locatorType= self.HoHoPaymentPlan_locatorType)


    def annualPaymentPlan(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HoAnnualPlanPayment_locator,
                                                   locatorType=self.HoAnnualPlanPayment_locatorType)

    def ratesContinueButton(self):
        self.obj_SeleniumActions.clickmethod(locator=self.HoRatesSaveAndExitButton_locator,
                                             locatorType=self.HoRatesSaveAndExitButton_locatorType)

    def completeStingraySpinning(self):
        self.obj_SeleniumActions.waitForElementToDisappear(timeout=15,locator=self.HoRatesspinner_locator,
                                                            locatorType=self.HoRatesspinner_locatorType)

    def filldetailsforRatespage(self):
        self.paymentPlan()
        self.annualPaymentPlan()
        self.obj_SeleniumActions.sleepForWhile(10)
        self.ratesContinueButton()

