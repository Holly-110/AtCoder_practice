from itertools import combinations

N = int(input())
A_list = list(map(int, input().split()))
numbers = range(0, N)
all_pairs = list(combinations(numbers, 2))

cnt = 0

for pair in all_pairs:
    flag = True
    pair_sum = 0
    for i in range(pair[0], pair[1]+1):
        pair_sum += A_list[i]
    for i in range(pair[0], pair[1]+1):
        if pair_sum % A_list[i] == 0:
            flag = False
            break
    if flag:
        cnt += 1
    

print(cnt)