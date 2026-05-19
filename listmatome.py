# リストを作成するコード
my_list = ["pikachu", "kabigon", "pocchama", "hitokage", "dialga100", "palkia100"]
print("リスト:", my_list)

# インデックスを使ってリスト要素を指定するコード
print("インデックス0の要素:", my_list[0])
print("インデックス2の要素:", my_list[2])

# スライスを使ってリストの部分を指定するコード
print("スライス [1:3]:", my_list[1:3])  # インデックス1から2までの要素
print("スライス [:2]:", my_list[:2])   # 最初からインデックス1までの要素
print("スライス [3:]: ", my_list[3:])   # インデックス3から最後まで

# for 文を使って、リストの全要素にアクセスするコード
print("リストの全要素1:")
for element in my_list:
    print(element)

# for 文を使って、リストの全要素にアクセスするコード2
print("リストの全要素2:")
for i in range(0,len(my_list)):
    print(my_list[i])
