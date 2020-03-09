
eng_num = int(input())
eng_set = input().split()
eng_set = set(map(int, eng_set))
fren_num = int(input())
fren_set = input().split()
fren_set = set(map(int, fren_set))

print(len(eng_set.intersection(fren_set)))