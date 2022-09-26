# lectioToGoogleCalendar
## What is it?

## Installation
0.  pre-requisites:
* python (i used 3.10.7)
* pip
* git
* a NEW google account with no current calendars

you will also need the folowing user environment variables (i will explain how to set them up later, so dont worry if you dont know what they are just yet 😊):
* (GOOGLE_CALENDAR (NEW))
* `TOKEN` 
* `client_id`
* `REFRESH_TOKEN`
* `client_secret`
* `token_uri`
* (LECTIO)
* `user`
* `pass`
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
5. go to the [Google Calendar API](https://console.developers.google.com/apis/library/calendar-json.googleapis.com) and click `Enable`
6. click `OAuth consent screen` and fill in the form, then click `Save` (in the scope section, you must include `https://www.googleapis.com/auth/calendar`)



## Usage

## Troubleshooting

## todo
edit README.md