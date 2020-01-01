
def print_mat(mat):
    for row in mat:
        print(row)

def add_mat(mat1, mat2, rows, cols):
    result = []
    for i in range(0,rows): # go through each row
        new_row = []
        for j in range(0, cols):
            new_row.append(mat1[i][j] + mat2[i][j])
        result.append(new_row) 
    return result


def sub_mat(mat1, mat2, rows, cols):
    result = []
    for i in range(0,rows): # go through each row
        new_row = []
        for j in range(0, cols):
            new_row.append(mat1[i][j] - mat2[i][j])
        result.append(new_row) 
    return result
   
def dot_star_mat(mat1, mat2, rows, cols):
    result = []
    for i in range(0,rows): # go through each row
        new_row = []
        for j in range(0, cols):
            new_row.append(mat1[i][j] * mat2[i][j])
        result.append(new_row) 
    return result
    
def mul_mat(mat1, mat2):

    result = []
    for i in range(len(mat1)):
        row = [0] * len(mat2[0])
        result.append(row)

    # iterate through rows of X
    for i in range(len(mat1)):
        # iterate through columns of Y
        for j in range(len(mat2[0])):
            # iterate through rows of Y
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result
    
def read_matrix(input_prompt, rows, cols):
    matrix = []
    for i in range(0,rows):
        row = input(input_prompt + " {} ".format(i+1) + "row in a single line with elements separated by spaces : ")
        row = list(map(int, row.strip().split()))
        print(row)
        matrix.append(row)     
      
    return matrix

def matrix_operations(mat1, mat2, rows, columns, opr):
    result = None
    if opr == '+':
        result = add_mat(mat1,mat2, rows, columns)
    elif opr == '-':
        result = sub_mat(mat1,mat2, rows, columns)
    elif (opr == 'x') or (opr == 'X'):
        result = dot_star_mat(mat1, mat2, rows, columns)
    elif (opr == '*'):
        result = mul_mat(mat1, mat2)
    elif (opr == 'mult'):
        result = mul_mat(mat1, int(input("Whats the scale factor : ")))
    elif (opr == 'div'):
        result = mul_mat(mat1, int(input("Whats the division factor : ")))
    else:
        print("Bro, what even is that?")
        exit()
    return result

def scale_mult(mat1, scale_factor):
    result = []
    for i in range(0,rows): # go through each row
        new_row = []
        for j in range(0, cols):
            new_row.append(mat1[i][j] * scale_factor)
        result.append(new_row) 
    return result

def scale_div(mat1, div_factor):
    result = []
    for i in range(0,rows): # go through each row
        new_row = []
        for j in range(0, cols):
            new_row.append(mat1[i][j] * div_factor)
        result.append(new_row) 
    return result

rows = int(input("How many rows : "))
columns = int(input("How many collums : "))
mat1 = read_matrix("enter first matrix: ", rows, columns)
mat2 = read_matrix("enter second matrix: ", rows, columns)
opr = '+'
while True:
    opr = input("enter operation (+ = Add, - = Substract, X or x = dot product, * = product, div for scale division, mult for scale multiplication. enter 0 to exit) : ")
    if (opr == '0'):
        print("thank you for using our excellent product. exiting....")
        exit()
    result = matrix_operations(mat1, mat2, rows, columns, opr)
    print("result ....")
    print_mat(result)