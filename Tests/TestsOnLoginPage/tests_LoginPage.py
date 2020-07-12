from Pages_LOB.LoginPage import LoginPage
from Tests.testData import TestData as TD
from Documents.Configfile.GetDrivers import GetDriverInstance
import pytest
import unittest


class tests_LoginPage(unittest.TestCase):

    obj_GetDriverInstance = GetDriverInstance(browser="firefox")
    driver = obj_GetDriverInstance.DriverInstance()
    obj_login = LoginPage(driver)

    # Valid Credentials
    def test_TC1_ValidLogin(self):
        self.obj_login.login(userName=TD.ValidUsername,password=TD.ValidPassword)
        result=self.obj_login.verifyLoginSuceesful()


    # Valid user Name , Invalid Password
    def TC2_InvalidLogin(self):
        self.obj_login.login(userName=TD.ValidUsername,password=TD.InValidPassword)
        result=self.obj_login.verifyInvalidUsername()

    # Invalid user name , Valid Password
    def TC3_InvalidLogin(self):
        self.obj_login.login(userName=TD.InValidUsername,password=TD.ValidPassword)
        result = self.obj_login.verifyInvalidUsername()

    # Invalid user name and password
    def TC4_InvalidLogin(self):
        self.obj_login.login(userName=TD.InValidUsername,password=TD.InValidPassword)
        result=self.obj_login.verifyLoginFailed()
