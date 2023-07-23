import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = 'secret_key'
db = SQLAlchemy(app)
#LOGIN_MANAGER
login_manager = LoginManager(app)
login_manager.login_view = 'login'
#DATABASE ATTRIBUTES
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(150), unique=True)
    password_hash = db.Column(db.String(150))
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
#HOME PAGE
@app.route('/')
def home():
    return render_template('home.html')
#LOGIN PAGE
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user is not None :
            if user.check_password(password):
             login_user(user)  
            return redirect(url_for('secret_page'))
        else:
            flash('Invalid username or maybe an inavalid password.', 'danger')
    if current_user is None:
            flash('must log in!', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')
#SIGNUP PAGE
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords not matched', 'danger')
            return redirect(url_for('signup'))

        if User.query.filter_by(email=email).first():
            flash('Email already exists.', 'danger')
            return redirect(url_for('signup'))

        new_user = User(first_name=first_name, last_name=last_name, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Thank you for Registering to our website!', 'success')
        return redirect(url_for('thank_you'))

    return render_template('signup.html')
#SECRET_PAGE
@app.route('/secret_page')
def secret_page():
    return render_template('secret_page.html')
#THANK_YOU PAGE
@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')
#DEBUG 
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
