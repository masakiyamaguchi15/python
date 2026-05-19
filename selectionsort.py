# 配列を初期化
array = [25, 36, 11, 32, 81, 46, 52]

# ソート完了の配列を出力
print("ソート前:", array)

# 要素数を取得
n = len(array)

# ループ1 (i < 要素数 - 1)
# Pythonの range(n - 1) は 0 から n-2 まで繰り返します
for i in range(n - 1):
    # ループ2 (j < 要素数)
    # フローチャートの j ← i + 1 に対応し、i+1 から n-1 まで繰り返します
    for j in range(i + 1, n):
        #print("ソート結果:", array)
        print("ソート中:", array)
        # 判定：配列[i] > 配列[j]
        if array[i] > array[j]:
            # Yesの場合の処理
            
            # 退避領域を使った値の交換
            temp = array[i]      # 退避領域 ← 配列[i]
            array[i] = array[j]  # 配列[i] ← 配列[j]
            array[j] = temp      # 配列[j] ← 退避領域

# ソート完了後の配列を出力
print("ソート後:", array)