import argparse

def print_kuku():
    """九九の表を整形して出力します。"""
    # ヘッダー部分
    print("  |", end="")
    for i in range(1, 10):
        print(f"{i:3}", end="")
    print("\n--+" + "-" * 27)
    
    # データ部分
    for i in range(1, 10):
        print(f"{i} |", end="")
        for j in range(1, 10):
            print(f"{i * j:3}",end="")
        print()

def main():
    parser = argparse.ArgumentParser(description="九九表を出力するCLIアプリ")
    # 今回は特に引数を取らないシンプルな作りとします
    # parser.parse_args()
    
    print_kuku()

if __name__ == "__main__":
    main()
