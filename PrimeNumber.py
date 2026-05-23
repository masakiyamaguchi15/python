import math

pnList = []  # 要素数0の配列

maxNum = int(input("1以上の整数を入力してください: "))

# i を 2 から maxNum まで 1 ずつ増やす (a = maxNum) maxNumは+1する（2からmaxNumまでという意味になる）
for i in range(2, maxNum + 1):
    divideFlag = True    
    # iの正の平方根の整数部分が2未満のときは、繰返し処理を実行しない
    limit = int(math.sqrt(i))
    print("i=", i)

# j を 2 から iの正の平方根の整数部分 まで 1 ずつ増やす  limit + 1 は+1する(2からlimitまでという意味になる)
    for j in range(2, limit+1):
        if i % j == 0:  # i÷jの余りが0と等しい
            divideFlag = False #割り切れたら素数でないので Falseにする
            break  # αの行から始まる繰返し処理を終了する
        print("j=", j)
    
    print("divideFlag=", divideFlag)                

    if divideFlag==True: #Trueならiの値が平方根まで変化した場合にどの数字でも割り切れなかったと考える（素数である）
        pnList.append(i) #pnLintに素数を追加する
            
print(pnList)


