S = list(input())

cnt = 0
target_num = []

for i in range(len(S)):
    if S[i] == '#':
        cnt += 1
        target_num.append(i+1)

for i in range(0, len(target_num), 2):
    if i + 1 < len(target_num):
        item1 = target_num[i]
        item2 = target_num[i + 1]
        print(f"{item1}, {item2}")
    else :
        item1 = target_num[i]
        print(f"{item1}")