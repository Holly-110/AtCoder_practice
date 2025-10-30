import sys

# 1. 入力の読み込み
try:
    N = int(input())
    A = list(map(int, input().split()))
except EOFError:
    # 入力がない場合のフォールバック（競技プログラミングでは通常不要）
    sys.exit()

# 2. ロジック本体

# Pの最終的な値を格納する配列を初期化
P = [0] * N 
# 既にAから値が割り当てられた要素 (1からN) を記録するセット
used_values = set() 
# A[i]が-1の位置 (Pの空き位置) のインデックスを記録
free_indices = []

# --- ステップ A: Pの確定要素を配置し、矛盾をチェック ---
for i in range(N):
    target_value = A[i]
    
    if target_value != -1:
        # 1. 範囲チェック (A[i]が1〜Nの範囲外でないか)
        if not (1 <= target_value <= N):
             print("No")
             sys.exit()
             
        # 2. 重複チェック (A[i]の値が既に他のP_kに割り当てられていないか)
        if target_value in used_values:
            print("No")
            sys.exit()
            
        # 矛盾がなければ、P[i]に値を確定させる
        P[i] = target_value
        used_values.add(target_value)
    
    else: # A[i] == -1 の場合、P[i]は空き
        free_indices.append(i)


# --- ステップ B: 残りの空きに値を埋める ---
# 1からNまでの全ての値のうち、まだ使われていない値をリストアップ
all_values = set(range(1, N + 1))
remaining_values = sorted(list(all_values - used_values)) # 昇順にしておく

# Pの空いている位置 (A[i] == -1 の場所) に、残りの値を順番に埋める
# free_indices と remaining_values の要素数は一致しているはず
if len(free_indices) != len(remaining_values):
    # ロジック上、このエラーは発生しないはずだが、念のため
    print("No")
    sys.exit()

for i, value in zip(free_indices, remaining_values):
    P[i] = value


# 3. 結果の出力
print("Yes")
# 整数のリストPをスペース区切りの文字列に変換して出力
P_str = map(str, P)
print(" ".join(P_str))