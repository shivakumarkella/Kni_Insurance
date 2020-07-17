from Tests.TestsOnLoginPage import tests_LoginPage as loginPage
from Tests.TestsOnHoFullQuotePage import tests_HoFQApplicant as HoFqApplication
from Tests.TestsOnHoFullQuotePage import tests_HoFQTandC as HoTandC
from Tests.TestsOnHoFullQuotePage import tests_HoFQCredits as HoCredits
from Tests.TestsOnHoFullQuotePage import tests_HoFQAddInfo as HoAddinfo
import unittest
import pytest
from TestResults.customLogger import customLogger
import logging


@pytest.mark.usefixtures("oneTimeSetUp")
class test_happyPath(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def thisClassConfig(self):
        self.log = customLogger(logging.INFO)
        self.obj_loginPage=loginPage.tests_LoginPage(self.driver)
        self.obj_HoFqApplication=HoFqApplication.tests_HoFQApplicantPage(self.driver)
        self.obj_HoTandC = HoTandC.tests_HoFQTandC(self.driver)
        self.obj_HoCredits = HoCredits.tests_HoFQCredits(self.driver)
        self.obj_HoAddinfo = HoAddinfo.tests_HoFQAddinfo(self.driver)

    @pytest.mark.run(order=1)
    def tests_HoLobPath(self):
        fileName=self.obj_loginPage.testCase1_ValidLogin(filnameRequired=1)
        self.obj_HoFqApplication.tests_ValidDetailsOnApplicant(fileName=fileName)
        self.log.info('Filling Done on Ho Full Quote by using :: Method fillDetailsForHoFullQuote ')
        self.log.info(' Ho Full Quote T and C  :: Method ValidDeatilsonTandC ')
        self.obj_HoTandC.tests_ValidDeatilsonTandC()
        self.log.info(' on the Ho Full Quote T and C Page ')
        self.log.info('Terms and Conditions Accepted')
        self.obj_HoCredits.tests_ValidDeatilsonCredit()
        self.log.info('Current on the Credits Page')
        self.log.info('Credit page is completed')
        self.obj_HoAddinfo.tests_ValidDtailsOnAddinfo()
        self.log.info('Presently on Addinfo Page')




