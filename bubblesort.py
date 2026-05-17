def bubble_sort(arr):
    n = len(arr)
    
    # ヘッダーの出力
    print(f"{'j(確定対象)':<7} | {'i(比較添字)':<7} | {'配列[i]':<5} | {'配列[i+1]':<7} | {'[i] > [i+1]':<11} | {'入れ替え':<5} | 配列の状態 (処理後)")
    print("-" * 95)
    
    # 初期状態の出力
    print(f"{'-':<11} | {'-':<11} | {'-':<7} | {'-':<9} | {'-':<11} | {'-':<9} | {arr}")
    
    # j ← 要素数 - 1
    j = n - 1
    
    # ループ1
    while j > 0:
        # i ← 0
        i = 0
        
        # ループ2
        while i < j:
            val_i = arr[i]
            val_i_plus_1 = arr[i+1]
            condition = "Yes" if val_i > val_i_plus_1 else "No"
            swapped = "有" if val_i > val_i_plus_1 else "なし"
            
            # 比較と入れ替え
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                
            # 途中経過の出力
            print(f"{j:<11} | {i:<11} | {val_i:<7} | {val_i_plus_1:<9} | {condition:<11} | {swapped:<9} | {arr}")
            
            # i ← i + 1
            i += 1
            
        # 確定した要素の表示
        if j == 1:
            print(f"{'':<11} | {'':<11} | {'':<7} | {'':<9} | {'':<11} | {'':<9} | ※ {arr[j]} と {arr[0]} が確定")
        else:
            print(f"{'':<11} | {'':<11} | {'':<7} | {'':<9} | {'':<11} | {'':<9} | ※ 末尾 {arr[j]} が確定")
            print(f"{'---':<11} | {'---':<11} | {'---':<7} | {'---':<9} | {'---':<11} | {'---':<9} | ---")
            
        # j ← j - 1
        j -= 1

if __name__ == "__main__":
    # 画像にあるデータを再現
    data = [25, 36, 11, 32, 81, 15, 52]
    bubble_sort(data)