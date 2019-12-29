m = int(input("How many rows : "))
n = int(input("How many collums : "))
mat1 = []

for i in range(0,m):
    row = []
    for j in range(0, n):
        element = input("enter [{},{}] ".format(i+1, j+1))
        element = int(element)
        row.append(element)
    mat1.append(row)
