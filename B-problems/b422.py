H, W = map(int, input().split())

masume = []

for i in range(H):
    masume.append(input())

jedge = "Yes"

for h in range(H):
    for w in range(W):
        if masume[h][w] == '#':
            cnt = 0
            if masume[h-1][w] == '#' :
                cnt += 1
            if masume[h+1][w] == '#' :
                cnt += 1
            if masume[h][w-1] == '#' :
                cnt += 1
            if masume[h][w+1] == '#' :
                cnt += 1
            if cnt % 2 != 0:
                jedge = "No"
                break

print(jedge)
