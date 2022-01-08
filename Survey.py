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

    # Minimizes the window for CMD input
    driver.minimize_window()

    # Finds Entry Box and starts typing
    SixteenDigitCode = input("Please enter the 16 digit code from your survey: ")
    CashierName = input("Please enter the name listed team member: ")
    
    #For Dev
    #SixteenDigitCode = "8041903919073402"
    #CashierName = "Alexis"

    # Minimizes the window for easy of use
    driver.maximize_window()

    # Checks if code is valid and is all numbers
    if (int(SixteenDigitCode) < 1000000000000000 or SixteenDigitCode.isdigit() == False):
        print("Error: Code Invalid or Contains Non-Numeric Values")
        time.sleep(15)
        sys.exit()

    # If the name includes non-letter characters it fails
    # Thus, spaces/more than one name ruins the fun
    if(CashierName.isalpha() == False):
       print("Error: Name Contains Numbers/Spaces/Symbols")
       time.sleep(15)
       sys.exit()

    # If no name given it autofills with the manager
    if(CashierName == ""):
        CashierName = "The Manager"

    SurveyCode = driver.find_element_by_xpath('//*[@id="CN1"]')
    SurveyCode.send_keys(SixteenDigitCode)

    # Find Start Button and Clicks
    StartButton = driver.find_element_by_xpath('//*[@id="NextButton"]')
    StartButton.click()

    # Screen 1 - Overall Satisfaction
    HighSatisfy = driver.find_element_by_xpath('//*[@id="FNSR001000"]/td[1]/span')
    HighSatisfy.click()

    NextButton()

    # Screen 2 - Rate Satisfication | Big Chunk | Completely Random Order
    try:
        SpeedService = driver.find_element_by_xpath('//*[@id="FNSR012000"]/td[1]/span')
        SpeedService.click()

    except:
        print("Option Not Present; Skipped")

    try:
        HealthSafety = driver.find_element_by_xpath('//*[@id="FNSR000121"]/td[1]/span')
        HealthSafety.click()
    except:
        print("Option Not Present; Skipped")

    try:
        FriendlyTeam = driver.find_element_by_xpath('//*[@id="FNSR010000"]/td[1]/span')
        FriendlyTeam.click()
    except:
        print("Option Not Present; Skipped")

    try:
        Accuracy = driver.find_element_by_xpath('//*[@id="FNSR008000"]/td[1]/span')
        Accuracy.click()
    except:
        print("Option Not Present; Skipped")

    try:
        Appearance = driver.find_element_by_xpath('//*[@id="FNSR011000"]/td[1]/span')
        Appearance.click()
    except:
        print("Option Not Present; Skipped")

    try:
        Exterior = driver.find_element_by_xpath('//*[@id="FNSR014000"]/td[1]/span')
        Exterior.click()
    except:
        print("Option Not Present; Skipped")

    try:
        PortionSize = driver.find_element_by_xpath('//*[@id="FNSR007000"]/td[1]/span')
        PortionSize.click()
    except:
        print("Option Not Present; Skipped")

    try:
        Taste = driver.find_element_by_xpath('//*[@id="FNSR005000"]/td[1]/span')
        Taste.click()
    except:
            print("Option Not Present; Skipped")

    NextButton()

    # Screen 3 - Problem In Visit (No)
    Problem = driver.find_element_by_xpath('//*[@id="FNSR024000"]/td[2]/span')
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
    print(FinalResponse)

    TextBox1 = driver.find_element_by_xpath('//*[@id="S081000"]')
    TextBox1.click()
    TextBox1.send_keys(FinalResponse)

    NextButton()

    # Screen 4 - Reconize Team Member? Yes
    ReconizeMember = driver.find_element_by_xpath('//*[@id="FNSR030000"]/td[1]/span')
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
    HardShell = driver.find_element_by_xpath('//*[@id="FNSR031000"]/td[2]/span')
    HardShell.click()
    CrispyChickenTaco = driver.find_element_by_xpath('//*[@id="FNSR000127"]/td[2]/span')
    CrispyChickenTaco.click()

    NextButton()

    # Screen 7 - Health Safety Extended Response
    HealthySafetyER = driver.find_element_by_xpath('//*[@id="S000124"]')
    FillResponse2 = CashierName + " made me feel safe. All interactions followed decent guidelines regarding saftey!"
    HealthySafetyER.send_keys(FillResponse2)
    NextButton()

    # Screen 8 - Enter Sweepstakes? (No)
    Sweepstakes = driver.find_element_by_xpath('//*[@id="FNSR046000"]/td[2]/span')
    Sweepstakes.click()

    # Final Submission
    NextButton()
    
except:
    # Should Work
    print("Error: Chrome and WebDriver Version Desync")
    print("Solution: The Earliest Error Code Points to the Solution")

# Let User See Completion Screen
time.sleep(5)
driver.quit()