N = int(input())
A_list = list(map(int, input().split()))

ans = 0
flag = True

while (flag):
    if N-1 <= ans:
        print(N)
        exit()
    else:
        num = A_list[ans]
    
    if num == 1:
        print(ans+1)
        exit()
    ans += num-1