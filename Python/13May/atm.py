#! /usr/bin/env python3

'''
    Rochelle Gardner
    13 May 2019
    ATM

        Use the Account class to simulate an ATM
    Create ten accounts in a list with the ids 0, 1,... 9
    and an initial balance of $100. The system prompts
    the user to enter an id. If the id is entered incorrectly
    ask the user to enter a correct id. Once an id is 
    accepted, the main menu is displayed as shown in the 
    sample run. You can enter a choice of 
    1.  for viewing the current balance
    2.  for withdrawing money
    3.  for depositing money
    4.  for exiting the menu 
'''

class Account:
    # Construct an Account object 
    def __init__(self, id, balance = 100):
        self.__id = id
        self.__balance = balance

    def getId(self):
        return self.__id

    def getBalance(self):
        print("\nBalance: ", self.__balance)
        return self.__balance

    def withdraw(self):
        while True:
            amount = input("Enter the amount you want to withdraw: ")
            try:
                amount = int(amount)
                if amount > self.__balance:
                    print("Cannont withdraw more than you have...")
                else:
                    self.__balance -= amount
                    return self.__balance
            except ValueError:
                print("Enter a whole dollar amount...")
        

    def deposit(self):
        while True:
            amount = input("Enter the amount you want to deposit: ")
            try:
                amount = int(amount)
                self.__balance += amount
                return self.__balance
            except ValueError:
                print("Enter a whole dollar amount...")


def main():
    while True:
        id = input("Enter your ID: ")
        try:
            id = int(id)
            if (id >=0 and id <= 9):
                break
            else:
                print("Please try again with an id 0-9...")
        except ValueError:
            print("Must be a number 0-9! Try again...")

    account = Account(id, 100)

    while True:
        print("\n\t1. View Current Balance")
        print("\t2. Make a Withdrawl")
        print("\t3. Make a Deposit")
        print("\t4. Enter a new ID")
        print("\t5. Exit")
        choice = int(input("---> "))

        if (choice == 1):
            account.getBalance()
        elif (choice == 2):
            account.withdraw()
        elif (choice == 3):
            account.deposit()
        elif (choice == 4):
            main()
        elif (choice == 5):
            print("\nGoodbye")
            exit()
    
    print("ID is", account.getId())
    print("Balance is", account.getBalance())
    
          
main()