def isPrime(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

def findPrime(x):
    count = 0
    num = 2

    while True:
        if isPrime(num) == True:
            count += 1
            if count == x:
                return num
        num += 1

