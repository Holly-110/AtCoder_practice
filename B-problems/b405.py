N, M = map(int, input().split())
A_list = list(map(int, input().split()))

cnt = 0

for i in range(N-1, 1, -1):
    for j in range(1, M+1):
        if (j in A_list):
            continue
        else:
            print(cnt)
            exit()
    del A_list[i]
    cnt += 1