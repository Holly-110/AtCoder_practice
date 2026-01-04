N, M = map(int, input().split())

R, C = map(int, input().split())
registered_pairs = []
registered_pairs.append([R, C, R + 1, C + 1])
count = 1

for i in range(1, M):
    R, C = map(int, input().split())

    new_r1, new_c1, new_r2, new_c2 = R, C, R + 1, C + 1
    is_overlap = False
    print(new_r1, new_c1, new_r2, new_c2)
    
    for existing_pair in registered_pairs:
        ex_r1, ex_c1, ex_r2, ex_c2 = existing_pair[0], existing_pair[1], existing_pair[2], existing_pair[3]
        
        if not (new_r2 < ex_r1 or new_r1 > ex_r2 or 
                new_c2 < ex_c1 or new_c1 > ex_c2):
            
            is_overlap = True 
            break             
            
    if not is_overlap:
        registered_pairs.append([new_r1, new_c1, new_r2, new_c2])
        count += 1
        
print(count)