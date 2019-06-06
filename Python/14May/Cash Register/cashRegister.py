# cashRegister.py

import retail

class CashRegister:

    # initialize an empty list to hold purchased items
    def __init__(self):

        self.__items = []

    # method that clears the contents of the cash register
    def clear(self):

        self.__items = []

    # method that simulates adding an item to the cash register.
    # receives a RetailItem object as an argument. 
    def purchase_item(self, retail_item):

        self.__items.append(retail_item)
        print("The item was added to the cash register.")

    # method returning the total cost of items at the cash register.
    def get_total(self):

        total = 0.0
        for item in self.__items:
            total = total + item.get_price()

        return total

    # method that prints a list of items at the cash register.
    def show_items(self):

        print("The items in the cash register are:")
        print()
        for item in self.__items:
            print(item)
            print()
 
# 11-7.py

import retail
import cashRegister

# constants to hold the options of purchase items
PANTS = 1
SHIRT = 2
DRESS = 3
SOCKS = 4
SWEATER = 5


def main():

    #create sale items
    pants = retail.RetailItem("Pants", 10, 19.99)
    shirt = retail.RetailItem("Shirt", 15, 12.50)
    dress = retail.RetailItem("Dress", 3, 79.00)
    socks = retail.RetailItem("Socks", 50, 1.00)
    sweater = retail.RetailItem("Sweater", 5, 49.99)

    # create dictionary of sale items
    sale_items = {PANTS:pants, SHIRT:shirt, \
                  DRESS:dress, SOCKS:socks, SWEATER:sweater}

    # create a cash register
    register = cashRegister.CashRegister()

    # initialize loop test
    checkout = 'N'

    # user wants to purchase more items
    while checkout=='N':

        user_choice = get_user_choice()
        item = sale_items[user_choice]
        if item.get_inventory() == 0:
            print("The item is out of stock.")
        else:
            register.purchase_item(item)

            # update item
            new_item = retail.RetailItem(item.get_description(),\
                                         item.get_inventory()-1,\
                                         item.get_price())
            sale_items[user_choice] = new_item

            checkout = input("Are you ready to check out (Y/N)? ")

    print()
    print("Your purchase total is: ", format(register.get_total(), '.2f'))
    print()
    register.show_items()
    register.clear()




def get_user_choice():

    print("Menu")
    print("---------------------------------")
    print("1. Pants")
    print("2. Shirt")
    print("3. Dress")
    print("4. Socks")
    print("5. Sweater")
    print()

    choice = int(input("Enter the menu number of the item " +\
                       "you would like to purchase: "))
    print()

    while choice > SWEATER or choice < PANTS:

        choice = int(input("Please enter a valid item number: "))
        print()

    return choice


main()