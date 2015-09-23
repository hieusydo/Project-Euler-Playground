#Project Euler 22 - Hieu Do - 3/8/2015

from time import *
start = clock()

file = open('names.txt', 'r')
names = file.readline().strip('"').split('","')
file.close()
names.sort()
import string

dictionary = {}
i = 1
for alpha in string.ascii_uppercase:
    dictionary[alpha] = i
    i += 1

def nameScore(name):
    alphaScore = 0
    for char in name:
        alphaScore += dictionary[char]
    return alphaScore*(names.index(name)+1)

totalNameScore = 0
for name in names:
    totalNameScore += nameScore(name)

print("Sum", totalNameScore)
print("Elapsed:", clock()-start, "s")

