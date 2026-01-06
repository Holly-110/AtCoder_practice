def get_happy_sum(n_str):
    """各桁の2乗和を計算して文字列で返す"""
    total = 0
    for char in n_str:
        total += int(char) ** 2
    return str(total)

N = input()
history = set()

while True:
    N = get_happy_sum(N)
    if N == '1':
        print("Yes")
        exit()
    if N in history:
        print("No")
        exit()
    history.add(N)