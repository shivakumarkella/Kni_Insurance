from Pages_LOB.Locators import ApplicationLocators
from SeleniumActions import Actions



class HoFullQuotePropertyPage():

    #Locators

    Locator = ApplicationLocators.HoFullQuoteProperty
    HoOccupancy_locator=list(Locator['HoOccupancy'].items())[0][1]
    HoOccupancy_locatorType= list(Locator['HoOccupancy'].items())[0][0]
    HODistanceFromFireHydrant_locator = list(Locator['HoDistancfromFireHydrant'].items())[0][1]
    HODistanceFromFireHydrant_locatorType = list(Locator['HoDistancfromFireHydrant'].items())[0][0]
    HOVisibletoNeighbours_locator = list(Locator['HoVisibletoNeighbours'].items())[0][1]
    HOVisibletoNeighbours_locatorType = list(Locator['HoVisibletoNeighbours'].items())[0][0]
    HOPrimaryHeatSource_locator = list(Locator['HoPrimaryHeatSource'].items())[0][1]
    HOPrimaryHeatSource_locatorType = list(Locator['HoPrimaryHeatSource'].items())[0][0]
    HOFuelType_locator = list(Locator['HoFuelType'].items())[0][1]
    HOFuelType_locatorType = list(Locator['HoFuelType'].items())[0][0]
    HOAlternatingHeatSource_locator = list(Locator['HoAlternatingHeatSource'].items())[0][1]
    HOAlternatingHeatSource_locatorType = list(Locator['HoAlternatingHeatSource'].items())[0][0]
    HOSwimmingpool_locator = list(Locator['HoSwimmingPool'].items())[0][1]
    HOSwimmingpool_locatorType = list(Locator['HoSwimmingPool'].items())[0][0]
    HOPropertyContinue_locator = list(Locator['HoPropertyContinueButton'].items())[0][1]
    HOPropertyContinue_locatorType = list(Locator['HoPropertyContinueButton'].items())[0][0]
    HOPropertypinner_locator = list(Locator['SpinnerOverlay'].items())[0][1]
    HOPropertypinner_locatorType = list(Locator['SpinnerOverlay'].items())[0][0]



    def __init__(self, driver):
        self.driver = driver
        self.obj_SeleniumActions = Actions.SeleniumActions(self.driver)


    def occupancy(self,selectvalue):
        self.obj_SeleniumActions.selectDropdown(locator=self.HoOccupancy_locator,
                                                locatorType= self.HoOccupancy_locatorType, SelectValue=selectvalue)

    def distancefromFireHydrant(self,distance):
        self.obj_SeleniumActions.sendKeys(locator=self.HODistanceFromFireHydrant_locator,
                                          locatortype=self.HODistanceFromFireHydrant_locatorType, message=distance)

    def visibleToNeighbours(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HOVisibletoNeighbours_locator,
                                                   locatorType=self.HOVisibletoNeighbours_locatorType)

    def primaryHeatSource(self, selectvalue):
        self.obj_SeleniumActions.selectDropdown(locator=self.HOPrimaryHeatSource_locator,
                                                locatorType=self.HOPrimaryHeatSource_locatorType, SelectValue=selectvalue)

    def fuelType(self, selectvalue):
        self.obj_SeleniumActions.selectDropdown(locator=self.HOFuelType_locator,
                                                locatorType=self.HOFuelType_locatorType, SelectValue=selectvalue)

    def alternatingHeatSource(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HOAlternatingHeatSource_locator,
                                                   locatorType=self.HOAlternatingHeatSource_locatorType)

    def swimmingPool(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HOSwimmingpool_locator,
                                                   locatorType=self.HOSwimmingpool_locatorType)

    def propertyContinueButton(self):
        self.obj_SeleniumActions.clickmethod(locator=self.HOPropertyContinue_locator,
                                             locatorType=self.HOPropertyContinue_locatorType)

    def completeStingraySpinning(self):
        self.obj_SeleniumActions.waitForElementToDisappear(timeout=15,locator=self.HOPropertypinner_locator,
                                                            locatorType=self.HOPropertypinner_locatorType)

    def filldetailsforPropertypage(self,valueforOccupancy,distancefromfoire,primaryHeatingSource,fuelType):

        self.completeStingraySpinning()
        self.occupancy(valueforOccupancy)
        self.distancefromFireHydrant(distancefromfoire)
        self.visibleToNeighbours()
        self.primaryHeatSource(primaryHeatingSource)
        self.fuelType(fuelType)
        self.alternatingHeatSource()
        self.swimmingPool()
        self.propertyContinueButton()
        self.completeStingraySpinning()
        # self.obj_SeleniumActions.sleepForWhile(5)

