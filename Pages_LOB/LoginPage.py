from Pages_LOB.Locators import ApplicationLocators
from SeleniumActions import Actions



class LoginPage():

    # Get Locators and its types of Login Page
    Locator = ApplicationLocators.Loginpage
    url_HomePage = list(Locator['URL'].items())[0][1]
    lp_userName_Locator = list(Locator['UserName'].items())[0][1]
    lp_userName_LocatorType = list(Locator['UserName'].items())[0][0]
    lp_password_locator = list(Locator['Password'].items())[0][1]
    lp_password_locatorType = list(Locator['Password'].items())[0][0]
    lp_LoginButton_locator=list(Locator['LoginButton'].items())[0][1]
    lp_LoginButton_locatorType=list(Locator['LoginButton'].items())[0][0]
    lp_spinner_locator=list(Locator['SpinnerOverlay'].items())[0][1]
    lp_spinner_locatorType = list(Locator['SpinnerOverlay'].items())[0][0]
    HOFullQuoteLink_locator = list(Locator['HOFullQuoteLink'].items())[0][1]
    HOFullQuoteLink_locatorType = list(Locator['HOFullQuoteLink'].items())[0][0]


    def __init__(self,driver):
        self.driver =driver
        self.obj_SeleniumActions = Actions.SeleniumActions(self.driver)

    def enterUserName(self,userName):
        self.obj_SeleniumActions.sendKeys(locator=self.lp_userName_Locator,
                                          locatortype=self.lp_userName_LocatorType,
                                          message=userName)

    def enterPassword(self, password):
        self.obj_SeleniumActions.sendKeys(locator=self.lp_password_locator,
                                          locatortype=self.lp_password_locatorType,
                                          message=password)
    def clickOnLoginButton(self):
        self.obj_SeleniumActions.waitForElementToClickOn(locator=self.lp_LoginButton_locator,locatorType=self.lp_password_locatorType)

    def CompleteStingraySpinning(self):
        self.obj_SeleniumActions.waitForElementToDisappear(locator=self.lp_spinner_locator,locatorType=self.lp_spinner_locatorType)

    def goToLoginPage(self):
        self.driver.get(self.url_HomePage)

    def login(self,userName,password):
        self.goToLoginPage()
        self.enterUserName(userName)
        self.enterPassword(password)
        self.clickOnLoginButton()
        self.CompleteStingraySpinning()
        self.obj_SeleniumActions.waitForElementToClickOn(locator=self.HOFullQuoteLink_locator,locatorType=self.HOFullQuoteLink_locatorType)