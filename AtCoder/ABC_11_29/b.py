N, M = map(int, input().split())

M_list = [0] * M
M_cnt = [0] * M
M_result = []

for i in range(N):
    A, B = map(int, input().split())
    M_list[A-1] += B
    M_cnt[A-1] += 1

for i in range(M):
    M_result.append(M_list[i] / M_cnt[i]) 

for m in M_result:
    print(m)

