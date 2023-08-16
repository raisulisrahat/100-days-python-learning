# Here i am showing Practising Day 21 in python

# Time Built-In Modules
import time

def countdown(timer):       # countdown timer
    while timer:
        hours, mins, secs = divmod(timer, 3600), divmod(timer % 3600, 60), timer % 60
        times = '{:02d}:{:02d}:{:02d}'.format(hours[0], mins[0], secs)
        print(times, end="\r")
        time.sleep(1)
        timer -= 1
    print('Your time has been closed!!')

timer = input("Enter the time in secend: ")
countdown(int(timer))


# Date Built-In Modules
from datetime import date

def age(birthdate):         # age calculator
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

year = int(input("Enter birth year (YYYY): "))
month = int(input("Enter birth month (MM): "))
day = int(input("Enter birth day (DD): "))
birthdate = date(year, month, day)

calculated_age = age(birthdate)
print("Your age is:", calculated_age)

