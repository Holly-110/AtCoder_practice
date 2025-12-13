N = int(input())

for i in range(N, 920):
    str_i = str(i)
    ans = int(str_i[0]) * int(str_i[1])
    str_ans = str(ans)
    if ans == int(str_i[2]):
        print(i)
        exit()
    