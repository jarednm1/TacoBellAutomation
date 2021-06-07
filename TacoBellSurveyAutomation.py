import random
from selenium import webdriver
# For Testing
import time
import random

def NextButton():
    Next1 = driver.find_element_by_xpath('//*[@id="NextButton"]')
    Next1.click()

driver = webdriver.Chrome()

# Need to check if Chrome is Updated to Match Driver before this !!!
driver.get('https://www.tellthebell.com/')

# Finds Entry Box and starts typing
#sixteen_digit = input("Please enter the 16 digit code from your survey: ")
#cashier_name = input("Please enter the name listed team member: ")

# For Dev
sixteen_digit = 1525803122870026
cashier_name = "Justin"

survey_code_box = driver.find_element_by_xpath('//*[@id="CN1"]')
survey_code_box.send_keys(sixteen_digit)

# Find Start Button and Clicks
start_button_click = driver.find_element_by_xpath('//*[@id="NextButton"]')
start_button_click.click()

# If Sccessful
# Screen 1 - Overall Satisfaction
HighSatisfy = driver.find_element_by_xpath('//*[@id="FNSR001000"]/td[2]/span')
HighSatisfy.click()
NextButton()

# Screen 2 - Rate Satisfication Big Chunk Completely Random Order
try:
    SpeedService = driver.find_element_by_xpath('//*[@id="FNSR012000"]/td[2]/span')
    SpeedService.click()
except:
        print("Option Not Present")

try:
    HealthSafety = driver.find_element_by_xpath('//*[@id="FNSR000121"]/td[2]/span')
    HealthSafety.click()
except:
    print("Option Not Present")

try:
    FriendlyTeam = driver.find_element_by_xpath('//*[@id="FNSR010000"]/td[2]/span')
    FriendlyTeam.click()
except:
    print("Option Not Present")

try:
    Accuracy = driver.find_element_by_xpath('//*[@id="FNSR008000"]/td[2]/span')
    Accuracy.click()
except:
    print("Option Not Present")

try:
    Appearance = driver.find_element_by_xpath('//*[@id="FNSR011000"]/td[2]/span')
    Appearance.click()
except:
    print("Option Not Present")

try:
    Exterior = driver.find_element_by_xpath('//*[@id="FNSR014000"]/td[2]/span')
    Exterior.click()
except:
    print("Option Not Present")

try:
    PortionSize = driver.find_element_by_xpath('//*[@id="FNSR007000"]/td[2]/span')
    PortionSize.click()
except:
    print("Option Not Present")

try:
    Taste = driver.find_element_by_xpath('//*[@id="FNSR005000"]/td[2]/span')
    Taste.click()
except:
        print("Option Not Present")

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
# Picks 0-2
choice = random.randint(0,2)

print(choice)

if (choice is 0):
    FinalResponse = StockResponse0
elif (choice is 1):
    FinalResponse = StockResponse1
else:
    FinalResponse = StockResponse2

TextBox1 = driver.find_element_by_xpath('//*[@id="S081000"]')
TextBox1.send_keys(FinalResponse)
# time.sleep(30)
NextButton()

# Screen 4 - Reconize Team Member? Yes
ReconizeMember = driver.find_element_by_xpath('//*[@id="FNSR030000"]/td[2]/span')
ReconizeMember.click()
NextButton()

# Screen 5 - Name Drop Time
# Team Member Name
TeamMemberName = driver.find_element_by_xpath('//*[@id="S081001"]')
TeamMemberName.send_keys(cashier_name)

TeamMemberDescription = driver.find_element_by_xpath('//*[@id="S081002"]')
FillResponse = cashier_name + " did an excellent job taking care of myself and other customers in the line. Exceptional work!"
TeamMemberDescription.send_keys(FillResponse)
NextButton()

# Screen 6 - Hard or Soft Shell?
HardSoft = driver.find_element_by_xpath('//*[@id="FNSR031000"]/td[3]/span')
HardSoft.click()
NextButton()

# Screen 7 - Health Saftey Extended Response
HealthySafetyER = driver.find_element_by_xpath('//*[@id="S000124"]')
FillResponse2 = cashier_name + " made me feel safe. All interactions followed strict guidelines regarding saftey!"
HealthySafetyER.send_keys(FillResponse2)
NextButton()

# Screen 8 - Enter Sweepstakes?
Sweepstakes = driver.find_element_by_xpath('//*[@id="FNSR046000"]/td[3]/span')
Sweepstakes.click()

# Final Submission
# NextButton()
