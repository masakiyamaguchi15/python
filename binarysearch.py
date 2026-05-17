# 使用例
array = [100, 100, 101, 102,102,105,121,132,150,186,213]
target = int(input("=>"))


low = 0
high = len(array) - 1
mid = (low + high) // 2


while low <= high:
    if array[mid] == target:
      break
    elif target < array[mid]:
      high = mid - 1
    else:
      low = mid + 1
    mid = (low + high) // 2


if low <= high:
  print("探索成功")
  print("low",low)
  print("high",high)
  print("mid",mid)
else:
  print("探索失敗")
  print("low",low)
  print("high",high)
  print("mid",mid)

