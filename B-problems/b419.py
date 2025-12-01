Q = int(input())
answer = []

for q in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        answer.append(query[1])
    elif query[0] == 2:
        if len(answer) >= 1:
            min_value = min(answer)
            print(min_value)
            answer.remove(min_value)
