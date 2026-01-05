from collections import deque

Q = int(input())

que = deque()

for i in range(Q):
    query = input()
    if query == '2':
        print(que[0])
        que.popleft()
    else:
        q1, q2 = query.split()
        que.append(q2)