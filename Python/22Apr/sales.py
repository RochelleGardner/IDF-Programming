#! /usr/bin/env python3

item1 = float(input("\nEnter the price of item 1: "))
item2 = float(input("Enter the price of item 2: "))
item3 = float(input("Enter the price of item 3: "))
item4 = float(input("Enter the price of item 4: "))
item5 = float(input("Enter the price of item 5: "))
subtotal = (item1 + item2 + item3 + item4 + item5)
tax = float(subtotal * .06)
total = (subtotal + tax)
              
print "\nYour receipt: "
print "Item 1:\t\t", item1
print "Item 2:\t\t", item2
print "Item 3:\t\t", item3
print "Item 4:\t\t", item4
print "Item 5:\t\t", item5
print "\nSubtotal:\t", subtotal
print "Taxes:\t\t", tax
print "Total:\t\t", total
leave = input("\nPress enter to continue")
