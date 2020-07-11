import pytest
from Configfile.GetDrivers import GetDriverInstance


class SetupConfig():

    def Getoptions(self,parser):
        parser.addoption("--browser")
