class Station():  # ← 'C'を小文字の'c'に修正
    def __init__(self, 駅番号, 駅名):
        self.駅番号 = 駅番号
        self.駅名 = 駅名
        
    def 駅情報出力(self):
        print('駅情報:', self.駅名, self.駅番号)