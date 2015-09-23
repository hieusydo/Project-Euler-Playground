matrix = open('018.txt', 'r')
tri = []
for i in range(15):
    line = matrix.readline().split()
    for j in range(len(line)):
        line[j] = int(line[j])
    tri.append(line)
matrix.close()

base = 14

while base >= 0:
    tempTri = []
    for i in range(len(tri[base])-1):
        tempTri.append(max(tri[base][i], tri[base][i+1]) + tri[base-1][i])
    if base >0:
        tri.pop(base)
        tri.pop(base-1)
    tri.append(tempTri)
    base -= 1

print tri
