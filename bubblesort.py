array = [25, 36, 11, 32, 81, 15, 52]
n = len(array)
print("ソート前:", array)

# ループ1 (j を n-1 から 1 まで 1 ずつ減らしながら繰り返す)
for j in range(n - 1, 0, -1):
    # ループ2 (i を 0 から j-1 まで 1 ずつ増やしながら繰り返す)
    for i in range(j):
        # 比較と入れ替え
        if array[i] > array[i+1]:
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp

print("ソート後:", array)