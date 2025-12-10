def find_min_index(X_box):
    min_value = min(X_box)
    min_index = X_box.index(min_value)
    return min_index

N, Q = map(int, input().split())
X_list = list(map(int, input().split()))
X_box = [0]*N

for i in range(Q):
    if X_list[i] >= 1:
        X_box[X_list[i] - 1] += 1
        print(X_list[i], end = ' ')
    elif X_list[i] == 0:
        index = find_min_index(X_box)
        X_box[index] += 1
        print(index + 1, end = ' ')
print()
    