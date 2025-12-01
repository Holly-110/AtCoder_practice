N, M = map(int, input().split())
S = []
S_list = [] 
point = [0] * N

for i in range(N):
    S.append(input())

for i in zip(*S_list):
    S_list.append("".join(i))
    
    

for s_str in S_list:
    cnt_0_x = 0
    cnt_1_y = 0
    for i in range(N):
        if s_str[i] == '0':
            cnt_0_x += 1
        elif s_str[i] == '1':
            cnt_1_y += 1
    
    if cnt_0_x == 0 or cnt_1_y == 0:
        point = [x+1 for x in point]
    elif cnt_0_x < cnt_1_y:
        for i in range(N):
            if s_str[i] == '0':
                point[i] += 1
    else :
        for i in range(N):
            if s_str[i] == '1':
                point[i] += 1

max_value = max(point)
max_index = [index+1 for index, value in enumerate(point)
             if value == max_value]

print(*max_index)
    

