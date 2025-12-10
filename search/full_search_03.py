#全探索のパターン２：あり得るものを全通り試す
#全体の通り数に気を遣う(10^9)
#for文を用いた多重ループで実装することができる問題か確認する

N = int(input())
x = int(input())

ans = 0

for i in range(1, N+1):
    for j in range(i + 1, N + 1):
        for k in range(j + 1, N + 1):
            if (i + j + k) == x:
                ans += 1

print(ans)
                