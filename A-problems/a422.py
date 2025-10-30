I, J = map(int, input().split("-"))

if J < 8:
    J += 1
elif (I < 8) and (J == 8):
    I += 1
    J = 1 
else:
    I = 8
    J = 8

print(f"{I}-{J}")
