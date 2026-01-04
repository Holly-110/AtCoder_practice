W, B = map(int, input().split())

W = W * 1000
cnt = 0

while W >= 0:
    W = W - B
    cnt += 1 
    
print(cnt)