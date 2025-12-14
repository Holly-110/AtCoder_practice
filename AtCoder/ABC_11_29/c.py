from math import fabs

T = int(input())
result = []
result_list = []

def jedge(H, t, max, min) :
    max_gap = max - H
    min_gap = min - H
    if max_gap > min_gap:
        if (min_gap >= 0) and (fabs(min_gap) <= t) :
            return True
        else:
            return False
    elif max_gap < min_gap:
        if (max_gap >= 0) and (fabs(max_gap)) :
            return True
        else:
            return False
    else:
        if (max_gap >= 0) and (fabs(max_gap)) :
            return True
        else:
            return False
    
               
for i in range(T):
    result = []
    N, H = map(int, input().split())
    for i in range(N):
        t, l, u = map(int, input().split())
        result.append(jedge(H, t, l, u))
    result_list.append(all(result))
    print(result)

for i in result_list:
    if i == True:
        print("Yes")
    else :
        print("No")
    
    