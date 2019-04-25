#! /usr/bin/env python3

weighti = float(input("What is your weight in lbs? "))
heighti = float(input("What is you height in inches? "))
weightm = weighti/2.2046
heightm = heighti/39.37
bmi = weightm/ (heightm ** 2)

print "Your BMi is ", bmi, "%"
wait = input("press enter to continue....")