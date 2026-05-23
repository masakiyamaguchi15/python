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
        print(f"{self.name} の必殺技は {self.waza} です。")

# インスタンス化
fushigidane = Monster("フシギダネ", 1, "ハートプラント")
hitokage = Monster("ヒトカゲ", 100, "かえんほうしゃ")
zenigame = Monster("ゼニガメ", 100, "ハイドロポンプ")
myu2 = Monster("ミュウツー（色違い）",100,"シャドーボール")

array = [fushigidane,hitokage,zenigame,myu2]

for i in array:
    i.self_introduce()
    i.waza_attack()
