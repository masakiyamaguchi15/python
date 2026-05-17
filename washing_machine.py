import time

def main():
    # 良い匂いにしたい？ (Yes / No)
    want_good_smell = input("良い匂いにしたいですか？ (yes/no): ")
    
    if want_good_smell.lower() in ['yes', 'y', 'はい']:
        print("柔軟剤を入れる")
        
    print("ふたを閉める")
    print("自分の名前を書いた紙を貼る")
    print("スタートボタンを押す")
    
    # 反復: 終わるまで待つ
    is_finished = False
    count = 0
    print("（洗濯が終わるまで待ちます）")
    
    while not is_finished:
        # なにもしない
        print("なにもしない...")
        time.sleep(1) # 1秒待機
        
        # シミュレーションとして、3回ループしたら終了とする
        count += 1
        if count >= 3:
            is_finished = True
            
    print("ふたを開けて取り出す")

if __name__ == "__main__":
    main()
