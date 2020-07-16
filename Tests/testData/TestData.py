import pandas
import datetime as dt

excelRowNumber=115
rowNumber=excelRowNumber-1
dataRow=rowNumber-1

path='D:\\sharath Data\\HO_UserData.xlsx'
data=pandas.read_excel(path, sheet_name='APLUS Claims Data',nrows=rowNumber, usecols=['LAST NAME', 'FIRST NAME','INSURED SSN',
                                                                                      'INSURED DOB','INSURED GENDER',
                                                                                      'STREET NUMBER','STREET NAME','STREET TYPE',
                                                                                      'APT NUMBER','CITY','STATE','ZIP CODE',
                                                                                      'POLICY TYPE','POLICY NUMBER','ACCOUNT NUMBER','LOSS/ACCIDENT DATE',
                                                                                      'CLAIM AMOUNT','CLAIM TYPE','CASE FILE NUMBER/CLAIM #',
                                                                                      'STATUS','UPDATE FLAG','AM BEST NUMBER'
                                                                                      ])
data=data.to_dict(orient='records')
LastName=list(data[dataRow].items())[0][1]
FirstName = list(data[dataRow].items())[1][1]
SSN = int(list(data[dataRow].items())[2][1])
# DOB= dt.datetime.strptime(str(int(list(data[dataRow].items())[3][1])),'%m%d%Y').date()
selectgender = list(data[dataRow].items())[4][1]

StreetNumber = list(data[dataRow].items())[5][1]
StreetName = list(data[dataRow].items())[6][1]
StreetBluff = list(data[dataRow].items())[7][1]
propertyAddress1=str(StreetNumber)+' '+str(StreetName)+' '+str(StreetBluff)

# NumberaApt = list(data[dataRow].items())[8][1]
# if str(NumberaApt)=='nan':
#     aptNumber=' '
# else:
#     aptNumber=NumberaApt


propertyCity = list(data[dataRow].items())[9][1]
propertyState = list(data[dataRow].items())[10][1]
# propertyZip = list(data[dataRow].items())[11][1]
policyType = list(data[dataRow].items())[12][1]
policyNumber = list(data[dataRow].items())[13][1]
accountNumber = list(data[dataRow].items())[14][1]
lossAccidentdate = dt.datetime.strptime(str(int(list(data[dataRow].items())[15][1])),'%Y%m%d').date()
claimAmount = list(data[dataRow].items())[16][1]
claimType = list(data[dataRow].items())[17][1]
caseFileNumberClaim = list(data[dataRow].items())[18][1]
status = list(data[dataRow].items())[19][1]
updateFlag = list(data[dataRow].items())[20][1]
amBestNumber = list(data[dataRow].items())[21][1]



ValidUsername = "xlsol"
ValidPassword = "1234"
InValidPassword = "8592212983"
InValidUsername = "brxyz"
# FirstName="Test"
# LastName="Test"
# SSN="123321115"
DOB="10/31/1990"
Email="test@test.com"
# propertyAddress1="190 Stump Bluff	Rd"
propertyAddress2="     "
# propertyCity="Bowling Green"
# propertyState="KY"
propertyZip="42102"
YearsAtCurrentAddress ="5"
selectvalueforagency="486"
selectCounty ="67"
# selectvalueforATC = "1"
# selectgender = "M"


location="C:\\Users\\Sharat\\Workspace_python\\Kni_Insurance\\TestResults\\Screenshots"
AutomationFileName = 'automation'
pathToSaveAutomationLog = "TestResults//DocsScreenShotsLogFiles//"


