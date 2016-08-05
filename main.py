import time
import webbrowser
import random


currentHour = time.localtime().tm_hour  # Return the current hour
currentMinute = time.localtime().tm_min  # Return the current minute
currentSecond = time.localtime().tm_sec  # Return the current seconds
alarmHour = 0
alarmMinute = 0
alarmSeconds = 0

# Combine hour and minute into a string to be displayed
currentTime = str(currentHour) + ':' + str(currentMinute).zfill(2)

print('Hello, welcome to your Max Alarm. The current time is ' + currentTime)  # Short introduction
print('\nWhat time would you like the alarm to go off?')  # Question for the user

errorCheck = 0  # Setting the error check to zero (no errors)

while errorCheck == 0:
    alarmTime = input('Alarm time (HH:MM): ')

    if len(alarmTime) == 5:
        alarmHour = alarmTime[0] + alarmTime[1]
        alarmHour = int(alarmHour)
        alarmMinute = alarmTime[3] + alarmTime[4]
        alarmMinute = int(alarmMinute)
        errorCheck = 1
    else:
        print('You didn\'t use the correct format, did you mean to set an alarm in a certain amount of time?')
        errorAnswer = input('Enter Y / N: ')
        if errorAnswer.lower() == 'y':
            errorCheck = 0
            minutesOrHours = input('Minutes, hours or seconds? ' )
            if minutesOrHours.lower() == 'minutes':
                addMinutes = input('Enter minutes: ')
                alarmHour = int(currentHour) + (int(addMinutes) / 60)
                alarmHour = int(alarmHour)
                alarmMinute = int(currentMinute) + (int(addMinutes) % 60)
                alarmMinute = int(alarmMinute)
                if alarmHour > 23:
                    print('Too high, setting to maximum')
                    alarmHour = 23
                    alarmMinute = 59
                elif alarmMinute > 59:
                    print('Too high, setting to maximum')
                    alarmMinute = 59
                else:
                    errorCheck = 1
            elif minutesOrHours.lower() == 'hours':
                addHours = input('Enter hours: ')
                alarmHour = int(currentHour) + int(addHours)
                alarmMinute = int(currentMinute)
                if alarmHour > 23:
                    print('Too high, setting to maximum')
                    alarmHour = 23
                    alarmMinute = 59
                elif alarmMinute > 59:
                    print('Too high, setting to maximum')
                    alarmMinute = 59
                else:
                    errorCheck = 1
            elif minutesOrHours.lower() == 'seconds':
                addSeconds = input('Enter seconds: ')
                alarmHour = int(currentHour) + (int(addSeconds) / (60 * 60))
                alarmHour = int(alarmHour)
                alarmMinute = int(currentMinute) + ((int(addSeconds) / 60) % 60)
                alarmMinute = int(alarmMinute)
                if alarmHour > 23:
                    print('Too high, setting to maximum')
                    alarmHour = 23
                    alarmMinute = 59
                elif alarmMinute > 59:
                    print('Too high, setting to maximum')
                    alarmMinute = 59
                else:
                    errorCheck = 1
            else:
                print('Invalid entry, going back to the start!')
                errorCheck = 0
        elif errorAnswer.lower() == 'n':
            print('Going back to the start!')
            errorCheck = 0

currentHour = time.localtime().tm_hour  # Return the current hour
currentMinute = time.localtime().tm_min  # Return the current minute
currentSecond = time.localtime().tm_sec # Return the current seconds

currentTotalSeconds = (currentHour * 60 * 60) + (currentMinute * 60)  # Works out current time in seconds
alarmTotalSeconds = (alarmHour * 60 * 60) + (alarmMinute * 60) + int(alarmSeconds)  # Works out alarm time in seconds
alarmSet = int(alarmTotalSeconds) - int(currentTotalSeconds)  # Works out seconds different between

if alarmSet < 1:
    alarmSet = int(addSeconds)

# Prints the seconds until alarm
print('Alarm set for ' + str(alarmSet) + ' seconds (' + str(alarmHour).zfill(2) + ':' + str(alarmMinute).zfill(2) + ')')

while alarmSet > 0:
    alarmSet -= 1
    time.sleep(1)

results = []
with open('youtube.txt') as inputfile:
    for line in inputfile:
        results.append(line.strip().split('\n'))

youtubeLink = random.randrange(0,len(results))

print('Opening ' + str(results[youtubeLink][0]))
webbrowser.open(str(results[youtubeLink][0]))