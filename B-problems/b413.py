N = int(input())

S_list = []
output_set = set()

for i in range(N):
    S_list.append(input())

for i in range(N):
    for j in range(N):
        if i != j :
            text = S_list[i] + S_list[j]
            output_set.add(text)

print(len(output_set))