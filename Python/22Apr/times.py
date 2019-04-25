#! /usr/bin/env python3

minutes = int(input("Enter the number of minutes: "))

year = 525600 
day = 1440
hour = 60
minuteL = minutes

years, minuteL = divmod(minuteL, year)
days, minuteL = divmod(minuteL, day)
hours, minuteL = divmod(minuteL, hour)

print years, " years ", days, " days ", hours, " hours and ", minuteL, " minutes"
wait = input ("press enter to continue....")