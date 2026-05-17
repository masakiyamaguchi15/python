# メインプログラム (例: main.py)

from mycalc import add, subtract, multiply, divide


# ユーザーからの入力を受け取る
num1 = int(input("=>"))
num2 = int(input("=>"))

# mycalcモジュールの関数を呼び出して計算する
sum_result = add(num1, num2)
difference_result = subtract(num1, num2)
product_result = multiply(num1, num2)
quotient_result = divide(num1, num2)

# 結果を出力する
print("和", sum_result)
print("差", difference_result)
print("積", product_result)
print("商", quotient_result)