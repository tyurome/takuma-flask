#Webフレームワーク
from flask import Flask, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from models import db, User

#入出力管理用
import os

app = Flask(__name__)

#db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///.database.db' #sqliteのDBファイルを指定
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #DB変更時の追跡機能を無効可（推奨はFalse）
app.config['SECRET_KEY'] = os.urandom(24) #session情報の暗号化キーを生成
db.init_app(app) #db modelを初期化

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'main.login' #セッション情報が無い場合にリダイレクトするページの指定

#ログインマネージャ、セッション情報の取得
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from controller import main
app.register_blueprint(main)

@app.route('/test')
def test():
    return url_for('main.login')

#アプリケーションの起動
if __name__ == '__main__':
    #DBの初期化
    with app.app_context():
        db.create_all()
    #指定のIPアドレスとポート番号でアプリケーションを起動
    app.run(host="0.0.0.0", port=5000)