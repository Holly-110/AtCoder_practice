N = int(input())
D_list = list(map(int, input().split()))

for i in range(N - 1):
    for j in range(i + 1, N):
        if j < N - 1:
            print(sum(D_list[i:j]), end = ' ')
        else:
            print(sum(D_list[i:j]))