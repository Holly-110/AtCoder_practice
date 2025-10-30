N, M, K = map(int, input().split())

ivent = {}
achieve = []

for i in range(K):
    a, b = map(int, input().split())
    ivent[a] = ivent.get(a, 0) + 1
    if ivent[a] == M:
        achieve.append(a)

print(*achieve)