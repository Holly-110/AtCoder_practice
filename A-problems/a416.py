N, L, R = map(int, input().split())
S = list(input())

S_LR = S[L-1:R]

if 'x' in S_LR:
    print("No")
else:
    print("Yes")
