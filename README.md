*Author: Jared Myers*

*Updated: 3/18/23*

# Purpose

The purpose of this short and simple Python script is to quickly complete the survey found at the top of each and every Taco Bell receipt. I found that it is somewhat long and annoying to take mannually and I feel that its length is a major deterrant to those wanting to take the survey.

Additionally, taking the survey and naming the employee listed on the reciept earns the worker at my local location monetary compensation per survey mention and I value their hard work.

# Requirements

Outlined below are the required installations to make the magic happen:
## The Script
First, you need to download the entirety of this repository to your machine. This can be down easily by downloading a ZIP of it via the green "Code" button on GitHub. Extract the contents to wherever you wish to the files on your machine.

## Python
Installing Python on your machine is very simple. Simply install it here: https://www.python.org/downloads/ 

On Windows, customize the installation and check the box titled "Add Python to Enviroment Variables"

If you are unsure if Python is installed on your machine type ```python3 -v``` in your terminal. 

I wrote this using Python 3.9.5, any backwards compatibility is uncharted territory.

## Selenium
To install Selenium you need to type the following command on your respective command line/console.

### Mac/Linux:
```pip3 install selenium```

NOTE: ```sudo``` is sometimes required infront of this command as well based on your permissions

### Windows: 
```pip install selenium```
## Google Chrome + Chrome Driver
## Chrome:

I chose to use Google Chrome as it commonly found on many people's machines: MacOS or Windows. 
Simply install Google Chrome here: https://www.google.com/chrome/ if you do not already have it installed.
Additionally, it must be updated to Version 111.+

## Driver: 

#### Mac/Linux:
1. To install the associated Chrome Driver, navigate here: https://sites.google.com/chromium.org/driver/ and click on the correct Driver that matches your Chrome Version and platform. 
2. Once downloaded, cut and paste the chromedriver into the same directory as the python script.
3. Open Terminal
4. Run ```sudo nano /etc/paths```
5. Enter your password
6. You are now in a basic text editor and will need to add the file path structure where it is located. 
Example: ```/Users/MY NAME/TacoBellAutomation```
7. Control + X to quit editing
8. Y to save changes
9. Finally, press enter once more to complete the edits (annoying I know)

### Windows:

1. To install the associated Chrome Driver, navigate here: https://sites.google.com/chromium.org/driver/ and click on the correct Driver that matches your Chrome Version and platform. 
2. Once downloaded, cut and paste the chromedriver into the same directory as the python script.

# Usage

There are two ways to execute this python script: The included .bat file and via the CMD Console. While they both work the same, the .bat file is included for the simplicity of the user.

## Using the .Bat File:
NOTE: This does NOT work on Mac/Linux
 1. Navigate to the directory where the .bat file is located
 2. Simply double click the TakeSurvey.bat
 
## Via CMD Line:
1. Open your terminal/CMD Console
2. Navigate to the directory where the .py file is located
3. Enter the command 
```python3 Survey.py```
4. Press Enter

# Troubleshooting
I plan to fill this in as people use it and run into problems. Fortunately, this is easily Googlable in most cases!

1.
2.
3.

# Known Issues/Future Plans
1. Actually do the chance for 500$ cause free $ lol
2. N/A
