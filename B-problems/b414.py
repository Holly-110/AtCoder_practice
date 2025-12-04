N = int(input())

target_text = ""

for i in range(N):
    C, L_str = input().split()
    L = int(L_str)
    for l in range(L):
        target_text += C
        if len(target_text) > 100:
            print("Too Long")
            exit()

print(target_text)
