import sys

def solve():
    # 入力を読み込む
    s = sys.stdin.readline().strip()
    n = len(s)
    
    # C++の long double ans = 0 に相当（Pythonのfloatは高精度）
    ans = 0.0
    
    # 1つ目の 't' を探すループ
    for i in range(n):
        if s[i] != 't':
            continue
            
        # 2つ目の 't' を探すループ（i+2 以降を探索）
        for j in range(i + 2, n):
            if s[j] != 't':
                continue
            
            # i番目から j番目の範囲にある 't' の個数を数える (x)
            # C++の ki ループに相当
            substring = s[i:j+1]
            x = substring.count('t')
            
            # 全体の長さ (len)
            length = j - i + 1
            
            # 指標の計算
            # 0除算を避けるため length > 2 を確認（j >= i + 2 なので基本OK）
            if length > 2:
                item = float(x - 2) / float(length - 2)
                if item > ans:
                    ans = item

    # 小数点以下17位まで固定精度で出力
    print(f"{ans:.17f}")

if __name__ == "__main__":
    solve()