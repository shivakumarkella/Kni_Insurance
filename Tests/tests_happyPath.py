from Tests.TestsOnLoginPage import tests_LoginPage as loginPage
from Tests.TestsOnHoFullQuotePage import tests_HoFQApplicant as HoFqApplication
from Tests.TestsOnHoFullQuotePage import tests_HoFQTandC as HoTandC
from Tests.TestsOnHoFullQuotePage import tests_HoFQCredits as HoCredits
from Tests.TestsOnHoFullQuotePage import tests_HoFQAddInfo as HoAddinfo
from Tests.TestsOnHoFullQuotePage import tests_HoFQLosses as HoLosses
from Tests.TestsOnHoFullQuotePage import tests_HoFQE2Value as HoE2value
from Tests.TestsOnHoFullQuotePage import tests_HoFQE2Reults as HoE2Result
from Tests.TestsOnHoFullQuotePage import tests_HoFQCoverages as HoCoverages
from Tests.TestsOnHoFullQuotePage import tests_HoFQProperty as HoProperty
from Tests.TestsOnHoFullQuotePage import tests_HoFQUWQuests as HoUWQuest
from Tests.TestsOnHoFullQuotePage import tests_HoFQClueResults as HoClueResults
from Tests.TestsOnHoFullQuotePage import tests_HoFQEndorsement as HoEndorsement
from Tests.TestsOnHoFullQuotePage import tests_HoFQBillingInfo as HoBilling
from Tests.TestsOnHoFullQuotePage import tests_HoFQRates as HoRates
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
        self.obj_HoLosses=HoLosses.tests_HoFQLossesPage(self.driver)
        self.obj_HoE2value=HoE2value.tests_HoFQE2ValuePage(self.driver)
        self.obj_HoE2Result=HoE2Result.tests_HoFQE2ResultsPage(self.driver)
        self.obj_HoCoverages=HoCoverages.tests_HoFQCoveragePage(self.driver)
        self.obj_HoProperty= HoProperty.tests_HoFQPropertyPage(self.driver)
        self.obj_HoUWQuest=HoUWQuest.tests_HoFQCoveragePage(self.driver)
        self.obj_HoClueResults= HoClueResults.tests_HoFQClueresultsPage(self.driver)
        self.obj_HoEndorsement= HoEndorsement.tests_HoFQEndorsementPage(self.driver)
        self.obj_HoBilling=HoBilling.tests_HoFQBillingInfoPage(self.driver)
        self.obj_HoRates= HoRates.tests_HoFQRatesPage(self.driver)



    @pytest.mark.run(order=1)
    def tests_HoLobPath(self):
        self.obj_loginPage.testCase1_ValidLogin()
        self.obj_HoFqApplication.tests_ValidDetailsOnApplicant()
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
        self.log.info('Credit Pag Details Added')
        self.obj_HoLosses.tests_ValidDtailsOnLosses()
        self.log.info('Presntly on the Losses Info Page')
        self.log.info('Information added on the Losses Page')
        self.obj_HoE2value.tests_ValidDetailsOnE2ValuePage()
        self.log.info('Third Party Valuation Page called E2Value')
        self.log.info('Third Party Valuation completed')
        self.obj_HoE2Result.tests_clickE2ResultContinuebutton()
        self.log.info('The E2Value Calculated and Displayed the Results')
        self.log.info('The E2 reults are correct and clicked on continue button')
        self.obj_HoCoverages.tests_ValidDetailsOnCoveragesPage()
        self.log.info('The Coverages Values are Retained from the E2 Calculated fields now entering other Coverages')
        self.log.info('The Coverages Values are Calculated')
        self.obj_HoProperty.tests_ValidDetailsOnPropertyPage()
        self.log.info('The property value are being Caluclated')
        self.log.info('The Proprty Page Completed')
        self.obj_HoUWQuest.tests_ValidDetailsOnUWQuest()
        self.log.info('The UW questions started the Answering')
        self.log.info('The UW Questions Completed')
        self.obj_HoClueResults.tests_clickClueContinuebutton()
        self.log.info("Laned on the Clue Results page and Screenshot Captured")
        self.log.info("Clicked on the Continue Button")
        self.obj_HoEndorsement.tests_clickEndorsementContinuebutton()
        self.log.info("Landed on Endorsement Page")
        self.log.info("Continue Button clicked on Endorsement Page ")
        self.obj_HoBilling.tests_ValidDetailsOnBillingInfoPage()
        self.log.info("CUrrently on the Billing Info Page")
        self.log.info("Billing Address Generated")
        self.obj_HoRates.tests_ValidDetailsOnRatesPage()
        self.log.info("Currently on the Rates page")
        self.log.info("The Policy has been Saved and Exited")











