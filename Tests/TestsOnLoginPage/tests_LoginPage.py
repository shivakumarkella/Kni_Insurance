from Pages_LOB.LoginPage.LoginPage import LoginPage
from Tests.testData import TestData as TD
from TestResults.customLogger import customLogger
import logging


class tests_LoginPage():


    def __init__(self,driver):
        self.log = customLogger(logging.INFO)
        self.obj_login = LoginPage(driver)



    def testCase1_ValidLogin(self,filnameRequired=0):
        if filnameRequired==1:
            fileName=self.obj_login.login(userName=TD.ValidUsername,password=TD.ValidPassword,filnameRequired=filnameRequired)
        else:
            self.obj_login.login(userName=TD.ValidUsername, password=TD.ValidPassword)
        self.log.info('Test Data Used for Login , User Name is :: ' + str(TD.ValidUsername))
        result=self.obj_login.verifyLoginSuceesful()
        self.log.info('is Login Suceesful , Result is :: ' + str(result))
        if filnameRequired==1:
            return fileName




    def testCase2_InvalidLogin(self):
        #Valid user Name , Invalid Password
        self.obj_login.login(userName=TD.ValidUsername,password=TD.InValidPassword)
        self.log.info('Test Data Used for Login , User Name is :: ' + str(TD.ValidUsername))
        result=self.obj_login.verifyInvalidUsername()
        self.log.info('is Login Suceesful , Result is :: ' + str(result))

    def testCase3_InvalidLogin(self):
        #invalid user name , Valid Password
        self.obj_login.login(userName=TD.InValidUsername,password=TD.ValidPassword)
        self.log.info('Test Data Used for Login , User Name is :: ' + str(TD.ValidUsername))
        result = self.obj_login.verifyInvalidUsername()
        self.log.info('is Login Suceesful , Result is :: ' + str(result))


    def testCase4_InvalidLogin(self):
        #invalid user name and password
        self.obj_login.login(userName=TD.InValidUsername,password=TD.InValidPassword)
        self.log.info('Test Data Used for Login , User Name is :: ' + str(TD.ValidUsername))
        result=self.obj_login.verifyLoginFailed()
        self.log.info('is Login Suceesful , Result is :: ' + str(result))




