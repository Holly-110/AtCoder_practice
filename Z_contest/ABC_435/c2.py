N = int(input())
A_list = list(map(int, input().split()))

i = A_list[0]

if i == 1:
    print(i+1)
    exit()

while (True):
    i += A_list[i - 1]
    if i >= N-1:
        print(N)
        exit()
    else:
        if A_list[i] == 1:
            print(i+1)
            exit()
    
    