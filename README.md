# lectioToGoogleCalendar
## What is it?
This is a small script that will fetch the readings for the day from the [Lectio](https://www.lectio.dk/) website and add them to your Google Calendar.

[Lectio](https://www.lectio.dk/) is a website used by many schools in Denmark to manage their students' schedules and assignments. It also contains the daily schedules for the students. This script will fetch the schedule for the next month and add them to your Google Calendar. This way you can easily see what you have to do for the next month. if you run this script continuously, you will also see any changes to your schedule so you can always see what you have to do.

this script is written in Python and uses the [Google Calendar API](https://developers.google.com/calendar/) as well as the [Lectio API](https://github.com/HSPDev/lectio).
## Installation
0. pre-requisites:  
     1. python (i used 3.10.7)  
     2. pip  
     3. git  
     4. aNEW google account with no current calendars  

you will also need the folowing user environment variables (i will explain how to set them up later, so dont worry if you dont know what they are just yet 😊):
* `TOKEN` 
* `client_id`
* `REFRESH_TOKEN`
* `client_secret`
* `token_uri`
* `user` (Lectio username)
* `pass` (Lectio password)
* `LECTIO_INST_ID`
* `student_id`

### installation:
1. find a directory to install the script in, and run the following commands:
```
git clone https://github.com/victorDigital/lectioToGoogleCalendar
cd lectioToGoogleCalendar
pip install -r requirements.txt
```
### configuration:
2. log into your Letio acount and find your `LECTIO_INST_ID` and `student_id` by going to your schedule and looking at the url, it should look something like this:
```
https://www.lectio.dk/lectio/681/SkemaNy.aspx?type=elev&elevid=12345678901
```
where `681` is your `LECTIO_INST_ID` and `12345678901` is your `student_id`  
(be careful when workkin with environment variables, if you override an existing variable, you can relly mess up your system, so make sure you dont override any existing variables)  
3. on Windows you open the app `Edit the system environment variables` and click `Environment Variables` and then `New` to create a new variable, and then `Edit` to edit an existing variable.  
4. you can also add the `pass` and `user` to your environment variables, the values should be your lectio username and password.  
#### that is all you need for the Lectio part of the configuration, now for the Google Calendar part (witch is a bit more complicated):  
5. go to the [Google Calendar API](https://console.developers.google.com/apis/library/calendar-json.googleapis.com) and log in with your NEW google account, and click `Enable`
   1. make sure you are on the `NEW` google account, if you are not, log out and log in with the `NEW` google account
   2. make sure you have a selected project, if you dont, click `Select a project` and then `New Project` and give it a name like `lectioToGoogleCalendar` and click `Create`
6. click `OAuth consent screen` and fill in the form, then click `Save` (in the scope section, you must include `https://www.googleapis.com/auth/calendar`)
   1. make sure to click external when you are asked if you are developing an internal or external app
7. click `Credentials` and then `Create Credentials` and select `OAuth client ID`
   1. make sure the application type is `Desktop app`
8. now when you click `Create` you will be asked to download a file, download it and save it in the `lectioToGoogleCalendar` directory
   1. make sure to rename the file to `client_secret.json`
9. now you can run the quickstart.py script by running ```python quickstart.py```in the `lectioToGoogleCalendar` directory
   1. this will open a browser window and ask you to log, log in with your NEW google account
   2. after you have logged in, you will be asked to give the script permission to access your google calendar (you can revoke this permission at any time , but it doesent matter because it's a new google account)
   3. after you have given the script permission, close the browser window, 
   4. the script will run a series of tests, 
   5. after you have done that, the script will create a file called `token.pickle` in the `lectioToGoogleCalendar` directory



## Usage

## Troubleshooting

## todo
edit README.md