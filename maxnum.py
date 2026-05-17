# 3つの数値の入力を促す
num1 = int(input("1つ目の数値を入力してください: "))
num2 = int(input("2つ目の数値を入力してください: "))
num3 = int(input("3つ目の数値を入力してください: "))

# 最大値を求める (if文を使用)
if num1 >= num2 and num1 >= num3:
    max_num = num1
elif num2 >= num1 and num2 >= num3:
    max_num = num2
else:
    max_num = num3

# 最大値を出力する
print("最大の数値は:", max_num)
