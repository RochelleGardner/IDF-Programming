cents = int(input("Enter your amount of change in cents: "))

change = cents
quarter = 25
dime = 10
nickel = 5
penny = 1

quarters, change = divmod(change, quarter)
dimes, change = divmod(change, dime)
nickels, change = divmod(change, nickel)
pennies, change = divmod(change, penny)

print ("Quarters: ", quarters, "\tDimes: ", dimes)
print ("Nickels: ", nickels, "\tPennies: ", pennies)
wait = input("press enter to continue...")
