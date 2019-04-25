#! /usr/bin/env python3

#! /usr/bin/env python3

def mulNums():
  product = 0
  while product < 100:
    print("\nYou can multiply until the product is 100+")
    number = int(input("Please enter a number: "))
    product = number * 10
    print("That number multipied by 10 is: ", product)
  
  main()

def addNums():
  looping = True
  while looping == True:
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    num3 = num1 + num2
    print("The sum of ", num1, " and ", num2, " is: ", num3)
    choice = input("Would you like to add again? [y] or [n] ")
    if choice == 'y':
      addNums()
    elif choice == 'n':
      main()
    else:
      print("That wasn't an option...")   

def listNums():
  for i in range (0,100):
    num = i * 10
    print(num, ", ",end = "")
  main()

def main():
  menu = int(input('''\nPick one:
  1. Enter a number to be multiplied by 10
  2. Add two numbers
  3. Display a list
  0. Quit
  '''))
  if menu == 1:
    mulNums()
  elif menu == 2:
    addNums()
  elif menu == 3:
    listNums()
  elif menu == 0:
    exit
  else:
    print("Please try again...")
    main()
main()