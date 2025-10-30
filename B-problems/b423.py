N = int(input()) + 1
L = list(map(int, input().split()))

room_key = {}
for i in range(1, len(L)+1):
    if L[i-1] == 0:
        room_key[i] = True
    else :
        room_key[i] = False

arrive_room = set()
arrive_room.add(0)
arrive_room.add(N)

for room_num, key in room_key.items():
    if key == True:
        arrive_room.add(room_num)
    else:
        break

for room_num, key in reversed(room_key.items()):
    if key == True:
        arrive_room.add(room_num)
    else:
        break

print(N - len(arrive_room))
