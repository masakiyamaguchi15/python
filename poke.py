# poke.py

class Monster:
    def __init__(self, name, level, waza):
        self.name = name
        self.level = level
        self.waza = waza

    def self_introduce(self):
        print(f"名前は {self.name} です。")
        print(f"レベルは {self.level} です。")
    
    def waza_attack(self):
        print(f"{self.name} の技は {self.waza} です。")


# インスタンス化
fushigidane = Monster("フシギダネ", 1, "ハートプラント")
hitokage = Monster("ヒトカゲ", 100, "かえんほうしゃ")
zenigame = Monster("ゼニガメ", 100, "ハイドロポンプ")

# メソッド実行
fushigidane.self_introduce()
fushigidane.waza_attack()

hitokage.self_introduce()
hitokage.waza_attack()

zenigame.self_introduce()
zenigame.waza_attack()