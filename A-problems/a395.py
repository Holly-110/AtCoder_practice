N = int(input())
A_list = list(map(int, input().split()))

is_ok = True

for i in range(N - 1):
    if A_list[i] >= A_list[i + 1]:
        print("No")
        is_ok = False
        break

if is_ok:
    print("Yes")