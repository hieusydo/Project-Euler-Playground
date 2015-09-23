import math
import time

start = time.time()

def checkAbun(n):
    sumDiv = 1
    divisor = 1
    for divisor in range(2, int(math.sqrt(n)+1)):
        if n % divisor == 0:
            sumDiv += divisor
            if divisor != int(n/divisor):
                sumDiv += int(n/divisor)

    if sumDiv > n:
        return True
    return False

abun = set()
for i in range(12, 28124):
    if checkAbun(i) == True:
        abun.add(i)

allSumAbun = set()
for i in abun:
    for j in abun:
        allSumAbun.add(i+j)

allIntCond = set()
for i in range(1, 28124):
    if i not in allSumAbun:
        allIntCond.add(i)
print("Sum: ", sum(allIntCond))

stop = time.time()

elapse = stop - start
print("Elapsed:", elapse)
