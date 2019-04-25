#! /usr/bin/env python3

def main():
  speed = int(input("What is the speed of the vehicle in mph? "))
  time = int(input("How many hours has it traveled? "))
  if speed <= 0 or time <= 0:
    print("Please try again...")
    main()

  print ('''Hour\t\tDistance traveled
_________________________________''')

  for i in range(1,time):
    distance = speed * i
    print(i,"\t\t\t", distance)

main()