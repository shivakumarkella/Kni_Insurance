from Pages_LOB.Locators import ApplicationLocators
from Configfile.GetDrivers import GetDriverInstance
from Tests.TestData import TestData as TD
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SeleniumActions import Actions



class LoginPage():


    def __init__(self):
        self.Locator = ApplicationLocators.Loginpage
        obj_GetDriverInstance = GetDriverInstance(browser="firefox")
        self.driver=obj_GetDriverInstance.DriverInstance()
        self.obj_SeleniumActions = Actions.SeleniumActions(self.driver)

    def login(self):
        URL= list(self.Locator['URL'].items())[0][1]
        self.driver.get(URL)
        self.obj_SeleniumActions.sendKeys(locator="UserName",locatortype="name",message=TD.Username)
        self.obj_SeleniumActions.sendKeys(locator="password",locatortype="name",message=TD.Password)
        self.obj_SeleniumActions.find_element(locator="submit",locatortype="name").click()
        self.obj_SeleniumActions.waitforelementvisible_hidden_clickable(locator="spinnerOverlay",locatortype="id",hidden=1)
        self.obj_SeleniumActions.find_element(locator="Full Quote - HO",locatortype="link_text").click()






ff = LoginPage()
ff.login()

