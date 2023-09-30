from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import re
import sys
import time
import random

def NextButton():
    NextButton = driver.find_element(By.XPATH, '//*[@id="NextButton"]')
    NextButton.click()

def DoesItExist(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
        print(xpath + ' Was present on the page!')
    except:
        print(xpath + ' Was present not on the page!')
        return False
    return True

def HighlySatisfiedResponses():
    choice = random.randint(0,5)
    default = "Nothing to complain about"
    switch = {
        1: "Food was amazing and the speed was incredible!",
        2: "Food tasted good.",
        3: "No problems!",
        4: "Food looked and tasted great!",
        5: "The speed of service was higher than expected",
        6: "Food was as ordered"
    }
    return switch.get(choice, default)

def EmployeePraise():
    choice = random.randint(0,7)
    default = " took my order."
    switch = {
        1: " did an excellent job taking care of myself and other customers in the line. Exceptional work!",
        2: " was super friendly and personal at the window!",
        3: " is an amazing worker! Do whatever you can to keep them.",
        4: " and crew provided excellent food.",
        5: " took my order effectively and made no mistakes.",
        6: " made sure to ask if I wanted anything else or sauces.",
        7: " and crew were quick as expected from fast food. Good stuff!"
    }
    return switch.get(choice, default)

def CmdClear():
    # Clears cmd window of random selenium garbage
    os.system('cls' if os.name == 'nt' else 'clear')

driver = webdriver.Chrome()

# Check For Chrome/Driver Mismatch: Must be on newest Chrome!
try:
    # Easy Testing Toggle
    testing = True

    # Get Webpage and let it load
    driver.get('https://www.tellthebell.com/')
    time.sleep(5)

    # Minimizes the window for CMD input
    driver.minimize_window()
    CmdClear()

    # Survey Code Entry
    if(testing == True):
        print("Testing...")
        SixteenDigitCode = "0047903920043023"
        CashierName = " "
    else:
        # Finds Entry Box and starts typing
        SixteenDigitCode = input("Please enter the 16 digit code from your survey: ")
        CashierName = input("Please enter the name listed team member: ")
    
    # Input Validation
    # Accepts Letters and Spaces
    # If no name given it autofills with the manager
    if(CashierName == " " or CashierName == ""):
        CashierName = "The Manager"

    isValidName = bool(re.match('[a-zA-Z\s]+$', CashierName))
    if(isValidName == False):
       print("Error: Name Contains Numbers/Symbols")
       time.sleep(15)
       sys.exit()

    # Checks if Survey code is all numbers
    if (SixteenDigitCode.isdigit() == False):
        print("Error: Survey Code Invalid")
        time.sleep(15)
        sys.exit()

    # Minimizes the window for the user
    driver.maximize_window()

    # Fill in survey code and start
    SurveyCode = driver.find_element(By.XPATH, '//*[@id="CN1"]')
    SurveyCode.send_keys(SixteenDigitCode)
    NextButton()

    # Screen 1 - Overall Satisfaction
    if(DoesItExist('//*[@id="FNSR001000"]/td[1]/span')):
        HighSatisfy = driver.find_element(By.XPATH, '//*[@id="FNSR001000"]/td[1]/span')
        HighSatisfy.click()
        NextButton()

    # Screen 1.2 - Order Type: Carry out
    if(DoesItExist('//*[@id="FNSR004000"]/div/div/div[1]/span/span')):
        CarryOut = driver.find_element(By.XPATH, '//*[@id="FNSR004000"]/div/div/div[1]/span/span')
        CarryOut.click()
        NextButton()

    if(DoesItExist('//*[@id="FNSR012000"]/td[1]/span') or DoesItExist('//*[@id="FNSR000121"]/td[1]/span')):
        # Screen 2 - Rate Satisfication | Big Chunk | Completely Random Order
        try:
            SpeedService = driver.find_element(By.XPATH, '//*[@id="FNSR012000"]/td[1]/span')
            SpeedService.click()
        except:
            print("Info: Option Not Present; Skipped")

        try:
            HealthSafety = driver.find_element(By.XPATH, '//*[@id="FNSR000121"]/td[1]/span')
            HealthSafety.click()
        except:
            print("Info: Option Not Present; Skipped")

        try:
            FriendlyTeam = driver.find_element(By.XPATH, '//*[@id="FNSR010000"]/td[1]/span')
            FriendlyTeam.click()
        except:
            print("Info: Option Not Present; Skipped")

        try:
            Accuracy = driver.find_element(By.XPATH, '//*[@id="FNSR008000"]/td[1]/span')
            Accuracy.click()
        except:
            print("Info: Option Not Present; Skipped")

        try:
            Appearance = driver.find_element(By.XPATH, '//*[@id="FNSR011000"]/td[1]/span')
            Appearance.click()
        except:
            print("Info: Option Not Present; Skipped")

        try:
            Exterior = driver.find_element(By.XPATH, '//*[@id="FNSR014000"]/td[1]/span')
            Exterior.click()
        except:
            print("Info: Option Not Present; Skipped")

        try:
            PortionSize = driver.find_element(By.XPATH, '//*[@id="FNSR007000"]/td[1]/span')
            PortionSize.click()
        except:
            print("Info: Option Not Present; Skipped")

        try:
            Taste = driver.find_element(By.XPATH, '//*[@id="FNSR005000"]/td[1]/span')
            Taste.click()
        except:
            print("Info: Option Not Present; Skipped")
        
        try:
            Cleanliness = driver.find_element(By.XPATH, '//*[@id="FNSR013000"]/td[1]/span')
            Cleanliness.click()
        except:
            print("Info: Option Not Present; Skipped")
        NextButton()

    # Screen 3 - Problem In Visit (No)
    if(DoesItExist('//*[@id="FNSR024000"]/td[2]/span')):
        Problem = driver.find_element(By.XPATH, '//*[@id="FNSR024000"]/td[2]/span')
        Problem.click()
        NextButton()

    # Screen 4 - You said You were highly satisfied
    # Pick a Canned Response
    FinalResponse = HighlySatisfiedResponses()

    if(DoesItExist('//*[@id="S081000"]')):
        TextBox1 = driver.find_element(By.XPATH, '//*[@id="S081000"]')
        TextBox1.click()
        TextBox1.send_keys(FinalResponse)
        NextButton()

    # Screen 4 - Reconize Team Member? Yes
    if(DoesItExist('//*[@id="FNSR030000"]/td[1]/span')):
        ReconizeMember = driver.find_element(By.XPATH, '//*[@id="FNSR030000"]/td[1]/span')
        ReconizeMember.click()
        NextButton()

    # Screen 5 - Name Drop Time
    # Team Member Name
    if(DoesItExist('//*[@id="S081001"]')):

        # Fill in Name
        TeamMemberName = driver.find_element(By.XPATH, '//*[@id="S081001"]')
        TeamMemberName.send_keys(CashierName)

        # Team Member Extended Response
        FinalResponse = CashierName + EmployeePraise()
        TeamMemberDescription = driver.find_element(By.XPATH, '//*[@id="S081002"]')
        TeamMemberDescription.send_keys(FinalResponse)
        NextButton()

    # Screen 6 - Hard or Soft Shell?
    if(DoesItExist('//*[@id="FNSR031000"]/td[2]/span')):
        HardShell = driver.find_element(By.XPATH, '//*[@id="FNSR031000"]/td[2]/span')
        HardShell.click()

        try:
            CrispyChickenTaco = driver.find_element(By.XPATH, '//*[@id="FNSR000127"]/td[2]/span')
            print("Info: Chicken Sandwich Taco Present")
            CrispyChickenTaco.click()
        except:
            print("Info: Option Not Present; Skipped")
        NextButton()

    # Screen 7 - Health Safety Extended Response
    if(DoesItExist('//*[@id="S000124"]')):
        HealthySafetyER = driver.find_element(By.XPATH, '//*[@id="S000124"]')
        FillResponse2 = CashierName + " made me feel safe. All interactions followed decent guidelines regarding saftey!"
        HealthySafetyER.send_keys(FillResponse2)
        NextButton()

    # Screen 8 - Enter Sweepstakes? (No, for now..)
    Sweepstakes = driver.find_element(By.XPATH, '//*[@id="FNSR046000"]/td[2]/span')
    Sweepstakes.click()

    # Final Submission
    if(testing == True):
        print("Info: Skipping next button due to testing")
    else:
        CmdClear()
        NextButton()
        print("Info: Survey Completed Successfully") 
    
except:
    # Exception Handling
    print("Error: Chrome and WebDriver Version Desync")
    print("Solution: The Earliest Error Code Points to the Solution")
    print("Info: The Survey Did Not Complete Successfully")

# Let User See Completion Screen
time.sleep(20)
driver.quit()