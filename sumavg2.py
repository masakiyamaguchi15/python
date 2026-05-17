# 合計を初期化
total = 0

# カウントを初期化
count = 0

# 3回ループ
while count < 3:
    # 数値を入力
    num = float(input("数値を入力してください: "))

    # 合計に加算
    total += num

    # カウントを増やす
    count += 1

# 平均を計算
average = total / count

# 合計を出力
print("合計は:", total)

# 平均を出力
print("平均は:", average)
