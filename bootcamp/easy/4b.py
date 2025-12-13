N = int(input())

ans = N / 1.08

if (N % 1.08) == 0:
    print(int(ans))
else:
    print(":(")
