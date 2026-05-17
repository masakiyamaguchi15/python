array_size = 10
target=98
j=0

# 【間違い1】 リストは {} ではなく [] で定義します
# {} で作ると「セット」となり、my_array[i] のようにインデックスでアクセスできません
my_array = [30, 20, 50, 40, 48, 72, 38, 49, 99, 100]
print("配列:", my_array)

print("探索する値:", target)

for i in range(array_size):
    if my_array[i] == target:
        j=1
        break   # 見つかった場合はループを終了します
if j==0:
    print("探索失敗")
if j==1:
    print("探索成功")
