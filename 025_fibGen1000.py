#Project Euler - Problem 25 - Feb 20, 2015

#Keep track of the n-th term
term = 2
#generate an n-th Fib number
a, b = 1, 1
while True:
    a, b = b, a + b
    term += 1
    if len(str(b)) == 1000: #First term to have 1000 digits
        print term
        break
