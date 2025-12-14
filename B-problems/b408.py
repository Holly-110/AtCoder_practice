N = int(input())
A_list = list(map(int, input().split()))

A_set = set(A_list)

print(len(A_set))
A_set_sorted = sorted(A_set)
print(' '.join([str(x) for x in A_set_sorted]))