print('5科目の得点を入力してください')

counter = 0
total = 0
while counter < 5:
    score = int(input('score=>'))
    total += score
    counter += 1

average = total / 5
print("平均",average)
