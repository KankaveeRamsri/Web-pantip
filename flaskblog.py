from flask import Flask, render_template
from forms import RegistractionForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '4058f686bb3cc7a9edc824164d1ed6c6'

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
    }   
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register")
def register():
    form = RegistractionForm()
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login")
def register():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)

if __name__ == "__main__":
    app.run(debug=True)