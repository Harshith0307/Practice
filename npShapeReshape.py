import numpy as np

def rShape(x, y, z): #y and z are the dimensions, created a function for simplicity
    arr = np.copy(x)
    arr = np.reshape(arr, (y, z))
    return arr


x = list(map(int, input().split()))
print(rShape(x, 3, 3))