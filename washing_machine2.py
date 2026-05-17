import time

def main():
    # 図の記載通りに出力します。
    # ※「選択物を投入するd」はおそらく「洗濯物を投入する」のタイポと思われます。
    print("選択物を投入するd")
    
    print("洗濯機の電源を入れる")
    
    print("洗剤を洗剤入れに入れる")
    
    # コース選択（図の左右に「急ぎ」「予約」のメモがあるためここに入れておきます）
    print("コース選択")
    
    # 分岐：予約
    is_reserved = input("予約機能を使いますか？ (yes/no): ")
    if is_reserved.lower() in ['yes', 'y', 'はい']:
        # Yesの場合
        print("予約時間なる")
        time.sleep(1) # 予約時間まで待つシミュレーション
        
    # 予約してもしなくても最終的にここを通る
    print("スタートボタンを押す")
    
    # 途中工程
    print("すすぎ")
    print("洗剤投入")
    print("脱水")
    
    print("洗濯が終わる")
    
    # 分岐：乾燥機能
    use_dryer = input("乾燥機能を使いますか？ (yes/no): ")
    if use_dryer.lower() in ['yes', 'y', 'はい']:
        # Yesの場合
        print("乾燥させる")
        
    # 乾燥機能を使っても使わなくても最終的にここを通る
    # ※「選択物」はおそらく「洗濯物」のタイポと思われます。
    print("選択物を取り出す")
    print("終了する")

if __name__ == "__main__":
    main()
