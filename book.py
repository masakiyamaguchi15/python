class Book:
    def __init__(self, author: str, title: str, price: int, isbn: str):
        # 属性をプライベート変数として定義
        self.__author = author
        self.__title = title
        self.__price = price
        self.__isbn = isbn

    # ゲッターメソッド
    def getAuthor(self) -> str:
        return self.__author

    def getTitle(self) -> str:
        return self.__title

    def getPrice(self) -> int:
        return self.__price

    def getIsbn(self) -> str:
        return self.__isbn

    # セッターメソッド
    def setPrice(self, price: int) -> None:
        self.__price = price


# --- 使用例 ---
if __name__ == "__main__":
    # Bookオブジェクトの作成
    my_book = Book("夏目漱石", "こころ", 1200, "978-4-04-100000-0")

    # ゲッターを使って情報を取得
    print(f"タイトル: {my_book.getTitle()}")
    print(f"価格: {my_book.getPrice()}円")

    # セッターを使って価格を更新
    my_book.setPrice(1500)
    print(f"更新後の価格: {my_book.getPrice()}円")