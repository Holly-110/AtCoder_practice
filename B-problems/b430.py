N, M = map(int, input().split())

matrix = []

for i in range(N):
    row = list(input().split())
    matrix.append(row)

cnt = N - M
output_rows = []
for i in range(M):
    row_slice = matrix[i][0:M]

for i in range(cnt):
    