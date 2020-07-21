Loginpage = {"URL":{"URL":"http://10.1.1.13:88/login.max?preprocess=true#"},
            "UserName":{"Name":"UserName"},
            "Password":{"Name":"password"},
            "LoginButton":{"Name":"submit"},
            "HOFullQuoteLink":{"Xpath":"//table[@class='TableMenu']//a[contains(text(),'Full Quote - HO')]"},
            "SpinnerOverlay":{"id":"spinnerOverlay"},
            "InvalidUsername":{"Xpath":"//div[contains(text(),'Invalid Login - Your user account will be locked o')]"},
            "InvalidLogin":{"Xpath": "//div[contains(text(),'Invalid Login Please try again.')]"},
            "LoginDiv":{"Xpath": "//table[@class='Login']"}
             }



HoFullQuote = {"Days60PopUpButton":{"id":"popup_ok"},
                "HOFullQuoteLink":{"xpath":"//table[@class='TableMenu']//a[contains(text(),'Full Quote - HO')]"},
                "HOSelectAgency":{"id":"hPQ_Agency"},
                "HOGender":{"id":"hPQ_Gender1"},
                "HONA":{"xpath":"//div[@id='rightColumn']//div//div[9]//input[1]"},
                "HOFirstName":{"id":"hPQ_FirstName"},
                "HOLastName":{"id":"hPQ_LastName"},
                "HOSsn":{"id":"hPQ_SSN"},
                "HODob":{"id":"hPQ_DOB1"},
                "HOEmail":{"id":"hPQ_Email"},
                "HOMailingAddress":{"id":"hPQ_AddressSame"},
                "HOOccupiedBy":{"id":"PolicyType"},
                "HOPropertyAddress1":{"id":"hPQ_Address1"},
                "HOPropertyAddress2":{"id":"hPQ_Address2"},
                "HOPropertyCity":{"id":"hPQ_City"},
                "HOState":{"id":"hPQ_State"},
                "HOZip":{"id":"hPQ_Zip"},
                "HOSuggestionBox":{"xpath":"//div[@class='avs-header']"},
                "HOEmptyBox":{"xpath":"//div[6]//a[1]//span[1]"},
                "HOApplicantContinue":{"id":"Continue"},
                "HOAddressSpinnerOverlay":{"id":"spinnerOverlay"},
                "MMInsuredManagement":{"xpath":"//a[contains(text(),'Insured Login Management')]"},
                "HOCounty":{"id":"hPQ_CountyID"}}


HoFullQuoteAcceptAgrement = {"SpinnerOverlay":{"id":"spinnerOverlay"},
                            "HOAcceptAgreementRB":{"xpath":"//div[@class='component DynamicContainer']//div[1]//input[1]"},
                            "HOAcceptAgreementContinueButton":{"id":"Continue"}}


HoFullQuoteCreditPage = {"SpinnerOverlay":{"id":"spinnerOverlay"},
                        "HOCreditContinue":{"id":"Continue"}}



HoFullQuoteAddinformation = {"SpinnerOverlay":{"id":"spinnerOverlay"},
                             "HOYearsAtCurrentAddress":{"id":"hPQ_yrscurrentaddress"},
                             "HOFirstTimeHomeBuyer":{"id":"hPQ_NewPurchase"},
                             "HOAddinfoContinueButton":{"id":"btnContinue"}}



HoFullQuoteLosses ={"SpinnerOverlay":{"id":"spinnerOverlay"},
                    "HOConstructionClase":{"id":"hCTC_ConstructionType"},
                    "HONumberOfFamilies":{"id":"hPQL_NumOfFamilies"},
                    "HOUsage":{"id":"hPQL_Usage"},
                    "HOLossesContinueButton":{"id":"Continue"}}



