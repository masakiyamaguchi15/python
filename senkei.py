array_size = 10
target=38

# 【間違い1】 リストは {} ではなく [] で定義します
# {} で作ると「セット」となり、my_array[i] のようにインデックスでアクセスできません
my_array = [30, 20, 50, 40, 48, 72, 38, 49, 99, 100]
print("配列:", my_array)

print("探索する値:", target)

for i in range(array_size):
    if my_array[i] == target:
        print("探索成功")
        break   # 見つかった場合はループを終了します
else:
    print("探索失敗")
