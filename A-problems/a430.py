A, B, C, D = map(int, input().split())

if C >= A:
    if D < B:
        print("Yes")
        exit()
        
print("No")