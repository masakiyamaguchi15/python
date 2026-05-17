def triangle_type(a, b, c):
  """
  三角形の3辺の長さを入力とし、三角形の種類を表示する関数。

  Args:
    a: 1つ目の辺の長さ (数値)
    b: 2つ目の辺の長さ (数値)
    c: 3つ目の辺の長さ (数値)

  Returns:
    文字列: 三角形の種類 ("不等辺三角形", "二等辺三角形", "正三角形")。
            不正な入力の場合 ("不正な三角形") を返す。
  """

  if a + b <= c or a + c <= b or b + c <= a:
    return "不正な三角形"  # 三角形の成立条件を満たさない

  if a == b and b == c:
    return "正三角形"
  elif a == b or a == c or b == c:
    return "二等辺三角形"
  else:
    return "不等辺三角形"


# テストケースの定義 (判定条件網羅)

test_cases = [
    # 1. 不正な三角形のテスト（成立条件を満たさない場合）
    (1, 2, 10),  # a + b <= c の場合
    (1, 10, 2),  # a + c <= b の場合
    (10, 1, 2),  # b + c <= a の場合

    # 2. 正三角形のテスト (a == b == c)
    (5, 5, 5),

    # 3. 二等辺三角形のテスト (いずれかの2辺が同じ)
    (5, 5, 3),  # a == b
    (5, 3, 5),  # a == c
    (3, 5, 5),  # b == c

    # 4. 不等辺三角形のテスト (全て異なる長さ)
    (2, 3, 4),
    (1, 2, 3), # ギリギリ成立するケースも確認
]


# テストの実行と結果の検証
for a, b, c in test_cases:
  expected = ""
  if a + b <= c or a + c <= b or b + c <= a:
    expected = "不正な三角形"
  elif a == b and b == c:
      expected = "正三角形"
  elif a == b or a == c or b == c:
      expected = "二等辺三角形"
  else:
      expected = "不等辺三角形"

  actual = triangle_type(a, b, c)
  print(f"Input: ({a}, {b}, {c}) - Expected: {expected} - Actual: {actual}")
  assert actual == expected, f"Test failed for input ({a}, {b}, {c})"

print("すべてのテストケースが成功しました!")
