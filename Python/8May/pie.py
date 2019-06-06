import time
import datetime as dt
import sys
import decimal
from decimal import Decimal
from progress.bar import Bar

def calcPi():
    am, a, b, t, p = 0, 1, 1/Decimal(2).sqrt(), Decimal(1/4), 1
    while am != a:
        pi = Decimal((a+b)**2/(4*t))
        am, bm, tm, pm = a, b, t, p

        a = Decimal((am+bm)/2)
        b = Decimal(am*bm).sqrt()
        t = Decimal(tm-pm*(am-a)**2)
        p = 2*pm
    return pi

def main():
    start = time.time()

    pi_digits = calcPi()
    i = 0
    c = int(input("Enter how many digits of pi to show: "))

    fp = open("pitext.txt", "w+")

    with Bar('Working', max=c) as bar:
        for d in pi_digits:
            if (d % 1000) == 0:
                fp.write(str(d))
                i += 1
                bar.next()
                if i == c: 
                    break
            else:
                #pbar.update(1)
                fp.write(str(d))
                i += 1
                bar.next()
                if i == c: 
                    break
        #bar.finish()
        
    end = time.time()

    print("\n\nFor ", c, " digits, That took:", end-start, " seconds\n")

    fp.close()

main()    
