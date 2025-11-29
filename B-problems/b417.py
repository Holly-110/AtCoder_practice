N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for m in range(M):
    for n in range(len(A)):
        if B[m] == A[n]:
            A.remove(A[n])
            break

print(*A)