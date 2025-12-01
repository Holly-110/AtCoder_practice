N = int(input())
T = list(input())
A = list(input())

judge = "No"

for i in range(N):
    if T[i] == 'o':
        if A[i] == 'o':
            judge = "Yes"
            break

print(judge)