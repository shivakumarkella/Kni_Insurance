from Pages_LOB.LoginPage import LoginPage
from Tests.testData import TestData as TD
from TestResults.customLogger import customLogger


class tests_LoginPage():


    def __init__(self,driver):
        self.log = customLogger()
        self.obj_login = LoginPage(driver)


    def testCase1_ValidLogin(self):
        self.obj_login.login(userName=TD.ValidUsername,password=TD.ValidPassword)
        result=self.obj_login.verifyLoginSuceesful()



    def testCase2_InvalidLogin(self):
        #Valid user Name , Invalid Password
        self.obj_login.login(userName=TD.ValidUsername,password=TD.InValidPassword)
        result=self.obj_login.verifyInvalidUsername()

    def testCase3_InvalidLogin(self):
        #invalid user name , Valid Password
        self.obj_login.login(userName=TD.InValidUsername,password=TD.ValidPassword)
        result = self.obj_login.verifyInvalidUsername()


    def testCase4_InvalidLogin(self):
        #invalid user name and password
        self.obj_login.login(userName=TD.InValidUsername,password=TD.InValidPassword)
        result=self.obj_login.verifyLoginFailed()
