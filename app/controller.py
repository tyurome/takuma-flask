#Webフレームワーク
from flask import Flask, render_template, request, redirect, url_for, Blueprint
#セッション管理用拡張機能
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

#DB接続用ORM
from flask_sqlalchemy import SQLAlchemy
#パスワードハッシュ化用
from werkzeug.security import generate_password_hash, check_password_hash
#models.pyから、db及びUserクラスをimport
from models import db, User


main = Blueprint('main', __name__)


@main.route('/')
def index():
    #ルートディレクトリにアクセスした場合、loginページにリダイレクト
    return redirect(url_for('main.register'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        #ORMの使用、usernameとpasswordをUserクラスに格納
        username = request.form.get('username')
        password = request.form.get('password')
        #Userクラスのインスタンスを生成し、ORMで紐づけ
        user = User(username=username, password=generate_password_hash(password, method='pbkdf2:sha256'))
        #インスタンスに基づきDBに登録
        db.session.add(user)
        #DBに反映
        db.session.commit()
        #登録後は、loginページにリダイレクト
        return redirect('/login')
    else:
        #GETがない（＝登録時でない）場合は、テンプレートエンジンを使って、/app/templates内のregister.htmlを表示
        return render_template('register.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first() #ユーザ名がユニークなのでfirst（検索時の一番上）指定
        if check_password_hash(user.password, password): #ハッシュ化されたパスワードをチェック
            #Flask-Loginのlogin_user()を使用して、セッション情報を設定
            login_user(user)
            return redirect('/home')
    else:
        return render_template('login.html')

@main.route('/logout')
@login_required #ログインを必須条件にする
def logout():
    #Flask-Loginのlogout_user()を使用して、セッション情報を削除
    logout_user()
    return redirect(url_for('/login'))

@main.route('/home')
@login_required
def home():
    #ログイン情報から、Userクラスのusernameを取得
    showname = 'Logged in as: ' + current_user.username
    return render_template('home.html' , showname=showname)