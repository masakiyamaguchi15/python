import random
import sys
def main():
    # Windowsのコンソールでの文字化け対策（UTF-8出力に再設定）
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        
    # メンバー AからH
    members = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    
    # 1番目から8番目までの順番を作成してシャッフル
    orders = list(range(1, 9))
    random.shuffle(orders)
    
    # メンバーと順番を紐付けて出力
    for member, order in zip(members, orders):
        print(f"{member} グループ {order}番目")

if __name__ == "__main__":
    main()
