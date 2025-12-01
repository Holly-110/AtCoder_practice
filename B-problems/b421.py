X, Y = map(int, input().split())

a_list = []
a_list.append(X)
a_list.append(Y)

for i in range(1,9):
    a_list.append(a_list[i] + a_list[i - 1])
    tmp = str(a_list[i + 1])[::-1]
    a_list[i + 1] = int(tmp)
    
print(a_list[9])
        