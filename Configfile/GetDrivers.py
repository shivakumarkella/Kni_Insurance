from selenium import webdriver

class GetDriverInstance():
    def __init__(self,browser="Chrome"):
        self.browser = browser.lower()

    def DriverInstance(self):
        if self.browser == "firefox":
            driver = webdriver.Firefox()
            # driver= webdriver.Firefox(executable_path= "C:\\Users\\Sharat\\Workspace_python\\drivers\\geckodriver.exe")
        elif self.browser == "ie":
            driver = webdriver.Ie()
            # driver=webdriver.Ie(executable_path="C:\\Users\\Sharat\\Workspace_python\\drivers\\IEDriverServer.exe")
        else:
            driver =webdriver.Chrome()
            # driver=webdriver.Chrome(executable_path="C:\\Users\\Sharat\\Workspace_python\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(2)
        return driver




