import decimal
from decimal import Decimal, getcontext
import time
import sys
import progress.bar
from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
    AdaptiveETA, FileTransferSpeed, FormatLabel, Percentage, \
    ProgressBar, ReverseBar, RotatingMarker, \
    SimpleProgress, Timer, UnknownLength

start = time.time()
digit = int(input("How many digits to calculate? "))
getcontext().prec = digit+1
am, a, b, t, p = 0, 1, 1/Decimal(2).sqrt(), Decimal(1/4), 1

widgets = [Bar('>'), ' ', ETA(), ' ']
with ProgressBar(widgets=widgets, maxval=10000000).start() as pbar:
    for i in range(digit):
        am, bm, tm, pm = a, b, t, p 
        pi = Decimal((a+b)**2/(4*t))
        a = Decimal((am+bm)/2)
        b = Decimal(am*bm).sqrt()
        t = Decimal(tm-pm*(am-a)**2)
        p = 2*pm
        pbar.update(0.5*i + 1)
    
#print(pi)

end = time.time()
print("\n\nFor {} digits, That took: {} seconds".format(digit, end-start))