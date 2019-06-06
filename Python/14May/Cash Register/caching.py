import math


items = [["Pants", 10, 19.99, "Just some pants"],\
        ["Shirt", 15, 12.50, "A plain shirt"], \
        ["Dress", 3, 79.00, "There's no way that dress is gonna fit"], \
        ["Socks", 50, 1.00, "Colorful mismatched socks"], \
        ["Sweater", 5, 49.99, "That sweater looks itchy"]]

def get_inventory(item):
    if item == 1:
        inventory = items[0][1]
        return inventory
    elif item == 2:
        inventory == items[1][1]
        return inventory
    elif item == 3:
        inventory == items[2][1]
        return inventory
    elif item == 4:
        inventory == items[3][1]
        return inventory
    elif item == 5:
        inventory == items[4][1]
        return inventory
    else:
        print("An error occured...")


def check_out(choice):
    checkout = 'N'
    inventory = 0

    while checkout == 'N':
        if choice == 1:
            item = items[0][1]
            print(item)
            break
        elif choice == 2:
            item == items[1][1]
            print(item)
            break
        elif choice == 3:
            item == items[2][1]
            print(item)
            break
        elif choice == 4:
            item == items[3][1]
            print(item)
            break
        elif choice == 5:
            item == items[4][1]
            print(item)
            break
        else:
            print("An unexpected error occured...")
            item_choice()
        
    get_inventory(item)
    print (inventory)
        


def item_choice():
    while True:
        print("""
        Menu
        ____________________________
        What would you like to buy?
        ____________________________
        1. Pants
        2. Shirt
        3. Dress
        4. Socks
        5. Sweater
        0. Quit
        """)
        choice = input("---> ")
        try:
            choice = int(choice)
            if choice == 0:
                print("Goodbye")
                exit()
            check_out(choice)
        except ValueError:
            print("Please enter a menu option by number")

def main():
    print(items[0][1])
    print(items[1][1])
    print(items[2][1])
    print(items[3][1])
    print(items[4][1])
    item_choice()


main()