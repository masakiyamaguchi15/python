import sys

# コマンドライン引数を取得（プログラム名を除く）
args = sys.argv[1:]

# 1. 合計を保持する変数を「0」で初期化する
total = 0

# 2. 引数のリストから、値を一つずつ取り出してループ処理する
for arg in args:
    # 3. 取り出した値（文字列）を整数(int)に変換する
    num = int(arg)
    
    # 4. 変換した数値を、変数totalに足していく
    total = total + num
    # ※ total += num と書いても同じ意味です

# 最終的な合計を表示
print(f"合計： {total}")