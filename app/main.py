from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User
import os

app = Flask(__name__)

#db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24) #secret key for session
db.init_app(app) #db modelを初期化

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' #route to login

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return redirect(url_for('/login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User(username=username, password=generate_password_hash(password, method='pbkdf2:sha256'))
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    else:
        return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first() #ユーザ名がユニークなのでfirst（一番上）指定でいいかな
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect('/home')
    else:
        return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home')
@login_required
def protected():
    return 'Logged in as: ' + current_user.username

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000)