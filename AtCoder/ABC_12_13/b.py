N = int(input())

ans = [[0] * N for _ in range(N)]

x = int((N-1)/2)
ans[0][x] = 1
r = 0
c = x
k = 1

for _ in range(N*N - 1):
    if ans[(r-1) % N][(c+1)% N] == 0:
        ans[(r-1) % N][(c+1) % N] = k+1
        r = (r-1) % N
        c = (c+1) % N
        k = k+1
    else:
        ans[(r+1) % N][c] = k+1
        r = (r+1) % N
        c = c
        k = k+1

for i in range(N):
    for j in range(N):
        print(f"{ans[i][j]}", end=" ")
    print()

    

    