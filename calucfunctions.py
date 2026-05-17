# calcfunctions.py

def add(x, y):
  """2つの数値を加算します。"""
  return x + y

def subtract(x, y):
  """2つの数値を減算します (x - y)。"""
  return x - y

def multiply(x, y):
  """2つの数値を乗算します。"""
  return x * y

def divide(x, y):
  """2つの数値を割り、小数点以下を切り捨てた結果を返します。"""
  if y == 0:
    return "Error: Division by zero"  # ゼロ除算エラー処理
  return x // y

num1 = int(input("=>"))
num2 = int(input("=>"))

sum_result = add(num1, num2)
difference_result = subtract(num1, num2)
product_result = multiply(num1, num2)
quotient_result = divide(num1, num2)

print("和",sum_result)
print("差",difference_result)
print("積",product_result)
print("商",quotient_result)
