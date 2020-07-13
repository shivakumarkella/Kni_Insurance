from Pages_LOB.Locators import ApplicationLocators
from SeleniumActions import Actions



class HoFullQuotePage():

    #Locators
    Locator = ApplicationLocators.HoFullQuote
    Ho6oDaysPopUp_locator=list(Locator['Days60PopUpButton'].items())[0][1]
    Ho6oDaysPopUp_locatorType= list(Locator['Days60PopUpButton'].items())[0][0]
    HOFullQuoteLink_locator = list(Locator['HOFullQuoteLink'].items())[0][1]
    HOFullQuoteLink_locatorType = list(Locator['HOFullQuoteLink'].items())[0][0]

    def __init__(self,driver):
        self.driver = driver
        self.obj_SeleniumActions = Actions.SeleniumActions(self.driver)

    def clickOn60DaysPop_up(self):
        self.obj_SeleniumActions.waitForElementToClickOn(locator=self.Ho6oDaysPopUp_locator,
                                                         locatorType=self.Ho6oDaysPopUp_locatorType)

    def gotoHoFullQuotePage(self):
        self.obj_SeleniumActions.waitForElementToClickOn(locator=self.HOFullQuoteLink_locator,
                                                         locatorType=self.HOFullQuoteLink_locatorType)

    def fillDetailsForHoFullQuote(self):
        self.gotoHoFullQuotePage()
        self.clickOn60DaysPop_up()