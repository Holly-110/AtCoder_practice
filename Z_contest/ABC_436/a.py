N = int(input())
S = input()

add = ''

for i in range(N - len(S)):
    add += 'o'

print(str(add) + S)