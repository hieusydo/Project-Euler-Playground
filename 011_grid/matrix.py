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

##Find all vertical, horizontal, left diagonal, and right diagonal products
product = 0
for row in range(20):
    for col in range(20):
        try:
            down = mat[row][col]*mat[row+1][col]*mat[row+2][col]*mat[row+3][col]
            left = mat[row][col]*mat[row][col+1]*mat[row][col+2]*mat[row][col+3]
            diagright = mat[row][col]*mat[row+1][col+1]*mat[row+2][col+2]*mat[row+3][col+3]
            diagleft = mat[row][col]*mat[row+1][col-1]*mat[row+2][col-2]*mat[row+3][col-3]
            ##Keep track of the greatest product
            if product < max(down, left, diagright, diagleft):
                product = max(down, left, diagright, diagleft)
        except IndexError:
            pass
print "Greatest product: ", product

stop = timeit.default_timer()
print stop - start 
