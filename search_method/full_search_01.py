#全探索の基礎

N, K = map(int, input().split())
A_list = list(map(int, input().split()))

cnt = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if A_list[i] + A_list[j] + A_list[k] == K:
                cnt += 1

print(cnt)

