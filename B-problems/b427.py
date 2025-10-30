S = input()

S_list = str(S)
counts = {}
target = ''

for char in S_list:
    counts[char] = counts.get(char, 0) + 1

for char, count in counts.items():
    if count == 1:
        target = char
    
print(target)