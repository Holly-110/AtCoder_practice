N, M = map(int, input().split())
A = list(map(int, input().split()))

A_total = sum(A)

if A_total <= M:
    print("Yes")
else :
    print("No")