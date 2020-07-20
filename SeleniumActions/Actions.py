from selenium import webdriver
from selenium.webdriver.common.by import By as BY
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import  *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from TestResults.customLogger import customLogger
from datetime import datetime
from pytz import timezone
from tzlocal import get_localzone
import logging
from Tests.testData import TestData as TD
format = "%Y_%m_%d_%H_%M_%S" # time stamp will come in this format

class SeleniumActions():
    def __init__(self,driver):
        self.driver = driver
        self.timeStamp = (datetime.now(timezone(str(get_localzone()).upper()))).strftime(format)

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
                                                     ElementNotSelectableException,TimeoutException])

            # element = wait.until(EC.element_to_be_clickable((byType, locator)))

        except:
            print('Error while wait for the element.')
        return wait

    def waitForElementToDisappear(self,locator,locatorType='id',timeout=10,element=None):
            if element is None:
                element=self.get_element(locator=locator,locatortype=locatorType)
            wait=self.waitForActionsOnElement(timeout=timeout,pollFrequency=1)
            wait.until(EC.invisibility_of_element_located(element))


    def waitForElementToVisible(self,locator,locatorType='id',timeout=10,element=None):
        try:
            if element is None:
                element=self.get_element(locator=locator,locatortype=locatorType)
            wait=self.waitForActionsOnElement(timeout=timeout,pollFrequency=1)
            wait.until(EC.visibility_of_element_located(element))
        except:
            print('Error while waiting for the element')
        return element





    def waitForElementToClickOn(self,locator,locatorType='id',timeout=10):
        try:
            element = None
            wait=self.waitForActionsOnElement(timeout=timeout,pollFrequency=1)
            byType=self.by_type(locatortype=locatorType)
            element=wait.until(EC.element_to_be_clickable((byType,locator)))
            if element is not None:
               element.click()

        except:
            print('Waited for' + locator + 'to be clicked, but ' + locatorType + 'not found')


    def isElementPresent(self,locator,locatorType='id',timeout=10):
        wait=self.waitForActionsOnElement()
        byType=self.by_type(locatortype=locatorType)
        element=wait.until(EC.presence_of_element_located((byType,locator)))
        if element is not None:
            return True
        else:
            return False




    def selectDropdown(self,locator, locatorType,element=None,SelectValue=None):
        element = Select(self.get_element(locatortype=locatorType,
                                           locator=locator))
        self.log = customLogger(logging.DEBUG)
        self.log.error(SelectValue)
        element.select_by_value(SelectValue)





    def selectRadiobutton(self,locator,locatorType,element=None):
        if element is None:
            element = self.get_element(locator=locator, locatortype=locatorType)
            element.click()
            element.click()
        else:
            element.click()


    def selectCheckbox(self,locator,locatorType,element=None):
        if element is None:
            element =self.get_element(locator=locator, locatortype=locatorType)
            element.click()
        else:
            element.click()


    def handlingalert(self):
       checkalert= self.driver.switch_to.alert
       checkalert.accept()


    def waitForPageLoaded(self):
        wait = self.waitForActionsOnElement(timeout=30)
        return str((self.driver).execute_script("return document.readyState")) == "complete"

    def LoadtheDomCompletely(self):
        try:
            i = 1
            while (i == 1):
                isLoaded = self.waitForPageLoaded()
                if isLoaded == True:
                    i = 0
        except:
            print('time out , page not loaded yet')

    def tabout(self):
       A= ActionChains(driver=self.driver)
       A.send_keys(Keys.TAB)


    def getTheDropDownSelectedValue(self,locator, locatorType,element=None,SelectValue=None):
        selectedValue = Select(self.get_element(locatortype=locatorType,
                                          locator=locator)).first_selected_option.get_attribute("value")
        return selectedValue

    def getListOFWindows(self):
        handles=self.driver.window_handles
        return handles

    def sleepForWhile(self,sleepTime=5):
        time.sleep(sleepTime)


    def clickmethod(self,locator, locatorType):
        element = self.get_element(locator=locator,locatortype=locatorType)
        element.click()

    def getTheCurrentWindowSize(self):
        # get the Window size i.e. height and width
            height = self.driver.execute_script("return window.innerHeight;")
            width = self.driver.execute_script("return window.innerWidth;")
            return height,width


    def scrollDown(self,height=0,width=0):
        if height==0 or width==0:
            height,width=self.getTheCurrentWindowSize()
        scriptForScroll = 'window.scrollBy(0,' + str(height) + ');'
        self.driver.execute_script("{}".format(scriptForScroll))

    def scrollUp(self,height=0,width=0):
        if height==0 or width==0:
            height,width=self.getTheCurrentWindowSize()
        scriptForScroll = 'window.scrollBy(0,' + str(-height) + ');'
        self.driver.execute_script("{}".format(scriptForScroll))

    def highlight(self, element,directory_to_save_ScreenShot='Default'):
        """Highlights (blinks) a Selenium Webdriver element"""
        driver = self.driver
        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",element, s)
        original_style = element.get_attribute('style')
        apply_style("background: yellow; border: 2px solid red;")
        if directory_to_save_ScreenShot.lower()=='default':
            print('only highlight the web element')
        else:
            self.driver.save_screenshot(directory_to_save_ScreenShot)
        time.sleep(1)
        apply_style(original_style)

    def takeScreenShot(self,element='Default',typeOfScreenShot='Default',screenShotName='Default',path='Default',returnScreenShotName=False):
        typeOfScreenShot=typeOfScreenShot.lower()
        screenShotName=screenShotName.lower()
        path=path.lower()
        if typeOfScreenShot=='default':
            typeOfScreenShot='.png'
        else:
            typeOfScreenShot='.jpg'
        if screenShotName=='default':
            screenShotName='Demo'
        if path=='default':
            path=TD.screenShotLocation

        # To maintain Unique file name adding the time stamp to the screenshot
        screenShotName=str(screenShotName)+str(self.timeStamp)
        # by adding timestamp (.) is part of the file name, hence replace (.) with empty
        screenShotName=screenShotName.replace('.','')

        directory_to_save_ScreenShot=path+screenShotName+typeOfScreenShot

        if str(element).lower()=='default':
            self.driver.save_screenshot(directory_to_save_ScreenShot)
        else:
            self.highlight(element,directory_to_save_ScreenShot)


        if returnScreenShotName==True:
            return directory_to_save_ScreenShot

    def scrollLeftInWebElement(self,cssSelector):
        scriptToExecute = "document.querySelector""('{}').scrollLeft=530".format(cssSelector)
        self.driver.execute_script("{}".format(scriptToExecute))

    def getWebElements(self, locator, locatorType='xpath'):
        byType=self.by_type(locatortype=locatorType)
        webElements=self.driver.find_elements(byType,locator)

        return webElements