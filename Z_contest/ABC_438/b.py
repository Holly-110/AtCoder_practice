N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

def cnt(s, t):
    while True:
        cnt = 0
        for i in range(len(t)):
            while s[i] != t[i]:
                cnt += 1
                if t[i] == 9:
                    t[i] = 0
                else :
                    t[i] += 1
        return cnt

result = []
S_list = []
for i in range(0, len(T), len(S)):
    S_list.append(S[i:i+len(T)])
for i in range(len(T)):
    if i+len(T) > len(S):
        break
    else:
        result.append(cnt(S[i:i+len(T)], T))

# print(min(result))
print(result)