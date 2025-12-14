#全探索のパターン3：「答え」を全探索する
#判定する部分に関数を用いると、実装とデバッグが楽になることがある
#答えの通り数が現実的な数になるのか見積もる(10^9)

def solve(border):
    cnt = 0
    for i in range(N):
        if A_list[i] > border:
            cnt += 1
        else:
            cnt = 0
        if cnt >= P:
            return False
    return True
    

P, N = map(int, input().split())
A_list = list(map(int, input().split()))
for i in range(41):
    if solve(i):
        print(i)
        exit()
