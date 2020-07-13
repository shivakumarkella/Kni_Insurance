from Pages_LOB.LoginPage import LoginPage
from Tests.testData import TestData as TD
import pytest
import unittest
from TestResults.customLogger import customLogger


@pytest.mark.usefixtures("oneTimeSetUp")
class tests_LoginPage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def thisclassSetup(self):
        self.log = customLogger()
        self.obj_login = LoginPage(self.driver)


    @pytest.mark.run(order=1)
    def testCase1_ValidLogin(self):
        self.obj_login.login(userName=TD.ValidUsername,password=TD.ValidPassword)

        # result=self.obj_login.verifyLoginSuceesful()



    # @pytest.mark.run(order=3)
    # def testCase2_InvalidLogin(self):
    #     #Valid user Name , Invalid Password
    #     self.obj_login.login(userName=TD.ValidUsername,password=TD.InValidPassword)
    #     result=self.obj_login.verifyInvalidUsername()

    # @pytest.mark.run(order=4)
    # def testCase3_InvalidLogin(self):
    #     #invalid user name , Valid Password
    #     self.obj_login.login(userName=TD.InValidUsername,password=TD.ValidPassword)
    #     result = self.obj_login.verifyInvalidUsername()

    # @pytest.mark.run(order=1)
    # def testCase4_InvalidLogin(self):
    #     #invalid user name and password
    #     self.obj_login.login(userName=TD.InValidUsername,password=TD.InValidPassword)
    #     result=self.obj_login.verifyLoginFailed()
