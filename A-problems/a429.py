N, M = map(int, input().split())

for n in range(1, N+1):
    if n <= M:
        print("OK")
    else:
        print("Too Many Requests")