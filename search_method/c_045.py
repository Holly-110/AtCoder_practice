#bit全探索の基礎問題

import sys

s_list = input()
N = len(s_list)

all_sum = 0

for bit in range(1 << (N - 1)):
    s = s_list[0]
    for i in range(N - 1):
        if (bit >> i) & 1:
            all_sum += int(s)
            s = ""
        s += s_list[i + 1]
    all_sum += int(s)

print(all_sum)




            

