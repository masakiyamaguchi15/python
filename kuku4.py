def kuku():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i} × {j} = {i * j}")
        print()  # 各段の後に空行を入れる

if __name__ == "__main__":
    kuku()