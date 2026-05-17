def basic_selection_sort(arr):
    n = len(arr)
    
    # ヘッダーの出力
    print(f"{'i':<2} | {'j':<2} | {'配列[i]':<5} | {'配列[j]':<5} | {'配列[i] > 配列[j]':<15} | {'入れ替え':<5} | 配列の状態 (処理後)")
    print("-" * 85)
    
    # 初期状態の出力
    print(f"{'-':<2} | {'-':<2} | {'-':<5} | {'-':<5} | {'-':<15} | {'-':<5} | {arr}")
    
    i = 0
    while i < n - 1:
        j = i + 1
        while j < n:
            val_i = arr[i]
            val_j = arr[j]
            condition = "Yes" if val_i > val_j else "No"
            swapped = "有" if val_i > val_j else "なし"
            
            # 比較と入れ替え
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                
            # 途中経過の出力
            print(f"{i:<2} | {j:<2} | {val_i:<5} | {val_j:<5} | {condition:<15} | {swapped:<5} | {arr}")
            
            j += 1
        i += 1

if __name__ == "__main__":
    # 画像にあるデータを再現
    data = [25, 36, 11, 32, 81, 15, 52]
    basic_selection_sort(data)
