class Station():
    def __init__(self,駅番号,駅名): 
        self.駅番号 = 駅番号
        self.駅名 = 駅名 

#ここでインスタンス化（実体化）している。
st1 = Station('M16','梅田')
st2 = Station('M17','難波')

print('駅番号',st1.駅番号)
print('駅名',st1.駅名)
print('駅番号',st2.駅番号)
print('駅名',st2.駅名)