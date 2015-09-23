#Project Euler - Problem 2 - Jan 18, 2015

#generate an n-th Fib number
def fib(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b 
    return b

#an empty list to store all the Fib values of interest
fibSeries = []

#iterate until the last value smaller than 4,000,000 is found. Store all the even number
for i in range(34):
    if fib(i) % 2 == 0:
        fibSeries.append(fib(i))

#find the sum of all the even numbers in the series that are smaller than 4,000,000
print sum(fibSeries)
