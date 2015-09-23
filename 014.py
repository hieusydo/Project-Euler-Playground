import timeit
start = timeit.default_timer()

limit = 10
storelen = []
chainlen = 1

for n in range(1, 1000000):
    start = n
    while n != 1:
        if n%2 == 0:
            n = n/2
            chainlen += 1
        else:
            n = 3*n + 1
            chainlen += 1
    storelen.append([chainlen, start])
    chainlen = 1

print(max(storelen))
stop = timeit.default_timer()
print "Elapsed:", stop - start 
