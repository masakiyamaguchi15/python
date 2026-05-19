# 2分探索例
array = [1002, 1005, 1010, 1024,1028,1052,1211,1322,1500,1866,2132]
target = int(input("=>"))

left = 0
right = len(array) - 1
pivot = (left + right) // 2

while left <= right:
    if array[pivot] == target:
      break
    elif target < array[pivot]:
      right = pivot - 1
    else:
      left = pivot + 1
    pivot = (left + right) // 2

if left <= right:
  print("探索成功")
  print("left",left)
  print("right",right)
  print("pivot",pivot)
else:
  print("探索失敗")
  print("left",left)
  print("right",right)
  print("pivot",pivot)

