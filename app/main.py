#Web開発フレームワーク及びテンプレートエンジン
from flask import Flask, render_template

@app.route('/')
def hello_world():
    return 'Hello, Flask!'

#Web鯖起動
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)