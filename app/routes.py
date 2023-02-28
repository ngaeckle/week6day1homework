from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.jinja', title='Home')

@app.route('/about')
def about():
    return render_template('about.jinja',title='About')

@app.route('/register')
def register():
    return render_template('register.jinja',title='Register')

@app.route('/login')
def login():
    return render_template('login.jinja',title='Login')

@app.route('/blog')
def login():
    return render_template('blog.jinja',title='Blog')