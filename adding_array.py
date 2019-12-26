def addArray(ar):
    sum = 0
    for item in ar:
        sum = sum + item
    return sum

if __name__ == '__main__':
    count_array = int(input())
    ar = list(map(int, input().strip().split()))
    ans = addArray(ar)
    built_in_answer = sum(ar)
    print(ans)
    print("Validation success = ", built_in_answer==ans)