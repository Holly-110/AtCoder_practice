N, K = map(int, input().split())
A_list = list(map(int, input().split()))

ans = 1

for i in range(N):
    ans = ans * A_list[i]
    ans_str = str(ans)
    if len(ans_str) >= K + 1:
        print(ans, i)
        ans = 1

print(ans)