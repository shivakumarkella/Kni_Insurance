from Pages_LOB.Locators import ApplicationLocators
from SeleniumActions import Actions



class HoFullQuoteAddingInvoice():

    #Locators
    Locator = ApplicationLocators.HoAddBillingInfoPage
    HoInvoice_locator=list(Locator['HoInvoice'].items())[0][1]
    HoInvoice_locatorType= list(Locator['HoInvoice'].items())[0][0]
    HoRenewalInvoice_locator = list(Locator['HoRenewalInvoice'].items())[0][1]
    HoRenewalInvoice_locatorType = list(Locator['HoRenewalInvoice'].items())[0][0]
    HoBillingContinueButton_locator = list(Locator['HoBillingInfoContinueButton'].items())[0][1]
    HoBillingContinueButton_locatorType = list(Locator['HoBillingInfoContinueButton'].items())[0][0]
    HOBillingspinner_locator = list(Locator['SpinnerOverlay'].items())[0][1]
    HOBillingspinner_locatorType = list(Locator['SpinnerOverlay'].items())[0][0]


    def __init__(self,driver):
        self.driver = driver
        self.obj_SeleniumActions = Actions.SeleniumActions(self.driver)



    def completeStingraySpinning(self):
        self.obj_SeleniumActions.waitForElementToDisappear(locator=self.HOBillingspinner_locator,
                                                            locatorType=self.HOBillingspinner_locatorType)



    def invoiceRecepient(self, selectvalue):
       self.obj_SeleniumActions.selectDropdown(locator=self.HoInvoice_locator,
                                                locatorType=self.HoInvoice_locatorType,SelectValue=selectvalue)


    def renewalRecepient(self, selectvalue):
       self.obj_SeleniumActions.selectDropdown(locator=self.HoRenewalInvoice_locator,
                                                locatorType=self.HoRenewalInvoice_locatorType,SelectValue=selectvalue)



    def billinginfoContinueButton(self):
       self.obj_SeleniumActions.clickmethod(locator=self.HoBillingContinueButton_locator,
                                                locatorType=self.HoBillingContinueButton_locatorType)


    def filldetailsforAddingBill(self,invoice,renewal):

        self.obj_SeleniumActions.LoadtheDomCompletely()
        self.completeStingraySpinning()
        self.invoiceRecepient(invoice)
        self.renewalRecepient(renewal)
        self.billinginfoContinueButton()
        self.completeStingraySpinning()

