N = int(input())
L = list(map(int, input().split()))

cnt = 1

for l in L:
    if l == 1:
        break
    cnt += 1

for l in reversed(L):
    if l == 1:
        break
    cnt += 1

if cnt >= N:
    print("0")
else :
    print(N - cnt)