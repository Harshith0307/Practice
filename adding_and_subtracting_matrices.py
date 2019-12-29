m = int(input("How many rows : "))
n = int(input("How many collums : "))
mat1 = []

def print_mat(mat):
    for row in mat:
        print(row)
      
for i in range(0,m):
    row = []
    for j in range(0, n):
        element = input("enter first matrix [{},{}] ".format(i+1, j+1))
        element = int(element)
        row.append(element)
    mat1.append(row)
print_mat(mat1)
mat2 = []
# o = int(input("How many rows : "))
# p = int(input("How many collums : "))

for k in range(0,m):
    row = []
    for l in range(0, n):
        element = input("enter second matrix [{},{}] ".format(k+1, l+1))
        element = int(element)
        row.append(element)
    mat2.append(row)
print_mat(mat2)
result = []
opr = str(input("what operation : "))

if opr == '+':
    for i in range(0,m):
        new_row = []
        for j in range(0, n):
            new_row.append(mat1[i][j] + mat2[k][l])
        result.append(new_row)        

elif opr == '-':
    for i in range(0,m):
        new_row = []
        for j in range(0, n):
            new_row.append(mat1[i][j] - mat2[k][l])
        result.append(new_row)   
elif (opr == '*') or (opr == '/') or (opr == 'x'):
    print("Yeah bro... i don't really know how to multiply or divide YET")
    exit()
else:
    print("Bro, what even is that?")
    exit()

print("result ....")
print_mat(result)