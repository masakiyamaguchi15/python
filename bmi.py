# bmi.py

print("肥満度算出")

# 入力を受け取る
weight = float(input("体重(kg)=>"))
height = float(input("身長(m)=>"))

# BMIの計算 (体重 / 身長の2乗)
bmi = weight / (height ** 2)

# BMIの表示
print(f"BMI {bmi}")

# 肥満度の判定 (日本肥満学会の基準)
if bmi < 18.5:
    result = "低体重"
elif bmi < 25.0:
    result = "普通体重"
elif bmi < 30.0:
    result = "肥満（１度）"
elif bmi < 35.0:
    result = "肥満（２度）"
elif bmi < 40.0:
    result = "肥満（３度）"
else:
    result = "肥満（４度）"

# 判定結果の表示
print(result)