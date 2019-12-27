#Find the second highest number in a given array, this time in a given set of scores

if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))
    high_score = max(scores)
    
    while max(scores) == high_score:
        scores.remove(max(scores))
    
    print(max(scores))