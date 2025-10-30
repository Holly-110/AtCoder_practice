N, M = map(int, input().split())
S = list(map(int, input().split()))

S_total = sum(S)

judge = "No"

for i in S:
    if (S_total - i) == M:
        judge = "Yes"

print(judge)