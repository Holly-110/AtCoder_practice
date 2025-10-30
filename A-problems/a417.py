N, A, B = input().split() #NはSの長さ
S = list(input())

A = int(A)
B = int(B)

del S[:A]

if B > 0:
    del S[-B:]

print("".join(S))