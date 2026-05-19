# ファイル名: maxmin.py
numbers = [0,0,0,0,0]
sum = 0

for i in range(0,5):
    num = int(input("5 回、整数値を入力してください。 number?=>"))
    numbers[i] = num
    sum = sum + num

maximum = numbers[0]
minimum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number

print("最大値:", maximum)
print("最小値:", minimum)
print("合計:", sum)
print("平均点:", sum/5)
