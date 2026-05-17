print("肥満度算出")
weight = float(input("体重(kg)=>"))
height = float(input("身長(m)=>"))
bmi = weight / (height ** 2)
print("BMI",bmi)

if bmi < 18.5:
    print( "低体重")
if bmi>= 18.5 and bmi < 25:
    print("普通体重")
if bmi>= 25 and bmi < 30:
    print("肥満（1 度）")
if bmi>= 30 and bmi < 35:
    print("肥満（2 度）")
if bmi>= 35 and bmi < 40:
    print("肥満（3 度）")
if bmi>= 40:
    print("肥満（4 度）")
