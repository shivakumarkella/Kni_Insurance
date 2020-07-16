


Loginpage = {"URL":{"URL":"http://10.1.1.18:88/login.max?preprocess=true#"},
            "UserName":{"Name":"UserName"},
            "Password":{"Name":"password"},
            "LoginButton":{"Name":"submit"},
            "HOFullQuoteLink":{"Xpath":"//table[@class='TableMenu']//a[contains(text(),'Full Quote - HO')]"},
            "SpinnerOverlay":{"id":"spinnerOverlay"},
            "InvalidUsername":{"Xpath":"//div[contains(text(),'Invalid Login - Your user account will be locked o')]"},
            "InvalidLogin":{"Xpath": "//div[contains(text(),'Invalid Login Please try again.')]"}
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


# HoFullQuoteCreditPage = {"SpinnerOverlay":{"id":"spinnerOverlay"},
#                           "HOCreditContinue":{"id":"Continue"}}
#
#
# HoFullQuoteAddinformation = {"SpinnerOverlay":{"id":"spinnerOverlay"},
#                              "HOYearsAtCurrentAddress":{"id":"hPQ_yrscurrentaddress"},
#                              "HOFirstTimeHomeBuyer":{"id":"hPQ_NewPurchase"},
#                              "HOAddinfoContinueButton":{"id":"btnContinue"}}
#
#
# HoFullQuoteLosses ={"SpinnerOverlay":{"id":"spinnerOverlay"},
#                     "HOConstructionClase":{"xpath":"//select[@id='hCTC_ConstructionType']//option[2]"},
#                     "HONumberOfFamilies":{"xpath":"//select[@id='hPQL_NumOfFamilies']//option[1]"},
#                     "HOUsage":{"xpath":"//select[@id='hPQL_Usage']//option[2]"},
#                     "HOLossesContinueButton":{"id":"Continue"}}







