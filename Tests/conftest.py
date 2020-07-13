from Documents.Configfile import GetDrivers
import pytest


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    if browser is None:
        browser='Chrome'
    webDrivers=GetDrivers.GetDriverInstance(browser=browser)
    driver=webDrivers.DriverInstance()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    # driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