HoFullQuoteE2Value ={"SpinnerOverlay":{"id":"spinnerOverlay"},
                     "HoCoverageA":{"id":"hEV_coverage_a"},
                     "HoSqftArea":{"id":"hEV_square_footage"},
                     "HoConstructionYear":{"id":"hEV_year_built"},
                     "HoReplacementcosttype":{"id":"hEV_replacement_cost_type"},
                     "HoPropertyLocation":{"id":"sEVL_ID"},
                     "HoDwellingType":{"id":"sEVAT_ID"},
                     "HoConstructionType":{"id":"hEV_CNType"},
                     "HoConstructionQuality":{"id":"sEVCQ_ID"},
                     "HoGeneralCondition":{"id":"hEV_general"},
                     "HoRoofCondition":{"id":"hEV_roof"},
                     "HoDwellingShape":{"id":"sEVPS_ID"},
                     "HoPrimaryExterior":{"id":"sEVPE_ID"},
                     "HoPrimaryRoofCovering":{"id":"hEV_RCType"},
                     "HoWallCondition":{"id":"hEV_wall"},
                     "HoFoundationCondition":{"id":"hEV_foundation"},
                     "HoE2valueContinueButton":{"id":"Continue"}}


HoFullQuoteE2ValueResult ={"SpinnerOverlay":{"id": "spinnerOverlay"},
                               "HoE2valueResultContinueButton":{"id":"Skip"}}



HoFullQuoteCoverages = {"SpinnerOverlay":{"id": "spinnerOverlay"},
                            "HoCoverageE":{"id":"hPQL_CoverageE"},
                            "HoCoverageF":{"id":"hPQL_CoverageF"},
                            "HoPolicyDeductble":{"id":"hPQL_Deductible"},
                            "HoCoveragesContinueButton":{"id":"Continue"}}

HoFullQuoteProperty = {"SpinnerOverlay":{"id": "spinnerOverlay"},
                       "HoOccupancy":{"id":"hPQL_Occupancy"},
                       "HoDistancfromFireHydrant":{"id":"hPQL_FeetFromHydrant"},
                       "HoVisibletoNeighbours":{"id":"hPQL_Visible_To_Neighbors"},
                       "HoPrimaryHeatSource":{"id":"hPQL_Heating_type"},
                       "HoFuelType":{"id":"hPQL_Fuel_Type"},
                       "HoAlternatingHeatSource":{"xpath":"//div[7]//div[3]//div[3]//input[1]"},
                       "HoSwimmingPool":{"xpath":"//div[@id='rightColumn']//div[1]//div[3]//input[1]"},
                       "HoPropertyContinueButton":{"id":"Continue"}}


