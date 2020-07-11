from Pages_LOB.LoginPage import LoginPage
from Tests.TestData import TestData as TD
from Documents.Configfile.GetDrivers import GetDriverInstance


class Test_LoginPage():

    def __init__(self):
        obj_GetDriverInstance = GetDriverInstance(browser="firefox")
        self.driver = obj_GetDriverInstance.DriverInstance()
        self.obj_login=LoginPage(self.driver)

    def TC1_ValidLogin(self):
        self.obj_login.login(userName=TD.ValidUsername,password=TD.ValidPassword)
        result=self.obj_login.verifyLoginSuceesful()


    def TC2_InvalidLogin(self):
        #Valid user Name , Invalid Password
        self.obj_login.login(userName=TD.ValidUsername,password=TD.InValidPassword)
        result=self.obj_login.verifyInvalidUsername()


    def TC3_InvalidLogin(self):
        #invalid user name , Valid Password
        self.obj_login.login(userName=TD.InValidUsername,password=TD.ValidPassword)
        result = self.obj_login.verifyInvalidUsername()


    def TC4_InvalidLogin(self):
        #invalid user name and password
        self.obj_login.login(userName=TD.InValidUsername,password=TD.InValidPassword)
        result=self.obj_login.verifyLoginFailed()



obj_TestLoginPage=Test_LoginPage()
obj_TestLoginPage.TC1_ValidLogin()