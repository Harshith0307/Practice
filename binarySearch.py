#binary search in python
import random
import math


def randomNumber(x, y):
    return random.randint(1,101)


def sortedList(numOfValues):
    listLength = numOfValues
    sortedList = [1]

    for item in range(0, listLength - 1):
        sortedList.append(randomNumber(sortedList[item], sortedList[item+3]))
    
    return sortedList


def binarySearch(list, value):
    low = 0
    high = len(list) - 1
    mid = math.floor((low+high)/2)
    searching = False
    while(not(searching)):
    if(value == list[mid]):
        searching = True
        print(value, " found at index of ", mid)
    elif(value > list[mid]):
        low = mid
    elif(value < list[mid]):
        high = mid


length(int(input("How long do you want the randomly sorted list to be: ")))
sorList = sortedList(length)
flag = False

while(not(flag)):
    if(sorList.isalnum() == True):
        print(sorList)
        binarySearch(sorList, 11)
        flag = True

    else:
        sorList = str(sorList)
        sorList.sort()
        sorList = int(sorList)
    


