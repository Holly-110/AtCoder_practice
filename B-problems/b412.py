S = list(input())
T = list(input())

flag = False

for i in range(1, len(S)):
    if S[i].upper():
        for t in T:
            if S[i - 1] == t:
                flag = True
            