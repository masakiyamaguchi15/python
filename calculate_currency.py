# 入力例
amount = int(input("金額を入力してください: "))

# 金種リスト（2千円札は除外）
denominations = [10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

for d in denominations:
    count = amount // d    # 枚数を計算（整数の商）
    amount = amount % d     # 残り金額を更新（余り）
    print(f"{d}円: {count}枚")