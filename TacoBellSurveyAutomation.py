from selenium import webdriver
import time
import random
import sys

def NextButton():
    NextButton = driver.find_element_by_xpath('//*[@id="NextButton"]')
    NextButton.click()

driver = webdriver.Chrome()

# Check For Chrome/Driver Mismatch: Must be on newest Chrome!
try:
    driver.get('https://www.tellthebell.com/')

    # Finds Entry Box and starts typing
    SixteenDigitCode = input("Please enter the 16 digit code from your survey: ")
    CashierName = input("Please enter the name listed team member: ")

    if(CashierName.isalpha() == False):
       print("Error: Name Contains Numbers/Symbols")
       time.sleep(15)
       quit()

    if(CashierName == ""):
        CashierName = "The Manager"

    SurveyCode = driver.find_element_by_xpath('//*[@id="CN1"]')
    SurveyCode.send_keys(SixteenDigitCode)

    # Find Start Button and Clicks
    StartButton = driver.find_element_by_xpath('//*[@id="NextButton"]')
    StartButton.click()

    # Screen 1 - Overall Satisfaction
    HighSatisfy = driver.find_element_by_xpath('//*[@id="FNSR001000"]/td[2]/span')
    HighSatisfy.click()
    NextButton()

    # Screen 2 - Rate Satisfication Big Chunk Completely Random Order
    try:
        SpeedService = driver.find_element_by_xpath('//*[@id="FNSR012000"]/td[2]/span')
        SpeedService.click()
    except:
        print("Option Not Present; Skipped")

    try:
        HealthSafety = driver.find_element_by_xpath('//*[@id="FNSR000121"]/td[2]/span')
        HealthSafety.click()
    except:
        print("Option Not Present; Skipped")

    try:
        FriendlyTeam = driver.find_element_by_xpath('//*[@id="FNSR010000"]/td[2]/span')
        FriendlyTeam.click()
    except:
        print("Option Not Present; Skipped")

    try:
        Accuracy = driver.find_element_by_xpath('//*[@id="FNSR008000"]/td[2]/span')
        Accuracy.click()
    except:
        print("Option Not Present; Skipped")

    try:
        Appearance = driver.find_element_by_xpath('//*[@id="FNSR011000"]/td[2]/span')
        Appearance.click()
    except:
        print("Option Not Present; Skipped")

    try:
        Exterior = driver.find_element_by_xpath('//*[@id="FNSR014000"]/td[2]/span')
        Exterior.click()
    except:
        print("Option Not Present; Skipped")

    try:
        PortionSize = driver.find_element_by_xpath('//*[@id="FNSR007000"]/td[2]/span')
        PortionSize.click()
    except:
        print("Option Not Present; Skipped")

    try:
        Taste = driver.find_element_by_xpath('//*[@id="FNSR005000"]/td[2]/span')
        Taste.click()
    except:
            print("Option Not Present; Skipped")

    NextButton()

    # Screen 3 - Problem In Visit
    Problem = driver.find_element_by_xpath('//*[@id="FNSR024000"]/td[3]/span')
    Problem.click()
    NextButton()

    # Screen 4 - You said You were highly satisfied
    # Pick a Stock Response
    FinalResponse = ""
    StockResponse0 = "Food was amazing and the speed was incredible!"
    StockResponse1 = "Food tasted good."
    StockResponse2 = "Did not run into a single shortcoming!"
    choice = random.randint(0,2)

    if (choice == 0):
        FinalResponse = StockResponse0
    elif (choice == 1):
        FinalResponse = StockResponse1
    else:
        FinalResponse = StockResponse2

    TextBox1 = driver.find_element_by_xpath('//*[@id="S081000"]')
    TextBox1.send_keys(FinalResponse)
    NextButton()

    # Screen 4 - Reconize Team Member? Yes
    ReconizeMember = driver.find_element_by_xpath('//*[@id="FNSR030000"]/td[2]/span')
    ReconizeMember.click()
    NextButton()

    # Screen 5 - Name Drop Time
    # Team Member Name
    TeamMemberName = driver.find_element_by_xpath('//*[@id="S081001"]')
    TeamMemberName.send_keys(CashierName)

    # Team Member Extended Response
    FinalResponse = ""
    StockResponse0 = " did an excellent job taking care of myself and other customers in the line. Exceptional work!"
    StockResponse1 = " was super friendly and personal at the window!"
    StockResponse2 = " is an amazing worker! Do whatever you can to keep them."
    choice = random.randint(0,2)

    if (choice == 0):
        FinalResponse = CashierName + StockResponse0
    elif (choice == 1):
        FinalResponse = CashierName + StockResponse1
    else:
        FinalResponse = CashierName + StockResponse2

    TeamMemberDescription = driver.find_element_by_xpath('//*[@id="S081002"]')
    TeamMemberDescription.send_keys(FinalResponse)
    NextButton()

    # Screen 6 - Hard or Soft Shell?
    HardSoft = driver.find_element_by_xpath('//*[@id="FNSR031000"]/td[3]/span')
    HardSoft.click()
    NextButton()

    # Screen 7 - Health Safety Extended Response
    HealthySafetyER = driver.find_element_by_xpath('//*[@id="S000124"]')
    FillResponse2 = CashierName + " made me feel safe. All interactions followed strict guidelines regarding saftey!"
    HealthySafetyER.send_keys(FillResponse2)
    NextButton()

    # Screen 8 - Enter Sweepstakes?
    Sweepstakes = driver.find_element_by_xpath('//*[@id="FNSR046000"]/td[3]/span')
    Sweepstakes.click()

    # Final Submission
    NextButton()
    sys.exit()
except:
    # Should Work
    print("Error: Chrome and WebDriver Version Desync")
    print("Solution: Check for updates inside Google Chrome")
