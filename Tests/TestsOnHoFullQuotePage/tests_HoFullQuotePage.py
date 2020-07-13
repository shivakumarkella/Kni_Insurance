from Pages_LOB.HoFullQuotePage import HoFullQuotePage
from Tests.testData import TestData as TD
import pytest
import unittest
from TestResults.customLogger import customLogger



class tests_HoFullQuotePage(unittest.TestCase):


    def thisclassSetup(self):
        self.log = customLogger()
        self.obj_HoFullQuotePage = HoFullQuotePage(self.driver)


    def testCase1_ValidDetailsOnHoFQ(self):
        self.obj_HoFullQuotePage.fillDetailsForHoFullQuote()
