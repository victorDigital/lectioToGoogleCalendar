from __future__ import print_function

import datetime
import os.path
import random
from re import I
import program
import time

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    PULSE = '\033[5m'

def main():
    run = True
    if os.path.exists('token.json'):
        print(bcolors.WARNING+"Token file exists"+bcolors.ENDC)
        # aks if user wants to update token
        updateToken = input(bcolors.OKCYAN+"Do you want to update the token? (y/n): "+bcolors.ENDC)
        if updateToken == "y":
            print(bcolors.OKCYAN+"Updating token..."+bcolors.ENDC)
        else:
            print(bcolors.OKCYAN+"Keeping current"+bcolors.ENDC)
            run = False 
    if run:
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'client_secret.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        service = build('calendar', 'v3', credentials=creds)
        #make a event in the calendar in the next 10 minutes
        event = {
            'summary': 'Test Event',
            'location': 'Somewhere',
            'description': 'This is a test event',
            'start': {
                'dateTime': (datetime.datetime.utcnow() + datetime.timedelta(minutes=10)).isoformat(),
                'timeZone': 'UTC',
            },
            'end': {
                'dateTime': (datetime.datetime.utcnow() + datetime.timedelta(minutes=20)).isoformat(),
                'timeZone': 'UTC',
            },
            'id': str(random.randint(10000,1000000000)),
        }
        try: 
            service.events().delete(calendarId='primary', eventId=event['id']).execute()
        except HttpError as e:
            pass
        passAllChecks = True
        if os.environ.get('LECTIO_USER') == None:
            print(bcolors.FAIL+"Test1: FAIL ❌"+bcolors.ENDC)
            print(bcolors.FAIL+"LECTIO_USER enviroment variable not set"+bcolors.ENDC)
            print(bcolors.OKCYAN+"Setting it now..."+bcolors.ENDC)
            os.environ['LECTIO'] = str(input("Enter your lectio username: "))
        else:
            print(bcolors.OKGREEN+"Test1: PASS ✅"+bcolors.ENDC)
        if os.environ.get('LECTIO_PASS') == None:
            print(bcolors.FAIL+"Test2: FAIL ❌"+bcolors.ENDC)
            print(bcolors.FAIL+"LECTIO_PASS enviroment variable not set"+bcolors.ENDC)
            print(bcolors.OKCYAN+"Setting it now..."+bcolors.ENDC)
            os.environ['LECTIO_PASS'] = str(input("Enter your lectio password: "))
        else:
            print(bcolors.OKGREEN+"Test2: PASS ✅"+bcolors.ENDC)

        if os.environ.get('LECTIO_USER') != None and os.environ.get('LECTIO_PASS') != None:
            print(bcolors.OKGREEN+"Test3: PASS ✅"+bcolors.ENDC)
        else:
            passAllChecks = False
            print(bcolors.FAIL+"Test3: FAIL ❌"+bcolors.ENDC)

        if os.environ.get('LECTIO_INST_ID') != None and os.environ.get('LECTIO_STUDENT_ID') != None:
            print(bcolors.OKGREEN+"Test4: PASS ✅"+bcolors.ENDC)
        else:
            passAllChecks = False
            print(bcolors.FAIL+"Test4 FAIL ❌"+bcolors.ENDC)

        if os.path.exists('token.json'):
            print(bcolors.OKGREEN + "Test5: PASS ✅" + bcolors.ENDC)
        else:
            print(bcolors.FAIL + "Test5: FAIL ❌" + bcolors.ENDC)
            passAllChecks = False
        try:
            event = service.events().insert(calendarId='primary', body=event).execute()
            print(bcolors.OKGREEN + "Test6: PASS ✅" + bcolors.ENDC)
        except HttpError as e:
            print(bcolors.FAIL + "Test6: FAIL ❌" + bcolors.ENDC)
            print(e)
            passAllChecks = False
        try:
            event = service.events().get(calendarId='primary', eventId=event['id']).execute()
            print(bcolors.OKGREEN + "Test7: PASS ✅" + bcolors.ENDC)
        except HttpError:
            print(bcolors.FAIL + "Test7: FAIL ❌" + bcolors.ENDC)
            passAllChecks = False
        #now delete the event we just made
        try:
            service.events().delete(calendarId='primary', eventId=event['id']).execute()
            print(bcolors.OKGREEN + "Test8: PASS ✅" + bcolors.ENDC)
        except HttpError as e:
            print(bcolors.FAIL + "Test8: FAIL ❌" + bcolors.ENDC)
            print(e)
            passAllChecks = False
        if passAllChecks:
            run = input(bcolors.OKGREEN + "All tests passed! Would would you like to run the program? (y/n): " + bcolors.ENDC)
            if run == "y":
                print(bcolors.OKCYAN + "Running program..." + bcolors.ENDC)
                time.sleep(2)
                clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                clearConsole()
                program.master()
            else:
                print(bcolors.OKCYAN + "Exiting..." + bcolors.ENDC)
                exit()

if __name__ == '__main__':
    main()