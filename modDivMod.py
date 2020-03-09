def computateDiv(a, b):
    c = divmod(a, b)
    return c[0]

def computateMod(a,b):
    g = divmod(a, b)
    return g[1]

a = int(input())
b = int(input())

print(computateDiv(a,b))
print(computateMod(a,b))
print(divmod(a,b))
