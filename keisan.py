# 単価を入力
try:
  price = int(input("単価を入力: "))
  print(f"入力された単価: {price}")
except ValueError:
  print("無効な入力です。整数を入力してください。")
  exit()

# 数量を入力
try:
  quantity = int(input("数量を入力: "))
  print(f"入力された数量: {quantity}")
except ValueError:
  print("無効な入力です。整数を入力してください。")
  exit()


# 金額を計算
total_price = price * quantity

# 金額を出力
print(f"金額: {total_price}")

# 終わり
print("プログラム終了")