class Station():  # ← 'C'を小文字の'c'に修正
    def __init__(self, 駅番号, 駅名):
        self.駅番号 = 駅番号
        self.駅名 = 駅名
        
    def 駅情報出力(self):
        print('駅情報:', self.駅名, self.駅番号)

#ここでインスタンス化（実体化）している。
st1 = Station('M16','梅田')
st2 = Station('M17','難波')

st1.駅情報出力()
st2.駅情報出力()

