N = int(input())
X_list = list(map(int, input().split()))

X_len = len(X_list)
hp_sum_list = []

for p in range(1,101):
    hp_sum = 0
    for x in X_list:
        hp = (x - p) * (x - p)
        hp_sum += hp
    hp_sum_list.append(hp_sum)

print(hp_sum_list)
print(min(hp_sum_list))