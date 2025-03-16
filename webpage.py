from flask import Flask, render_template

app = Flask(__name__)  # Flaskアプリを作成

@app.route("/")  # トップページ
def home():
    return render_template("index.html")  # `index.html` を表示

@app.route("/about")  # /about ページ
def about():
    return render_template("about.html")  # `about.html` を表示

if __name__ == "__main__":
    app.run(debug=True)  # サーバーを起動（デバッグモードON）