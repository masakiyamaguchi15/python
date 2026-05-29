#ListElementTest.py

class ListElement:
    def __init__(self, val):
        self.val = val
        self.next = None

# リストの先頭要素を格納するグローバル変数
listHead = None


def delNode(pos):
    """引数 pos で指定された位置の要素を削除する手続き"""
    global listHead
    
    # pos が 1 と等しい場合
    if pos == 1:
        listHead = listHead.next
    else:
        prev = listHead
        # pos が 2 と等しいときは繰り返し処理を実行しない (iを2からpos-1まで増やす)
        for i in range(2, pos):
            prev = prev.next
        
        # [空欄の答え]: prev.next.next (選択肢 カ)
        # 削除対象ノードの次のノードへの参照を代入する
        if prev.next is not None:
            prev.next = prev.next.next
        else:
            print("指定された位置には要素が存在しません。")

def main():
    global listHead
    # リスト要素の初期化 (参照変数 list1, list2, list3, list4, list5)
    list1 = ListElement("T")
    list2 = ListElement("D")
    list3 = ListElement("I")
    list4 = ListElement("S")
    list5 = ListElement("S")  # 5番目の要素として "S" を定義

    # 単方向リストの連結
    list1.next = list2
    list2.next = list3
    list3.next = list4
    list4.next = list5

    # リストの先頭要素を格納
    listHead = list1

    # 消去するPOSをinput関数でUserから入力させる
    user_input = input("削除する位置 (1〜5) を入力してください: ")
    pos = int(user_input)
        
    # 削除処理の実行後のデータ
    delNode(pos)
    
    curr = listHead
    while curr is not None:
        print(curr.val)
        curr = curr.next
    
if __name__ == "__main__":
    main()

