from Pages_LOB.HoFullQuote.HoFullQuoteUWQuestPage import HoUWQUestPage
from Tests.testData import TestData as TD
from TestResults.customLogger import customLogger
import logging

class tests_HoFQCoveragePage():

    def __init__(self,driver):
        self.log = customLogger(logging.INFO)
        self.obj_HoFullQuoteUWQuestPage = HoUWQUestPage(driver)


    def tests_ValidDetailsOnUWQuest(self):
        self.log.info('Started Filling The Ho Full Quote by using :: Method fillDetailsForHoFullQuote ')
        self.obj_HoFullQuoteUWQuestPage.uwquestQuestions(years=TD.applicantKnown)

