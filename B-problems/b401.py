N = int(input())

login = False
cnt = 0

for i in range(N):
    s = input()
    if s == "login":
        login = True
    elif s == "logout":
        login = False
    elif s == "public":
        continue
    else:
        if login == False:
            cnt += 1

print(cnt)