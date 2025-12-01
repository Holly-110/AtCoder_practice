H, W = map(int, input().split())
<<<<<<< HEAD

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
=======
# 上下左右に 1 マスずつ白マスを広げたマス目を用意する
field = ['.' * (W + 2)] + ['.' + input() + '.' for i in range(H)] + ['.' * (W + 2)]
for i in range(1, H + 1):
    for j in range(1, W + 1):
        black_count = 0 # 周囲の黒マスの個数
        if field[i - 1][j] == '#':
            black_count += 1
        if field[i][j - 1] == '#':
            black_count += 1
        if field[i + 1][j] == '#':
            black_count += 1
        if field[i][j + 1] == '#':
            black_count += 1
        
        if field[i][j] == '#' and black_count != 2 and black_count != 4:
            # 条件を満たさないマスがあったら、No を出力して終了
            print('No')
            exit(0)
# すべてのマスが条件を満たすので、Yes を出力して終了
print('Yes')
>>>>>>> 6d7cf7fdf34e13f8860fff0a66db17311ac11287
