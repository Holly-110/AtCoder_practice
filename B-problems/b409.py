N = int(input())
A_list = list(map(int, input().split()))

ans = 0

for i in range(1,N + 1):
    cnt = 0
    for a in A_list:
        if i <= a:
            cnt += 1
            if cnt >= i:
                ans = i

print(ans)