N = int(input())

def f(a):
    total = 0
    a_str = str(a)
    for char in a_str:
        total += int(char)
    return total

A_list = []
A_list.append(1) 
for i in range(N-1):
    A_list.append(A_list[i] + f(A_list[i]))

print(A_list[-1])