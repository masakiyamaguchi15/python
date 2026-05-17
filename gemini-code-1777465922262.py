from flask import Flask, request, render_template

app = Flask(__name__)

# Entity (実体) の代わりとなる簡易的なデータストア
books = {"101": "オブジェクト指向分析設計", "102": "Python入門"}
users = {"U001": {"name": "山田太郎", "status": "eligible"}}
loan_ledger = []

# Boundary (境界) / Controller (制御)
@app.route('/borrow', methods=['POST'])
def borrow_book():
    user_id = request.form.get('user_id')
    book_id = request.form.get('book_id')
    
    # 制御ロジック
    user = users.get(user_id)
    if user and user['status'] == 'eligible':
        book_title = books.get(book_id)
        if book_title:
            # 貸出を記録 (Entityへの操作)
            loan_ledger.append({"user_id": user_id, "book_id": book_id})
            return f"{user['name']}さんに『{book_title}』を貸し出しました。"
        return "本が見つかりません。", 404
    return "利用資格がありません。", 403

if __name__ == '__main__':
    app.run(debug=True)