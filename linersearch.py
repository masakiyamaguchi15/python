# 線形探索の例
my_array = [1024, 2241, 1866, 2132, 554, 732, 11357, 33, 839, 6826]
target=0
i=0

print("配列:", my_array)

target=int(input("=>"))

while i<10:
    if my_array[i] == target:
        break  # 見つかった場合はループを終了します
    i+=1

if i<10:
    print("探索成功")
else:
    print("探索失敗")

