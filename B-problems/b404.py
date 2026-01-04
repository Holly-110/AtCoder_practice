def mismatch_cnt(s, t, n):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if s[i][j] != t[i][j]:
                cnt += 1
    return cnt

def right_90(s, n):
    new_grid = [["" for _ in range(n)] for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            new_grid[col][(n - 1) - row] = s[row][col]
    
    return ["".join(line) for line in new_grid]
                


N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

min_operations = float('inf')

for rot_cnt in range(4):
    color_cnt = mismatch_cnt(S, T, N)
    
    total_cnt = color_cnt + rot_cnt
    
    if total_cnt < min_operations:
        min_operations = total_cnt
    
    S = right_90(S, N)

print(min_operations)