from selenium import webdriver

driver = webdriver.Chrome()

# Need to check if Chrome is Updated to Match Driver before this !!!
driver.get('https://www.tellthebell.com/')

# Finds Entry Box and starts typing
sixteen_digit = input("Please enter the 16 digit code from your survey: ")
cashier_name = input("Please enter the name listed team member: ")
survey_code_box = driver.find_element_by_xpath('//*[@id="CN1"]')
survey_code_box.send_keys(sixteen_digit)

# Find Start Button and Clicks
start_button_click = driver.find_element_by_xpath('//*[@id="NextButton"]')
start_button_click.click()

# If Sccessful
# Screen 1
HighSatisfy1 = driver.find_element_by_xpath('//*[@id="FNSR001000"]/td[2]/span')
HighSatisfy1.click()
Next1 = driver.find_element_by_xpath('//*[@id="NextButton"]')
Next1.click()

# Screen 2
SpeedService = driver.find_element_by_xpath('//*[@id="FNSR012000"]/td[2]/span')
SpeedService.click()

HealthSafety = driver.find_element_by_xpath('//*[@id="FNSR000121"]/td[2]/span')
HealthSafety.click()

FriendlyTeam = driver.find_element_by_xpath('//*[@id="FNSR010000"]/td[2]/span')
FriendlyTeam.click()

Accuracy = driver.find_element_by_xpath('//*[@id="FNSR008000"]/td[2]/span')
Accuracy.click()

Appearance = driver.find_element_by_xpath('//*[@id="FNSR011000"]/td[2]/span')
Appearance.click()

Exterior = driver.find_element_by_xpath('//*[@id="FNSR014000"]/td[2]/span')
Exterior.click()

PortionSize = driver.find_element_by_xpath('//*[@id="FNSR007000"]/td[2]/span')
PortionSize.click()

# Is this Identical to above? if so remove and reuse!
Next2 = driver.find_element_by_xpath('//*[@id="NextButton"]')
Next2.click()

# Screen 3
Accuracy2 = driver.find_element_by_xpath('//*[@id="FNSR008000"]/td[2]/span')
Accuracy2.click()

Next1 = driver.find_element_by_xpath('//*[@id="NextButton"]')
Next1.click()

# Screen 4 - Problem In Visit
Problem = driver.find_element_by_xpath('//*[@id="FNSR024000"]/td[3]/span')
Problem.click()

# Does this work?
Next1 = driver.find_element_by_xpath('//*[@id="NextButton"]')
Next1.click()

# Screen #5 - You said You were highly satisfied
StockResponse1 = "Food was amazing and the speed was incredible"
TextBox1 = driver.find_element_by_xpath('//*[@id="S081000"]')
TextBox1.send_keys(StockResponse1)

# Does this work?
Next1 = driver.find_element_by_xpath('//*[@id="NextButton"]')
Next1.click()

# Screen #6 - Reconize Team Member
ReconizeMember = driver.find_element_by_xpath('//*[@id="FNSR030000"]/td[2]/span')

# Does this work?
Next1 = driver.find_element_by_xpath('//*[@id="NextButton"]')
Next1.click()

# Screen 7 - Name Drop Time
# Team Member Name
TeamMemberName = driver.find_element_by_xpath('//*[@id="S081001"]')
TeamMemberName.send_keys(cashier_name)

TeamMemberDescription = driver.find_element_by_xpath('//*[@id="S081001"]')
FillResponse = cashier_name + " did an excellent job taking care of myself and other customers in the line. Exception work!"
TeamMemberDescription.send_keys(FillResponse)

# Does this work?
Next1 = driver.find_element_by_xpath('//*[@id="NextButton"]')
Next1.click()

# Screen 8 - Hard or Soft Shell?
HardSoft = driver.find_element_by_xpath('//*[@id="FNSR031000"]/td[3]/span')
HardSoft.click()

# Does this work?
Next1 = driver.find_element_by_xpath('//*[@id="NextButton"]')
Next1.click()

# Screen 9 - Health Saftey Extedned Response
HealthySafetyER = driver.find_element_by_xpath('//*[@id="S000124"]')
FillResponse = cashier_name + " made me feel safe. All interactions followed strict guidelines regarding saftey!"
HealthySafetyER.send_keys(FillResponse)



##############################################
#invalid_code = driver.find_element_by_xpath('//*[@id="surveyQuestions"]/div[1]')

# if its on page kill script
#if(invalid_code == true)
