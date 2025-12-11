S = list(input())

t_list = []

for i in range(len(S)):
    if S[i] == 't':
        t_list.append(i)

for i in range(len(t_list)):
    