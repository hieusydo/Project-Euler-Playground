import timeit
start = timeit.default_timer()

#Load 100 50-digit number
mat =[]
matrix = open('50digitnumber.txt', 'r')
for i in range(100):
    line = matrix.readline().strip().split()
    for j in line:
        mat.append(int(j))
matrix.close()

#++++++++++FASTEST AND EASIEST WAY TO SOLVE++++++++++
print(str(sum(mat))[:10])

#++++++++++MOST COMPLICATE WAY TO SOLVE++++++++++
storeVal = []
for i in range(50):
    storeMem = 0
    for num in mat:
        storeMem += int(num[i])
    storeVal.append(storeMem*10**(49-i))
print storeVal, sum(storeVal)

stop = timeit.default_timer()
print stop - start 

