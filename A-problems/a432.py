num_list = list(map(int, input().split()))

for i in range(3):
    max_num = max(num_list)
    print(max_num, end="")
    num_list.pop(num_list.index(max_num))