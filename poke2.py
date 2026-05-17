# poke2.py

class Monster:
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp = hp



# インスタンス化
coratta = Monster("コラッタ", 3, 30 )
print(f"名前は {coratta.name} です。")
print(f"レベルは {coratta.level} です。")
print(f"HPは {coratta.hp} です。")


