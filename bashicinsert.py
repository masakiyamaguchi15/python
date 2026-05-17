def basic_insertion_sort(arr):
    n = len(arr)
    
    # ヘッダーの出力
    print(f"{'i(挿入対象)':<7} | {'j(比較位置)':<7} | {'配列[j]':<5} | {'配列[j+1]':<7} | {'j>=0 かつ [j]>[j+1]':<17} | {'入れ替え':<5} | 配列の状態 (処理後)")
    print("-" * 105)
    
    # 初期状態の出力
    print(f"{'-':<11} | {'-':<11} | {'-':<7} | {'-':<9} | {'-':<19} | {'-':<9} | {arr}")
    
    # i ← 0
    i = 0
    
    # ループ1
    while i < n:
        # j ← i - 1
        j = i - 1
        
        # ループ2の条件評価と途中経過の出力
        if j >= 0:
            while j >= 0:
                val_j = arr[j]
                val_j_plus_1 = arr[j+1]
                is_greater = val_j > val_j_plus_1
                
                if is_greater:
                    condition_str = f"Yes ({val_j} > {val_j_plus_1})"
                    swapped_str = "有"
                    
                    # 退避領域を使った値の交換
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
                    
                    # 途中経過の出力
                    print(f"{i:<11} | {j:<11} | {val_j:<7} | {val_j_plus_1:<9} | {condition_str:<19} | {swapped_str:<9} | {arr}")
                    
                    # j ← j - 1
                    j -= 1
                else:
                    condition_str = f"No ({val_j} > {val_j_plus_1})"
                    swapped_str = "なし"
                    
                    # 途中経過を出力してループ2を終了
                    print(f"{i:<11} | {j:<11} | {val_j:<7} | {val_j_plus_1:<9} | {condition_str:<19} | {swapped_str:<9} | {arr}")
                    break
                    
        # i ← i + 1
        i += 1

if __name__ == "__main__":
    # 画像にあるデータを再現
    data = [25, 36, 11, 32, 81, 15, 52]
    basic_insertion_sort(data)
