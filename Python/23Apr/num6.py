#! /usr/bin/env python3

def main():
    print('''Quantity\t\tDiscount
    _____________________________
    10-19\t\t20%
    20-49\t\t30%
    50-99\t\t40%
    100+\t\t50%
    _____________________________''')
    packages = float(input("Please enter how many packages you want: "))
    discount = 0.0
    subtotal = 99.0 * packages
    total = 0.0
    if packages < 0.9:
        print("Please enter a positive number")
        main()
    if packages ==1:
        print("Your subtotal before discount is: ", subtotal, " for ", packages, " package.")
    else:
        print("Your subtotal before discount is: ", subtotal, " for ", packages, " packages.")
    
    if (packages >= 10.0 and packages <= 19.0):
        discount = 0.2 * subtotal
        total = discount + subtotal
        print("Your discount is 20%: ", discount, "\nAnd your total cost for ", packages, " packages is: ", total)
    elif (packages >= 20.0 and packages <= 49.0):
        discount = 0.3 * subtotal
        total = discount + subtotal
        print("Your discount is 30%: ", discount, "\nAnd your total cost for ", packages, " packages is: ", total)
    elif (packages >= 50.0 and packages <= 99.0):
        discount = 0.4 * subtotal
        total = discount + subtotal
        print("Your discount is 40%: ", discount, "\nAnd your total cost for ", packages, " packages is: ", total)
    elif (packages >= 100.0):
        discount = 0.5 * subtotal
        total = discount + subtotal
        print("Your discount is 50%: ", discount, "\nAnd your total cost for ", packages, " packages is: ", total)
    elif (packages < 10 and packages > 0):
        if packages == 1:
            print("Your total cost for ", packages, " package is: ", subtotal, " and no discount was applied.")
        else:
            print("Your total cost for ", packages, " packages is: ", subtotal, " and no discount was applied.")
    else:
        print("Please try again....")
    main()
main()