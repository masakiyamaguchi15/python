# poke.py

class Monster:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def self_introduce(self):
        print(f"名前は {self.name} です。")
        print(f"レベルは {self.level} です。")


# インスタンス化
fushigidane = Monster("フシギダネ", 1)

# メソッド実行
fushigidane.self_introduce()
