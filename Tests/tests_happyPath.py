from Tests.TestsOnLoginPage import tests_LoginPage as loginPage
from Tests.TestsOnHoFullQuotePage import tests_HoFullQuotePage as HoFqApplication
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp")
class test_happyPath(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def thisClassConfig(self):
        self.obj_loginPage=loginPage.tests_LoginPage(self.driver)
        self.obj_HoFqApplication=HoFqApplication.tests_HoFullQuotePage(self.driver)

    @pytest.mark.run(order=1)
    def tests_HoLobPath(self):
        self.obj_loginPage.testCase1_ValidLogin()
        self.obj_HoFqApplication.testCase1_ValidDetailsOnHoFQ()

