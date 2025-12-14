#全探索のパターン１：問題文の通りに全探索する
#関数を用いて実装すると、実装とデバッグが楽になることがある
#Nが10^9以上など大きい場合、この手法では間に合わないことがあるので、通り数の見積もりに気を遣う

def solve(n):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
    if cnt == 8:
        return True
    else:
        return False

N = int(input())
ans = 0
for i in range(1, N + 1, 2):
    if solve(i):
        ans += 1

print(ans)