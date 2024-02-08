from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegistractionForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '4058f686bb3cc7a9edc824164d1ed6c6'
app.config['SQLALCHEMY_DATATBASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = username = db.Column(db.String(100), nullable=False)
    data_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())    
    content = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
    
    
posts = [
    {
        'author': 'Kankavee Ramri',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Peerada Anusakchaikul',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    },
    {
        'author': 'Puntawut Samakkee',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'April 22, 2018'
    }    
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistractionForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title = 'Login', form = form)

if __name__ == "__main__":
    app.run(debug=True)