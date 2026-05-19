class Station():
    def __init__(self,eki,name): 
        self.駅 = eki
        self.駅名 = name 

#ここでインスタンス化（実体化）している。
st1 = Station('M16','梅田')
st2 = Station('M17','難波')
st3 = Station('M18','天王寺')

print('駅番号',st1.駅)
print('駅名',st1.駅名)
print('駅番号',st2.駅)
print('駅名',st2.駅名)