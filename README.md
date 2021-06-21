Author: Jared Myers
Updated: 6/18/21

# Purpose

The purpose of this short and simple Python script is to quickly complete the survey found at the top of each and every Taco Bell receipt. I found that it is somewhat long and annoying to take mannually and I feel that its length is a major deterrant to those wanting to take the survey.

Additionally, taking the survey and naming the employee listed on the reciept earns the workers at my local locations monetary compensation per survey mention and I value their hard work.

# Requirements

Outlined below are the required installations to make the magic happen
## The Script
First, you need to download the entirety of this repository to your machine. This can be down easily by downloading a ZIP of it via the green "Code" button on GitHub. Then Extract the contents to whereever you wish to storethe files on your machine.

## Python
Installing Python on your machine is very simple. Simply install it here: https://www.python.org/downloads/ On Windows, customize the installation and check the box titled "Add Python to Enviroment Variables"
If you are unsure if Python is installed on your machine type "python -v" in your terminal. I wrote this using Python 3.9.5, any backwards compatibility is uncharted territory.

## Selenium
To install Selenium you need to type the following command.

Mac/Linux: 
>pip3 install selenium

NOTE: "sudo" is required infront of this command as well!
Windows: 
>pip install selenium
## Google Chrome + Chrome Driver
Chrome:

I chose to use Google Chrome as it commonly found on many people's machines. Simple install Google Chrome here: https://www.google.com/chrome/ if you do not already have it installed.

Driver: 
To install the associated Chrome Driver, Navigate here: https://sites.google.com/a/chromium.org/chromedriver/downloads and click on the correct Driver that matches your Chrome Version and platform. Once downloaded, cut and paste the chromedriver into the same directory as the python script.

# Usage

There are two ways to execute this python script: The included .bat file and via the CMD Console. While they both work the same, the .bat file is included for the simplicity of the user.

## Using the .Bat File:
 1. Navigate to the directory where the .bat file is located
 2. If you are using Windows 10, simply double click the TakeSurvey.bat
## Via CMD Line:
1. Open your terminal/CMD Console
2. Navigate to the directory where the .py file is located
3. Enter the command 
```
python Survey.py
```
4. Press Enter
# Troubleshooting
