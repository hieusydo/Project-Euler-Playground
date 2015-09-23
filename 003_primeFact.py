from __future__ import division

def primeFact():
    x = 600851475143
    dvd = 2
    while True:
        ##keep dividing x by dvd, incrementing dvd by 1 each time, until the modulo is 0
        if x == 1:
            break
        if x%dvd != 0:
            dvd += 1
        ##after the first prime is found,
        ##continue to divide until the last (largest) prime factor is found
        else:
            x = x/dvd
            print(dvd)
            
