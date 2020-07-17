from Pages_LOB.Locators import ApplicationLocators
from SeleniumActions import Actions



class HoFullQuoteE2ValuePage():

    #Locators
    Locator = ApplicationLocators.HoFullQuoteE2Value
    HoCoverageA_locator=list(Locator['HoCoverageA'].items())[0][1]
    HoCoverageA_locatorType= list(Locator['HoCoverageA'].items())[0][0]
    HosqftArea_locator = list(Locator['HoSqftArea'].items())[0][1]
    HosqftArea_locatorType = list(Locator['HoSqftArea'].items())[0][0]
    HoConstructionYear_locator = list(Locator['HoConstructionYear'].items())[0][1]
    HoConstructionYear_locatorType = list(Locator['HoConstructionYear'].items())[0][0]
    HoReplacementcosttype_locator = list(Locator['HoReplacementcosttype'].items())[0][1]
    HoReplacementcosttype_locatorType = list(Locator['HoReplacementcosttype'].items())[0][0]
    HoPropertyLocation_locator = list(Locator['HoPropertyLocation'].items())[0][1]
    HoPropertyLocation_locatorType = list(Locator['HoPropertyLocation'].items())[0][0]
    HoDwellingType_locator = list(Locator['HoDwellingType'].items())[0][1]
    HoDwellingType_locatorType = list(Locator['HoDwellingType'].items())[0][0]
    HoConstructionType_locator = list(Locator['HoConstructionType'].items())[0][1]
    HoConstructionType_locatorType = list(Locator['HoConstructionType'].items())[0][0]
    HoConstructionQuality_locator = list(Locator['HoConstructionQuality'].items())[0][1]
    HoConstructionQuality_locatorType = list(Locator['HoConstructionQuality'].items())[0][0]
    HoGeneralCondition_locator = list(Locator['HoGeneralCondition'].items())[0][1]
    HoGeneralCondition_locatorType = list(Locator['HoGeneralCondition'].items())[0][0]
    HoRoofCond_locator = list(Locator['HoRoofCondition'].items())[0][1]
    HoRoofCond_locatorType = list(Locator['HoRoofCondition'].items())[0][0]
    HoDwellingshape_locator = list(Locator['HoDwellingShape'].items())[0][1]
    HoDwellingshape_locatorType = list(Locator['HoDwellingShape'].items())[0][0]
    HoPrimaryExt_locator = list(Locator['HoPrimaryExterior'].items())[0][1]
    HoPrimaryExt_locatorType = list(Locator['HoPrimaryExterior'].items())[0][0]
    HoPriRoofCov_locator = list(Locator['HoPrimaryRoofCovering'].items())[0][1]
    HoPriRoofCov_locatorType = list(Locator['HoPrimaryRoofCovering'].items())[0][0]
    HoWallCond_locator = list(Locator['HoWallCondition'].items())[0][1]
    HoWallCond_locatorType = list(Locator['HoWallCondition'].items())[0][0]
    HoFoundationCond_locator = list(Locator['HoFoundationCondition'].items())[0][1]
    HoFoundationCond_locatorType = list(Locator['HoFoundationCondition'].items())[0][0]
    HoE2Continue_locator = list(Locator['HoE2valueContinueButton'].items())[0][1]
    HoE2Continue_locatorType = list(Locator['HoE2valueContinueButton'].items())[0][0]
    HOE2valuespinner_locator = list(Locator['SpinnerOverlay'].items())[0][1]
    HOE2valuespinner_locatorType = list(Locator['SpinnerOverlay'].items())[0][0]

    def __init__(self,driver):
        self.driver = driver
        self.obj_SeleniumActions = Actions.SeleniumActions(self.driver)



    def completeStingraySpinning(self):
        self.obj_SeleniumActions.waitForElementToDisappear(locator=self.HOE2valuespinner_locator,
                                                            locatorType=self.HOE2valuespinner_locatorType)


    def coverageAvalue(self,coverageAvalue):
        self.obj_SeleniumActions.sendKeys(locator=self.HoCoverageA_locator,
                                          locatortype=self.HoCoverageA_locatorType, message=coverageAvalue)

    def sqftLivingArea(self,livingArea):
        self.obj_SeleniumActions.sendKeys(locator=self.HosqftArea_locator,
                                          locatortype=self.HosqftArea_locatorType, message=livingArea)

    def constructionYear(self,ConstructionYear):
        self.obj_SeleniumActions.sendKeys(locator=self.HoConstructionYear_locator,
                                          locatortype=self.HoConstructionYear_locatorType, message=ConstructionYear)

    def replacementCost(self, selectvalue):
       self.obj_SeleniumActions.selectDropdown(locator=self.HoReplacementcosttype_locator,
                                                locatorType=self.HoReplacementcosttype_locatorType,SelectValue=selectvalue)

    def propertyLocation(self, selectvalue):
       self.obj_SeleniumActions.selectDropdown(locator=self.HoPropertyLocation_locator,
                                                locatorType=self.HoPropertyLocation_locatorType,SelectValue=selectvalue)

    def dwellingType(self,selectvalue):
       self.obj_SeleniumActions.selectDropdown(locator=self.HoDwellingType_locator,
                                                locatorType=self.HoDwellingType_locatorType,SelectValue=selectvalue)


    def constructionType(self,selectvalue):
       self.obj_SeleniumActions.selectDropdown(locator=self.HoConstructionType_locator,
                                                locatorType=self.HoConstructionType_locatorType,SelectValue=selectvalue)

    def constructionQuality(self,selectvalue):
       self.obj_SeleniumActions.selectDropdown(locator=self.HoConstructionQuality_locator,
                                                locatorType=self.HoConstructionQuality_locatorType,SelectValue=selectvalue)


    def generalCondition(self,selectvalue):
       self.obj_SeleniumActions.selectDropdown(locator=self.HoGeneralCondition_locator,
                                                locatorType=self.HoGeneralCondition_locatorType,SelectValue=selectvalue)


    def roofCondition(self,selectvalue):
       self.obj_SeleniumActions.selectDropdown(locator=self.HoRoofCond_locator,
                                                locatorType=self.HoRoofCond_locatorType,SelectValue=selectvalue)


    def dwellingShape(self,selectvalue):
       self.obj_SeleniumActions.selectDropdown(locator=self.HoDwellingshape_locator,
                                                locatorType=self.HoDwellingshape_locatorType,SelectValue=selectvalue)


    def primaryExterior(self,selectvalue):
       self.obj_SeleniumActions.selectDropdown(locator=self.HoPrimaryExt_locator,
                                                locatorType=self.HoPrimaryExt_locatorType,SelectValue=selectvalue)


    def primaryRoofCovring(self,selectvalue):
       self.obj_SeleniumActions.selectDropdown(locator=self.HoPriRoofCov_locator,
                                                locatorType=self.HoPriRoofCov_locatorType,SelectValue=selectvalue)

    def wallCondition(self,selectvalue):
       self.obj_SeleniumActions.selectDropdown(locator=self.HoWallCond_locator,
                                                locatorType=self.HoWallCond_locatorType,SelectValue=selectvalue)


    def foundationCondition(self,selectvalue):
       self.obj_SeleniumActions.selectDropdown(locator=self.HoFoundationCond_locator,
                                                locatorType=self.HoFoundationCond_locatorType,SelectValue=selectvalue)


    def e2ValueContinueButton(self):
       self.obj_SeleniumActions.clickmethod(locator=self.HoE2Continue_locator,
                                                locatorType=self.HoE2Continue_locatorType)


    def filldetailsforE2value(self,coverageAvalue,livingArea,ConstructionYear,selectreplacementcost,selectpropertyLocation,selectdwellingtype,selectconstructiontype,
                              selectconstructionquality,selectgeneralCondition,selectroofcondition,selectdwellingshape,selectprimaryExterior,selectprimaryroof,
                              selectwallcondition,selectfoundationcondition):

        self.obj_SeleniumActions.LoadtheDomCompletely()
        self.completeStingraySpinning()
        self.coverageAvalue(coverageAvalue)
        self.sqftLivingArea(livingArea)
        self.constructionYear(ConstructionYear)
        self.replacementCost(selectreplacementcost)
        self.propertyLocation(selectpropertyLocation)
        self.dwellingType(selectdwellingtype)
        self.constructionType(selectconstructiontype)
        self.constructionQuality(selectconstructionquality)
        self.generalCondition(selectgeneralCondition)
        self.roofCondition(selectroofcondition)
        self.dwellingShape(selectdwellingshape)
        self.primaryExterior(selectprimaryExterior)
        self.primaryRoofCovring(selectprimaryroof)
        self.wallCondition(selectwallcondition)
        self.foundationCondition(selectfoundationcondition)
        self.e2ValueContinueButton()
