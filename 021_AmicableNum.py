#Hieu Do - 3/7/15
#Project Euler 21
import time
import math

#Find the sum of all the proper divisors of n (numbers less than n which divide evenly into n)
def d(n):
    total = 1
    for divisor in range(2, int(math.sqrt(n) + 1)):
        if n%divisor == 0:
            total += divisor
            total += int(n/divisor)
    return total

start = time.time()

#Find the sum of all amicable numbers under 10000
amicables = []
for num in range(1, 10000):
    if d(d(num)) == num and d(num) != num:
        amicables.append(d(num))
print(sum(amicables))

print("Elapsed time {}".format(time.time() - start))


