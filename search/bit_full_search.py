import sys

def solve():
    try:
        N, W = map(int, input().split())
        a_list = list(map(int, sys.stdin.readline().split()))
    except:
        return()
    
    exist = False
    
    for bit in range(1 << N):
        #部分集合に対応する総和を計算
        current_sum = 0
        
        for i in range(N):
            
            #bitのi番目にフラグが立っているかを判定
            if (bit >> i) & 1:
                current_sum += a_list[i]
        
        if current_sum == W:
            exist = True
            break
    
    if exist:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()
                

    