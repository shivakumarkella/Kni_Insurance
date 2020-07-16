from Tests.TestsOnLoginPage import tests_LoginPage as loginPage
from Tests.TestsOnHoFullQuotePage import tests_HoFQApplicant as HoFqApplication
from Tests.TestsOnHoFullQuotePage import tests_HoFQTandC as HoTandC
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp")
class test_happyPath(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def thisClassConfig(self):
        self.obj_loginPage=loginPage.tests_LoginPage(self.driver)
        self.obj_HoFqApplication=HoFqApplication.tests_HoFQApplicantPage(self.driver)
        self.obj_HoTandC = HoTandC.tests_HoFQTandC(self.driver)

    @pytest.mark.run(order=1)
    def tests_HoLobPath(self):
        self.obj_loginPage.testCase1_ValidLogin()
        self.obj_HoFqApplication.tests_ValidDetailsOnApplicant()
        self.obj_HoTandC.tests_ValidDeatilsonTandC()



