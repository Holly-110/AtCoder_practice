N = int(input())

S = [input() for _ in range(N)]

X, Y = input().split()
X = int(X)

if S[X-1] == Y:
    print("Yes")
else :
    print("No")

