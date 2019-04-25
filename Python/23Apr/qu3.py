#! /usr/bin/env python3

def reverse(number):
  reverse = 0    
  while(number > 0):    
    remainder = number %10    
    reverse = (reverse *10) + remainder    
    number = number //10    
  print("\nReverse of entered number is = %d" %reverse)  

def main():
  number = int(input("Please enter an integer: "))
  reverse(number)
main()