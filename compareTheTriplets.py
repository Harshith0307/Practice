#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice = 0
    bob = 0

    for item in range(0, len(a)): #could be range(0, len(b))
        if(a[item] > b[item]):
            alice += 1
        elif(a[item] == b[item]):
            alice = alice
            bob = bob
        else:
            bob += 1
    
    finalScore = [alice, bob]
    print(finalScore[0], finalScore[1])


if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)


