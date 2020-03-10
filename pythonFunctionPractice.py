def gramsToOunces(grams):
    ounces = 28.3495231 * grams
    return ounces

def fahrenheitToCelsius(f):
    c = (5 / 9) * (f – 32)
    return c 

def compoundIntrest(principal, years, rate):
    amount = (principal * ((1 + rate) ** years))
    return amount

def solve(numheads, numlegs): #We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
    ns = 'No solutions!'
    for i in range(numheads + 1):
        j = numheads - i
        if 2 * i + 4 * j == numlegs:
            return i, j
    return ns,ns

