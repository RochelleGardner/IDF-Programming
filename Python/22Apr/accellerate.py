#! /usr/bin/env python3

svel = float(input("What is the starting velocity in peters per second? "))
evel = float(input("What is the ending velocity in meters per second? "))
time = float(input("How long did all that take? (in seconds) "))
accel = (evel - svel)/time

print "\nThe average acceleration was ", accel
wait = input ("press enter to continue....")