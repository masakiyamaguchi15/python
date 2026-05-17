# 配列を初期化
array = [25, 36, 11, 32, 81, 15, 52]

# 要素数を取得
n = len(array)

# i ← 0
i = 0

# ループ1 (i < 要素数)
while i < n:
    
    # j ← i - 1
    j = i - 1
    
    # ループ2 (j ≧ 0 かつ 配列[j] > 配列[j+1])
    # Pythonでは「かつ」を and で表現します
    while j >= 0 and array[j] > array[j + 1]:
        
        # 退避領域を使った値の交換
        temp = array[j]          # 退避領域 ← 配列[j]
        array[j] = array[j + 1]  # 配列[j] ← 配列[j+1]
        array[j + 1] = temp      # 配列[j+1] ← 退避領域
        
        # j ← j - 1
        j = j - 1
        
    # i ← i + 1
    i = i + 1
    print("ソート結果:", array)

# ソート完了後の配列を出力
print("ソート結果:", array)