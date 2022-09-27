from __future__ import print_function
from array import array
from ast import Delete

import datetime
from doctest import master
import os.path
import os

from operator import le
import os
from turtle import update
from lectio import Lectio
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
import time
from tokenUpdate import tokenUpdate
from datetime import date, timedelta
import datetime
import pytz
import requests
from rich.progress import Progress, track

SCOPES = ['https://www.googleapis.com/auth/calendar']

class bcolors:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    PULSE = '\033[5m'
    BOLD = '\033[1m'

load_dotenv()
calendarId = "primary"
l = Lectio(os.environ["LECTIO_INST_ID"])
reach = 30 # How many days ahead to sync
scheduler = BackgroundScheduler()

def sched():
    scheduler.add_job(main, 'interval', hours=0.5)
    scheduler.start()
    print("INFO: Schedule started, syncing every 30 minutes, press ctrl+c to stop and exit")
    main()
    while True:
        time.sleep(1)

def deleteAllEvents():
    service = tokenUpdate()
    events_result = service.events().list(calendarId=calendarId, singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])
    i = 0
    for i in track(range(len(events)), description="Deleting old events..."):
        event = events[i]
        service.events().delete(calendarId=calendarId, eventId=event['id']).execute()
        i += 1
    print(bcolors.OKCYAN+"INFO: "+bcolors.OKGREEN+"All events deleted, fetching new events"+bcolors.ENDC)

def updateCalendar():
    l.authenticate(os.environ["LECTIO_USER"], os.environ["LECTIO_PASS"])
    start = datetime.datetime.now() + timedelta(days=0)
    end = start + timedelta(days=reach)
    schedule = l.get_schedule_for_student(os.environ["LECTIO_STUDENT_ID"], start, end)
    for i in track(range(len(schedule)), description="Adding to calendar... "):
        lesson = schedule[i]
        addToCalendar(lesson)
    print(bcolors.OKCYAN+"INFO: "+bcolors.OKGREEN+"All events added to calendar successfully"+bcolors.ENDC)

def addToCalendar(lesson):
    service = tokenUpdate()
    # Create event
    event = {
        'summary': lesson.subject,
        'location': lesson.room,
        'description': lesson.url,
        'start': {
            'dateTime': lesson.start_time.isoformat(),
            'timeZone': 'Europe/Copenhagen',
        },
        'end': {
            'dateTime': lesson.end_time.isoformat(),
            'timeZone': 'Europe/Copenhagen',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=1'
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }
    service.events().insert(calendarId=calendarId, body=event).execute()

def generateTimeID(time):
    return str(time.day) + str(time.month) + str(time.year)[-1]

def main():
    deleteAllEvents()
    updateCalendar()

def master():
    print(bcolors.BOLD+"thanks for using this script,"+bcolors.WARNING+" it is still in development and might not work as expected!"+bcolors.ENDC)
    print(bcolors.WARNING+"if the script is not working, please refer to the github installation guide here:"+bcolors.ENDC)
    print(bcolors.OKGREEN+"https://github.com/victorDigital/lectioToGoogleCalendar"+bcolors.ENDC)
    print(bcolors.BOLD+"if you have any questions or suggestions, please contact me on GitHub"+bcolors.ENDC)
    print(bcolors.PULSE+"version: 0.3"+bcolors.ENDC)
    print(bcolors.OKCYAN+"-"*50+bcolors.ENDC)
    print(bcolors.FAIL+"WARN: Starting script in 15 seconds, DO NOT RUN ON PERSONAL CALENDAR, if in doubt press ctrl+c to cancel NOW!!!!"+ bcolors.ENDC)
    time.sleep(15)
    sched()

if __name__ == '__main__':
    master()
    