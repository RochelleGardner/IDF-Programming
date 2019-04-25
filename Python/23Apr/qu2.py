#! /usr/bin/env python3

def reverse(number):
  num = number
  reverse = 0    
  while(number > 0):    
    remainder = number %10    
    reverse = (reverse *10) + remainder    
    number = number //10    
  print("\nReverse of entered number is = %d" %reverse) 
  ispalindrome(reverse, num)

def ispalindrome(reverse, num):  
    if (num == reverse): 
        print ("Number is a Palindrome")
        return True
    print ("Number is not a Palindrome")    
    return False
def main():
  number = int(input("Please enter an integer: "))
  reverse(number)
main()