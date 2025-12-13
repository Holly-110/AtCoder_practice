N, A, B = map(int, input().split())
S = list(input())

cnt = 0
b_cnt = 0

for i in range(len(S)):
    if S[i] == 'a' and (A + B) > cnt:
        print("Yes")
        cnt += 1
    elif S[i] == 'b':
        b_cnt += 1
        if (A + B) > cnt and b_cnt <= B:
            print("Yes")
            cnt += 1
        else:
            print("No")
    else:
        print("No")
