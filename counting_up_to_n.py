#counting up to n; 123...n ie if n = 4, output will be 1234

if __name__ == '__main__':
    n = int(input())

    #Math, works for 0-9
    sum = 0
    for i in range(1,n+1):
        sum = sum + (i*(10**(n-i)))
    print(sum)

    #print function, works for any number
    for i in range(1, n+1):
        print(i, end = "")


