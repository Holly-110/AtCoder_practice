H, W = map(int, input().split())
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