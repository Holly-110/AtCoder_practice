T = input()
U = input()

indexes = [x for x in range(len(T)) if T[x] == '?']
alphabets = [chr(ord("a") + i) for i in range(26)]

for a in alphabets:
    for b in alphabets:
        for c in alphabets:
            for d in alphabets:
                S = list(T)
                S[indexes[0]] = a
                S[indexes[1]] = b
                S[indexes[2]] = c
                S[indexes[3]] = d
                S = "".join(S)
                if U in S:
                    print("Yes")
                    exit()

print("No")