HoFullQuoteUWQuest ={"SpinnerOverlay":{"id": "spinnerOverlay"},
                     "HoApplicantKnown":{"id":"EDIT244_KnowApplicant"},
                     "HoHaveyouinspectedtheproperty":{"xpath":"//tr[@id='RowInspectedProperty']//td[3]//div[1]//input[1]"},
                     "HoIsthisrisknewtoyouragency":{"xpath":"//tr[@id='RowNewRisk']//td[4]//div[1]//input[1]"},
                     "HoAnyfarmingorotherbusinessconductedonpremises":{"xpath":"//tr[@id='RowHomeBusiness']//td[4]//div[1]//input[1]"},
                     "HoAnyFloodingBrushForestFirehazardslandslideetc":{"xpath":"//tr[@id='RowDisasters']//td[4]//div[1]//input[1]"},
                     "HoAnyotherresidenceownedoccupiedorrented":{"xpath":"//tr[@id='RowOtherOwned']//td[4]//div[1]//input[1]"},
                     "HoHasapplicanteverhadafireloss":{"xpath":"//tr[@id='RowFireLoss5000']//td[4]//div[1]//input[1]"},
                     "HoHasinsurancebeentransferredwithinagency":{"xpath":"//tr[@id='RowTransferWithin']//td[4]//div[1]//input[1]"},
                     "HoAnycoveragedeclined":{"xpath":"//tr[@id='RowCovDeclined']//td[4]//div[1]//input[1]"},
                     "HoHasapplicanthadaforeclosure":{"xpath":"//tr[@id='RowForeclosed']//td[4]//div[1]//input[1]"},
                     "HoIspropertysituatedonmorethanfiveacres":{"xpath":"//tr[@id='RowMore5Acres']//td[4]//div[1]//input[1]"},
                     "HoDoesapplicantownanyrecreationalvehicles":{"xpath":"//tr[@id='RowOwnRVs']//td[4]//div[1]//input[1]"},
                     "HoHasanyapplicanteverbeenconvictedofthecrimeofarson":{"xpath":"//tr[@id='RowArsonConviction']//td[4]//div[1]//input[1]"},
                     "HoAnyuncorrectedfireorbuildingcodeviolations":{"xpath":"//tr[@id='RowFireCode']//td[4]//div[1]//input[1]"},
                     "HoIsbuildingundergoingrenovationorreconstruction":{"xpath":"//tr[@id='RowRenovation']//td[4]//div[1]//input[1]"},
                     "HoIshouseforsale":{"xpath":"//tr[@id='RowForSaleCurrently']//td[4]//div[1]//input[1]"},
                     "HoIspropertywithin300feetofcommercialproperty":{"xpath":"//tr[@id='RowCommercialProp']//td[4]//div[1]//input[1]"},
                     "HoIsthereatrampolineonthepremises":{"xpath":"//tr[@id='RowTrampoline']//td[4]//div[1]//input[1]"},
                     "HoWasthestructureoriginallybuilt":{"xpath":"//tr[@id='RowConverted']//td[4]//div[1]//input[1]"},
                     "HoAnyleadpainthazard":{"xpath":"//tr[@id='RowLeadPaint']//td[4]//div[1]//input[1]"},
                     "HoAnynon-domesticated":{"xpath":"//tr[@id='Rowwildanimal']//td[4]//div[1]//input[1]"},
                     "HoAnyanimalkeptonpremises":{"xpath":"//tr[@id='Rowanimalbite']//td[4]//div[1]//input[1]"},
                     "HoDoyouownand/orcarefor":{"xpath":"//tr[@id='Rowdogbreeds']//td[4]//div[1]//input[1]"},
                     "HoDoyouboardhorses":{"xpath":"//tr[@id='Rowboardhorses']//td[4]//div[1]//input[1]"},
                     "HoDoyouhaveanyhorsesforpersonaluse":{"xpath":"//tr[@id='Rowpersonalhorses']//td[4]//div[1]//input[1]"},
                     "HoArethenamedinsuredsthesoleownersofthisdwelling":{"xpath":"//tr[@id='Rowsoleowners']//td[3]//div[1]//input[1]"},
                     "HoIsthedwellingvacantorunoccupiedformorethan30consecutivedays":{"xpath":"/html[1]/body[1]/div[1]/div[6]/div[1]/div[7]/div[1]/table[1]/tbody[1]/tr[30]/td[4]/div[1]/input[1]"},
                     "HoUWQuestContinueButton":{"id":"Continue"}}


HoClueResults = {"SpinnerOverlay":{"id": "spinnerOverlay"},
                 "HoProgressBar":{"xpath":"//label[@class='Default']//img"},
                 "HoClueResultContinueButton":{"id":"Continue"},
                 "HoClueResultUncheck":{"xpath":"//input[@type='checkbox']"},
                 "HoClueResultFullRight":{"css":"div.right.column.component.EditableContent:nth-child(1) div.component.DynamicContainer:nth-child(3) div.component.EditorLabel div.TableMasterWrapper:nth-child(2) div.sBase > div.sData"}}

HoEndorsementPage = {"SpinnerOverlay":{"id": "spinnerOverlay"},
                    "HoEndorsmentContinueButton":{"xpath":"//input[@id='continue']"}}

HoAddBillingInfoPage = {"SpinnerOverlay":{"id": "spinnerOverlay"},
                        "HoInvoice":{"xpath":"/html[1]/body[1]/div[1]/div[6]/div[1]/div[7]/div[2]/select[1]/option[2]"},
                        "HoRenewalInvoice":{"xpath":"/html[1]/body[1]/div[1]/div[6]/div[1]/div[7]/div[4]/select[1]/option[2]"},
                        "HoBillingInfoContinueButton":{"id":"Continue"}}

HoFullQuoteRatesPage = {"SpinnerOverlay":{"id": "spinnerOverlay"},
                        "HoPaymentPlan":{"xpath":"//div[@id='paymentOptions_Div']//div[3]//input[1]"},
                        "HoAnnualPlanPayment":{"xpath":"//span[@id='nonEFTPayplan']//tr[2]//td[1]//div[1]//input[1]"},
                        "HoRatesSaveAndExitButton":{"id":"Save"}}





























