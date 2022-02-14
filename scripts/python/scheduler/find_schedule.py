#!/usr/bin/python
import sys
import pytz
from datetime import datetime

timezones = []
map = {"IST": "Asia/Calcutta",
       "AEST": "Australia/NSW",
       "HKT": "Asia/Hong_Kong"}


def find_recommended_time(raw_string):
    print("Finding Recommendations for:", raw_string)
    sydney_timezones = convert_to_local_timezones(raw_string)
    print("Sydney Timezones:", sydney_timezones)
    return sydney_timezones


def convert_to_local_timezones(raw_string):
    response = []
    arr = sanitize_input(raw_string)
    print("detected timezone", timezones)
    foreign_timezone_string = map[timezones[0]]
    sydney = pytz.timezone('Australia/Sydney')

    for v in arr:
        time_obj = __convert_to_hour(v)
        now = datetime.utcnow()
        foreign_timezone = pytz.timezone(foreign_timezone_string)
        dt = datetime(now.year, month=now.month, day=now.day, hour=time_obj.hour,
                      minute=time_obj.minute)
        dt = foreign_timezone.localize(dt)
        time_in_sydney = dt.astimezone(sydney)
        print("Other Person Available times:", timezones[0], dt.strftime("%I:%M %p"), "Potential Time in Sydney:",
              time_in_sydney.strftime("%I:%M %p"))
        response.append(time_in_sydney.strftime("%I:%M %p"))
    return response


def sanitize_input(input=[]):
    response = []
    for raw_string in input:
        response += __split_time(raw_string)
    return response


def __split_time(raw_string):
    arr = []
    if raw_string.isalpha():
        arr = []  # do nothing
    elif "-" in raw_string:
        arr = raw_string.split("-")
        from_time = arr[0]
        to_time = arr[1]
        arr = [__convert_to_time_object(from_time), __convert_to_time_object(to_time)]
    else:
        arr = [__convert_to_time_object(raw_string)]
    return arr


def __convert_to_time_object(input):
    if "p" in input and " " in input:
        arr = input.split(" ")
        timezones.append(arr[1])
        date1 = __convert_to_hour(arr[0][:-1] + " PM")
    elif "p" in input:
        arr = input.split(" ")
        timezones.append(arr[1])
        date1 = __convert_to_hour(arr[0][:-1] + " PM")
    elif "PM" in input:
        arr = input.split(" ")
        timezones.append(arr[2])
        date1 = __convert_to_hour(arr[0] + " " + arr[1])
    elif " " in input:
        arr = input.split(" ")
        timezones.append(arr[1])
        date1 = __convert_to_hour(arr[0])
    else:
        date1 = __convert_to_hour(input)
    return date1.strftime('%H:%M')


def __convert_to_hour(input):
    if "PM" in input and ":" in input:
        date1 = datetime.strptime(input, '%I:%M %p')
    elif ":" in input:
        date1 = datetime.strptime(input, '%H:%M')
    else:
        date1 = datetime.strptime(input, '%H')
    return date1


def __contains_numbers(inputString):
    return any(char.isdigit() for char in inputString)


if __name__ == '__main__':
    if len(sys.argv) > 0:
        del (sys.argv[0])
    find_recommended_time(sys.argv)
