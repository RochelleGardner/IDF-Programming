import math

principal = float(input("total loan amount taken: "))
interest_rate = float(input("annual interest rate applied: "))
duration = int(input("loan duration in years: "))

def monthly_loan(principal,interest_rate,duration):
    n = duration*12 
    r = interest_rate/(100*12) 
    monthly_payment = principal*((r*((r+1)**n))/(((r+1)**n)-1)) 
    return monthly_payment

def remaining_bal(principal,annual_interest_rate,duration,payments):
    r = annual_interest_rate/1200 
    m = r + 1
    n = duration*12 
    
    remaining = principal*(((m**n)-(m**payments))/((m**n)-1))
    return remaining

monthly = monthly_loan(principal,interest_rate,duration)
print("Loan amount: ",principal," Interest rate: ",interest_rate)
print("Duration (Years): {}  Monthly payment: {:.2f}\n".format(duration, monthly))

'''for x in range(1,duration+1):
    mon = x*12
    rem = remaining_bal(principal,interest_rate,duration,mon)
    print("Year: ",x," Balance remaining: ",int(rem)," Total payments: ",int(monthly*mon))
'''
wait = input("press enter to continue... ")
