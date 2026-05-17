counter = 0
total = 0
max = 0
min = 0
scores = []  # 入力されたスコアを保存するための空リストを用意

while counter < 5:
    num = int(input('score=>'))
    scores.append(num)  # 入力された値をリストに追加
    
    if counter == 0:
        max = num
        min = num
    else:
        if num > max:
            max = num
        if num < min:
            min = num
    total += num
    counter += 1

# リストを小さい順に並び替える
scores.sort()

# 今回は入力数が5個と決まっているため、インデックス2（3番目）が中央値
median = scores[2]

print("平均", total / 5)
print("最大値", max)
print("最小値", min)
print("中央値", median)