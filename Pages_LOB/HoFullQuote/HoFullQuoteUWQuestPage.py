from Pages_LOB.Locators import ApplicationLocators
from SeleniumActions import Actions


class HoUWQUestPage():

    # Locators
    Locator = ApplicationLocators.HoFullQuoteUWQuest
    HOApplicantKnow_locator = list(Locator['HoApplicantKnown'].items())[0][1]
    HOApplicantKnow_locatorType = list(Locator['HoApplicantKnown'].items())[0][0]
    HORadioButton1_locator = list(Locator['HoHaveyouinspectedtheproperty'].items())[0][1]
    HORadioButton1_locatorType = list(Locator['HoHaveyouinspectedtheproperty'].items())[0][0]
    HORadioButton2_locator = list(Locator['HoIsthisrisknewtoyouragency'].items())[0][1]
    HORadioButton2_locatorType = list(Locator['HoIsthisrisknewtoyouragency'].items())[0][0]
    HORadioButton3_locator = list(Locator['HoAnyfarmingorotherbusinessconductedonpremises'].items())[0][1]
    HORadioButton3_locatorType = list(Locator['HoAnyfarmingorotherbusinessconductedonpremises'].items())[0][0]
    HORadioButton4_locator = list(Locator['HoAnyFloodingBrushForestFirehazardslandslideetc'].items())[0][1]
    HORadioButton4_locatorType = list(Locator['HoAnyFloodingBrushForestFirehazardslandslideetc'].items())[0][0]
    HORadioButton5_locator = list(Locator['HoAnyotherresidenceownedoccupiedorrented'].items())[0][1]
    HORadioButton5_locatorType = list(Locator['HoAnyotherresidenceownedoccupiedorrented'].items())[0][0]
    HORadioButton6_locator = list(Locator['HoHasapplicanteverhadafireloss'].items())[0][1]
    HORadioButton6_locatorType = list(Locator['HoHasapplicanteverhadafireloss'].items())[0][0]
    HORadioButton7_locator = list(Locator['HoHasinsurancebeentransferredwithinagency'].items())[0][1]
    HORadioButton7_locatorType = list(Locator['HoHasinsurancebeentransferredwithinagency'].items())[0][0]
    HORadioButton8_locator = list(Locator['HoAnycoveragedeclined'].items())[0][1]
    HORadioButton8_locatorType = list(Locator['HoAnycoveragedeclined'].items())[0][0]
    HORadioButton9_locator = list(Locator['HoHasapplicanthadaforeclosure'].items())[0][1]
    HORadioButton9_locatorType = list(Locator['HoHasapplicanthadaforeclosure'].items())[0][0]
    HORadioButton10_locator = list(Locator['HoIspropertysituatedonmorethanfiveacres'].items())[0][1]
    HORadioButton10_locatorType = list(Locator['HoIspropertysituatedonmorethanfiveacres'].items())[0][0]
    HORadioButton11_locator = list(Locator['HoDoesapplicantownanyrecreationalvehicles'].items())[0][1]
    HORadioButton11_locatorType = list(Locator['HoDoesapplicantownanyrecreationalvehicles'].items())[0][0]
    HORadioButton12_locator = list(Locator['HoHasanyapplicanteverbeenconvictedofthecrimeofarson'].items())[0][1]
    HORadioButton12_locatorType = list(Locator['HoHasanyapplicanteverbeenconvictedofthecrimeofarson'].items())[0][0]
    HORadioButton13_locator = list(Locator['HoAnyuncorrectedfireorbuildingcodeviolations'].items())[0][1]
    HORadioButton13_locatorType = list(Locator['HoAnyuncorrectedfireorbuildingcodeviolations'].items())[0][0]
    HORadioButton14_locator = list(Locator['HoIsbuildingundergoingrenovationorreconstruction'].items())[0][1]
    HORadioButton14_locatorType = list(Locator['HoIsbuildingundergoingrenovationorreconstruction'].items())[0][0]
    HORadioButton15_locator = list(Locator['HoIshouseforsale'].items())[0][1]
    HORadioButton15_locatorType = list(Locator['HoIshouseforsale'].items())[0][0]
    HORadioButton16_locator = list(Locator['HoIspropertywithin300feetofcommercialproperty'].items())[0][1]
    HORadioButton16_locatorType = list(Locator['HoIspropertywithin300feetofcommercialproperty'].items())[0][0]
    HORadioButton17_locator = list(Locator['HoIsthereatrampolineonthepremises'].items())[0][1]
    HORadioButton17_locatorType = list(Locator['HoIsthereatrampolineonthepremises'].items())[0][0]
    HORadioButton18_locator = list(Locator['HoWasthestructureoriginallybuilt'].items())[0][1]
    HORadioButton18_locatorType = list(Locator['HoWasthestructureoriginallybuilt'].items())[0][0]
    HORadioButton19_locator = list(Locator['HoAnyleadpainthazard'].items())[0][1]
    HORadioButton19_locatorType = list(Locator['HoAnyleadpainthazard'].items())[0][0]
    HORadioButton20_locator = list(Locator['HoAnynon-domesticated'].items())[0][1]
    HORadioButton20_locatorType = list(Locator['HoAnynon-domesticated'].items())[0][0]
    HORadioButton21_locator = list(Locator['HoAnyanimalkeptonpremises'].items())[0][1]
    HORadioButton21_locatorType = list(Locator['HoAnyanimalkeptonpremises'].items())[0][0]
    HORadioButton22_locator = list(Locator['HoDoyouownand/orcarefor'].items())[0][1]
    HORadioButton22_locatorType = list(Locator['HoDoyouownand/orcarefor'].items())[0][0]
    HORadioButton23_locator = list(Locator['HoDoyouboardhorses'].items())[0][1]
    HORadioButton23_locatorType = list(Locator['HoDoyouboardhorses'].items())[0][0]
    HORadioButton24_locator = list(Locator['HoDoyouhaveanyhorsesforpersonaluse'].items())[0][1]
    HORadioButton24_locatorType = list(Locator['HoDoyouhaveanyhorsesforpersonaluse'].items())[0][0]
    HORadioButton25_locator = list(Locator['HoArethenamedinsuredsthesoleownersofthisdwelling'].items())[0][1]
    HORadioButton25_locatorType = list(Locator['HoArethenamedinsuredsthesoleownersofthisdwelling'].items())[0][0]
    HORadioButton26_locator = list(Locator['HoIsthedwellingvacantorunoccupiedformorethan30consecutivedays'].items())[0][1]
    HORadioButton26_locatorType = list(Locator['HoIsthedwellingvacantorunoccupiedformorethan30consecutivedays'].items())[0][0]
    HOUWQuestContinueButton_locator = list(Locator['HoUWQuestContinueButton'].items())[0][1]
    HOUWQuestContinueButton_locatorType = list(Locator['HoUWQuestContinueButton'].items())[0][0]
    HOUWQuestSpinner_locator = list(Locator['SpinnerOverlay'].items())[0][1]
    HOUWQuestSpinner_locatorType = list(Locator['SpinnerOverlay'].items())[0][0]




    def __init__(self,driver):
        self.driver = driver
        self.obj_SeleniumActions = Actions.SeleniumActions(self.driver)


    def applicantKnown(self, years):
        self.obj_SeleniumActions.sendKeys(locator=self.HOApplicantKnow_locator,
                                          locatortype=self.HOApplicantKnow_locatorType, message=years)

    def inspectedProperty(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton1_locator,
                                                   locatorType=self.HORadioButton1_locatorType)

    def riskAgency(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton2_locator,
                                                   locatorType=self.HORadioButton2_locatorType)

    def anyFarming(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton3_locator,
                                                   locatorType=self.HORadioButton3_locatorType)
    def anyFlooding(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton4_locator,
                                                   locatorType=self.HORadioButton4_locatorType)
    def anyOtherResidence(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton5_locator,
                                                   locatorType=self.HORadioButton5_locatorType)

    def hasApplicanthadFireLoss(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton6_locator,
                                                   locatorType=self.HORadioButton6_locatorType)

    def hasInsuranceTransferedWithAgency(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton7_locator,
                                                   locatorType=self.HORadioButton7_locatorType)

    def anyCoverageDeclined(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton8_locator,
                                                   locatorType=self.HORadioButton8_locatorType)

    def hasApplicantHadaForeclosure(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton9_locator,
                                                   locatorType=self.HORadioButton9_locatorType)

    def isPropertysituatedonmorethanfiveacres(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton10_locator,
                                                   locatorType=self.HORadioButton10_locatorType)

    def doesApplicantownanyRecreationalVehicles(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton11_locator,
                                                   locatorType=self.HORadioButton11_locatorType)

    def anyUncorrectedfire(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton12_locator,
                                                   locatorType=self.HORadioButton12_locatorType)

    def isBuildingUndergoingRenovation(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton13_locator,
                                                   locatorType=self.HORadioButton13_locatorType)

    def isHouseforSale(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton14_locator,
                                                   locatorType=self.HORadioButton14_locatorType)

    def isPropertywithin300feet(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton15_locator,
                                                   locatorType=self.HORadioButton15_locatorType)

    def isthereaTrampolineonthePremises(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton16_locator,
                                                   locatorType=self.HORadioButton16_locatorType)

    def WastheStructure (self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton17_locator,
                                                   locatorType=self.HORadioButton17_locatorType)

    def anyLeadpaintHazard(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton18_locator,
                                                   locatorType=self.HORadioButton18_locatorType)

    def anynonDomesticated(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton19_locator,
                                                   locatorType=self.HORadioButton19_locatorType)

    def anyAnimalkept(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton20_locator,
                                                   locatorType=self.HORadioButton20_locatorType)

    def doYouown(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton21_locator,
                                                   locatorType=self.HORadioButton21_locatorType)

    def  doYouboardHorses(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton22_locator,
                                                   locatorType=self.HORadioButton22_locatorType)

    def doyouhaveanyHorsesforPersonaluse(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton23_locator,
                                                   locatorType=self.HORadioButton23_locatorType)

    def soleOwnersofthisDwelling(self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton24_locator,
                                                   locatorType=self.HORadioButton24_locatorType)

    def istheDwellingVacant (self):
        self.obj_SeleniumActions.selectRadiobutton(locator=self.HORadioButton25_locator,
                                                   locatorType=self.HORadioButton25_locatorType)


    def clickOnUWQuestContinueButton(self):
        self.obj_SeleniumActions.clickmethod(locator=self.HOUWQuestContinueButton_locator,
                                                         locatorType=self.HOUWQuestContinueButton_locatorType)

    def completeStingraySpinning(self):
        self.obj_SeleniumActions.waitForElementToDisappear(timeout=5,locator=self.HOUWQuestSpinner_locator,
                                                            locatorType=self.HOUWQuestSpinner_locatorType)



    def uwquestQuestions(self,years):
        self.completeStingraySpinning()
        self.obj_SeleniumActions.sleepForWhile(5)
        self.applicantKnown(years)
        self.inspectedProperty()
        self.riskAgency()
        self.anyFarming()
        self.anyFlooding()
        self.anyOtherResidence()
        self.hasApplicanthadFireLoss()
        self.hasInsuranceTransferedWithAgency()
        self.anyCoverageDeclined()
        self.hasApplicantHadaForeclosure()
        self.isPropertysituatedonmorethanfiveacres()
        self.doesApplicantownanyRecreationalVehicles()
        self.anyUncorrectedfire()
        self.isBuildingUndergoingRenovation()
        self.isHouseforSale()
        self.isPropertywithin300feet()
        self.isthereaTrampolineonthePremises()
        self.WastheStructure()
        self.anyLeadpaintHazard()
        self.anynonDomesticated()
        self.anyAnimalkept()
        self.doYouown()
        self.doYouboardHorses()
        self.doyouhaveanyHorsesforPersonaluse()
        self.soleOwnersofthisDwelling()
        self.istheDwellingVacant()
        self.clickOnUWQuestContinueButton()
        self.completeStingraySpinning()




