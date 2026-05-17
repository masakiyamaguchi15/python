import math

def findPrimeNumbers(maxNum: int) -> list[int]:
    """
    引数で与えられた整数以下の、全ての素数だけを格納した配列を返す関数。
    ここで、引数に与える整数は2以上である。
    """
    pnList = []  # 要素数0の配列
    
    # i を 2 から maxNum まで 1 ずつ増やす (a = maxNum)
    for i in range(2, maxNum + 1):
        divideFlag = True
        
        # iの正の平方根の整数部分が2未満のときは、繰返し処理を実行しない
        limit = int(math.sqrt(i))
        print(limit)
        
        # j を 2 から iの正の平方根の整数部分 まで 1 ずつ増やす
        for j in range(2, limit + 1):
            if i % j == 0:  # b = (i % j == 0) または (i が j で割り切れる)
                divideFlag = False
                break  # αの行から始まる繰返し処理を終了する
                
        if divideFlag:
            pnList.append(i)
            
    return pnList

def main():
    # 動作確認 (例: 30以下の素数を求める)
    print(f"findPrimeNumbers(30): {findPrimeNumbers(1000)}")

if __name__ == "__main__":
    main()