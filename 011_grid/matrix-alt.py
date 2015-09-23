##SOLUTION BY TomRamsberger ON PROJECT EULER FORUM

import timeit
start = timeit.default_timer()

mat =[]

matrix = open('matrix.txt', 'r')
##Iterate over each line of code
for i in range(20):
    ##Declare var holder here so that it will not save the previous line in the matrix
    holder = []
    ##A powerful method that strips and splits a string at all space and new line
    line = matrix.readline().strip().split()
    for j in line:
        holder.append(int(j)) ##convert type from str to int
    mat.append(holder)
matrix.close()

matrix = mat
##Find all vertical, horizontal, left diagonal, and right diagonal products
maxProd, foundAt = 0, []
vectorOffsets = {'across':  ((0, 1),  (0, 2),  (0, 3)),
                 'down':    ((1, 0),  (2, 0),  (3, 0)),
                 'diagUp':  ((-1,1),  (-2,2),  (-3,3)),
                 'diagDown':((1, 1),  (2, 2),  (3, 3)) }

for row in range(20):
    for col in range(20):
        for vector, offsets in vectorOffsets.items():
            prod = matrix[row][col]
            for rowoff, coloff in offsets:
                if vector == 'diagUp' and row+rowoff < 0:
                    continue
                try:
                    prod *= matrix[row+rowoff][col+coloff]
                except IndexError:
                    continue
                if prod > maxProd:
                    maxProd, foundAt = prod, [row, col, vector]

row, col, vector = foundAt
print 'Max Product %d found at row %d, column %d, going %s \n' % (maxProd, row, col, vector), \
    '\n'.join(['row: %2d  col: %2d  val: %2d' %
              (row+rowoff, col+coloff, matrix[row+rowoff][col+coloff])
        for rowoff, coloff in ((0,0),) + vectorOffsets[vector] ])

stop = timeit.default_timer()
print stop - start 
