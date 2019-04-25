#! /usr/bin/env python3

def main():
  cal = 3.9
  minute = 1
  for minute in range(1, 31):
    cpm = minute * cal
    if minute == 10:
      print ("Number of calories burned at ", minute, " minutes: ", cpm)
    elif minute == 15:
      print ("Number of calories burned at ", minute, " minutes: ", cpm)
    elif minute == 20:
      print ("Number of calories burned at ", minute, " minutes: ", cpm)
    elif minute == 25:
      print ("Number of calories burned at ", minute, " minutes: ", cpm)
    elif minute == 30:
      print ("Number of calories burned at ", minute, " minutes: ", cpm)
    else:
      pass
main()