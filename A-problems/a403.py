N = int(input())
A_list = list(map(int, input().split()))

sum = 0

for i in range(N):
    if (i+1) / 2 != 0:
        sum += A_list[i]

print(sum)