# ユーザーから数値の入力を促す
num = float(input("数値を入力してください: "))

# 数値が正の数かどうかを判定
if num > 0:
    print("数値:", num, "は正の数です")
elif num < 0:
    print("数値:", num, "は負の数です")
else:
    print("数値:", num, "はゼロです")
