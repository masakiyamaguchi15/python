# 大域：整数型の配列
data = [2, 1, 3, 5, 4]

# sort関数の定義
def sort(first, last):
    # ピボットとして、範囲の中央の要素を選択します
    pivot = data[(first + last) // 2]
    i = first
    j = last
    
    print("pivot=",pivot," i=",i," j=",j)

    # 左右から探索して要素を入れ替えるループ
    while True:
        while data[i] < pivot:
            i += 1
        while pivot < data[j]:
            j -= 1
        if i >= j:
            break
        
        # data[i]とdata[j]の値を入れ替える
        temp=data[i]
        data[i]=data[j]
        data[j]=temp
        i += 1
        j -= 1
        
    # dataの全要素の値を要素番号の順に空白区切りで出力する /*** α ***/
    print(*(data))
    
    # 再帰呼び出し
    if first < i - 1:
        sort(first, i - 1)
    if j + 1 < last:
        sort(j + 1, last)

# 最初の呼び出し
sort(0, 4)
