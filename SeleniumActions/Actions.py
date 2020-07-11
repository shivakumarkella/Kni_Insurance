# Wait for Element and Return Element
# Screenshots
# Write a method Sleep()
# Writ a method to select * Dropdown, * check box, * radio Button * Alerts * Warnings



from selenium import webdriver
from selenium.webdriver.common.by import By as BY

import time
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import  *


class SeleniumActions():
    def __init__(self,driver):
        self.driver = driver

    def by_type(self,locatortype):
        if locatortype.lower()=="id":
            return BY.ID
        elif locatortype.lower()=="xpath":
            return BY.XPATH
        elif locatortype.lower() =="name":
            return BY.NAME
        elif locatortype.lower() =="link_text":
            return BY.LINK_TEXT
        elif locatortype.lower() == "class_name":
            return BY.CLASS_NAME
        elif locatortype.lower() == "tag_name":
            return BY.TAG_NAME
        elif locatortype.lower() == "css_selector":
            return BY.CSS_SELECTOR
        elif locatortype.lower() == "partial_link_text":
            return BY.PARTIAL_LINK_TEXT
        else:
            print("Locator Type is not supported " + locatortype)

    def get_element(self, locator, locatortype="id"):
        byType = self.by_type(locatortype)
        element = self.driver.find_element(byType, locator)
        return element

    def sendKeys(self, message,locator=None, locatortype=None, element=None):
        if element is None :
            element = self.get_element(locator=locator, locatortype=locatortype)
        element.send_keys(message)


    def timetosleep(self, timetosleep=10):
        time.sleep(timetosleep)


    def waitForActionsOnElement(self,timeout=10, pollFrequency=0.5):
        try:
            wait = wdw(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            # element = wait.until(EC.element_to_be_clickable((byType, locator)))

        except:
            print('Error while wait for the element.')
        return wait

        # if hidden is not None:
        #     wait.until(EC.invisibility_of_element_located(element))
        # if visible is not None:
        #     wait.until(EC.visibility_of_element_located(element))
        # if clickable is not None:
        #     wait.until(EC.element_to_be_clickable(element))
        #     self.driver.click(element)


    def waitForElementToDisappear(self,locator,locatorType='id',timeout=10,element=None):
        if element is None:
            element=self.get_element(locator=locator,locatortype=locatorType)
        wait=self.waitForActionsOnElement(timeout=timeout,pollFrequency=1)
        wait.until(EC.invisibility_of_element_located(element))

    def waitForElementToVisible(self,locator,locatorType='id',timeout=10,element=None):
        if element is None:
            element=self.get_element(locator=locator,locatortype=locatorType)
        wait=self.waitForActionsOnElement(timeout=timeout,pollFrequency=1)
        wait.until(EC.visibility_of_element_located(element))

    def waitForElementToClickOn(self,locator,locatorType='id',timeout=10):
        wait=self.waitForActionsOnElement(timeout=timeout,pollFrequency=1)
        byType=self.by_type(locatortype=locatorType)
        element=wait.until(EC.element_to_be_clickable((byType,locator)))
        element.click()





