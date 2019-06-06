import time
import math

start = time.time()
precision = int(input("How many spaces? "))

while precision > 1000000000:
	print("Number to large")
	precision = int(input("How many spaces? "))
else:
	print('%.*f' % (precision, math.pi))

end = time.time()

print("\n", end - start, " seconds")