Q = int(input())
Q_list = []
A = []

for i in range(Q):
    Q_list.append(input())

for q in Q_list:
    q_list = list(map(int, q.split()))
    if q_list[0] == 1:
        x = q_list[1]
        A.append(x)
    elif q_list[0] == 2:
        k = q_list[1]
        print(A[-k])