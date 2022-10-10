# lectio To Google Calendar
## What is it?
This is a small script that will fetch the readings for the day from the [Lectio](https://www.lectio.dk/) website and add them to your Google Calendar.

[Lectio](https://www.lectio.dk/) is a website used by many schools in Denmark to manage their students' schedules and assignments. It also contains the daily schedules for the students. This script will fetch the schedule for the next month and add them to your Google Calendar. This way you can easily see what you have to do for the next month. if you run this script continuously, you will also see any changes to your schedule so you can always see what you have to do.

this script is written in Python and uses the [Google Calendar API](https://developers.google.com/calendar/) as well as the [Lectio API](https://github.com/HSPDev/lectio).
## Installation
0. pre-requisites:  
     1. python (I used 3.10.7)  
     2. pip  
     3. git  
     4. a NEW google account with no current calendars  

you will also need the following user environment variables (i will explain how to set them up later, so don’t worry if you don’t know what they are just yet 😊)  
* `LECTIO_USER` (Lectio username)  
* `LECTIO_PASS` (Lectio password)  
* `LECTIO_INST_ID`  
* `LECTIO_STUDENT_ID`  

### installation:
find a directory to install the script in, and run the following commands:
```
git clone https://github.com/victorDigital/lectioToGoogleCalendar
cd lectioToGoogleCalendar
pip install -r requirements.txt
```
### configuration:
2. log into your Letio account and find your `LECTIO_INST_ID` and `LECTIO_STUDENT_ID` by going to your schedule and looking at the URL, it should look something like this:
```
https://www.lectio.dk/lectio/681/SkemaNy.aspx?type=elev&elevid=12345678901
```
where `681` is your `LECTIO_INST_ID` and `12345678901` is your `LECTIO_STUDENT_ID`  
(Be careful when working with environment variables, if you override an existing variable, you can really mess up your system, so make sure you don't override any existing variables)  
3. on Windows you open the app `Edit the system environment variables` and click `Environment Variables` and then `New` to create a new variable, and then `Edit` to edit an existing variable.  
4. you can also add the `LECTIO_PASS` and `LECTIO_USER` to your environment variables, the values should be your lectio username and password.  
#### that is all you need for the Lectio part of the configuration, now for the Google Calendar part (which sadly is a bit more complicated):  
5. go to the [Google Calendar API](https://console.developers.google.com/apis/library/calendar-json.googleapis.com) and log in with your NEW google account, and click `Enable`
   1. make sure you are on the `NEW` google account, if you are not, log out and log in with the `NEW` google account
   2. make sure you have a selected project, if you don't, click `Select a project` and then `New Project` and give it a name like `lectioToGoogleCalendar` and click `Create`
6. click `OAuth consent screen` and fill in the form, then click `Save` (in the scope section, you must include `https://www.googleapis.com/auth/calendar`)
   1. make sure to click external when you are asked if you are developing an internal or external app
7. click `Credentials` and then `Create Credentials` and select `OAuth client ID`
   1. make sure the application type is `Desktop app`
8. now when you click `Create` you will be asked to download a file, download it and save it in the `lectioToGoogleCalendar` directory
   1. make sure to rename the file to `client_secret.json`
9. now you can run the quickstart.py script by running ```python quickstart.py``` in the `lectioToGoogleCalendar` directory
   1. this will open a browser window and ask you to log, log in with your NEW google account
   2. after you have logged in, you will be asked to give the script permission to access your google calendar (you can revoke this permission at any time, but it doesent matter because it's a new google account)
   3. after you have given the script permission, close the browser window  
   4. the script will run a series of tests  
      1.  the result of the tests should look something like this:
      ```
        Token file exists
        Do you want to update the token? (y/n): y
        Updating token...
        Test1: PASS ✅
        Test2: PASS ✅
        Test3: PASS ✅
        Test4: PASS ✅
        Test5: PASS ✅
        Test6: PASS ✅
        Test7: PASS ✅
        Test8: PASS ✅
        All tests passed! Would would you like to run the program? (y/n):
      ```
      1.  if you get an error, refer troubleshooting section below   
11. to add the calendar to your google calendar app, click the `+` button in the bottom right corner and select `subscribe to calendar` and paste the email address of the new calendar into the text box and click `Add Calendar`  
12. now you can see your schedule in your google personal calendar   
13. Enjoy! 😊  

## Usage
every time you run the script, it will fetch the schedule for the next month and add it to your calendar, so if you run it manually every day, you will always have the next month's schedule in your calendar.  
i recommend running the script on a Raspberry PI or something similar, so you can just leave it running and it will update your calendar every 30 mins without you having to do anything.  

## Troubleshooting
if you get an error like this:
```
googleapiclient.errors.HttpError: <HttpError 403 ... "The caller does not have permission">
```
it could mean that you have not given the script permission to access your google calendar, to fix this, you need to delete the `token.json` file and run the `quickstart.py` script again.  
it could also mean that you have not specified the correct scope in the `OAuth consent screen` section, to fix this, you need to go to the `OAuth consent screen` click `Edit` and make sure that the scope includes `https://www.googleapis.com/auth/calendar` and then click `Save` and then delete the `token.json` file and run the `quickstart.py` script again.  


other errors are probably caused by something else, so if you get an error, you can open an GitHub issue and i will try to help you.

## TO-DO
expand troubleshooting section in README.md
use rich library to make the script look better