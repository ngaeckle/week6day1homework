from flask import render_template, flash, redirect
from app import app
from app.forms import CarForm, SignInForm, SignUpForm
from app.models import User, Car
from flask_login import current_user, login_user, login_required, logout_user

@app.route('/')
@login_required
def index():
    form = CarForm()
    if form.validate_on_submit():
        make = form.make.data
        model = form.model.data
        year = form.year.data
        color = form.color.data
        price = form.price.data
        car = Car(make=make,model=model,year=year,color=color,price=price, user_id=current_user.id)
        car.commit()
        flash(f'Car information logged successfully to ')
    return render_template('index.jinja', title='Home', form=form)


@app.route('/about')
def about():
    return render_template('about.jinja',title='About')

@app.route('/register')
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        u = User(username=username,email=email,password_hash='',first_name=first_name,last_name=last_name)
        user_match = User.query.filter_by(username=username).first()
        email_match = User.query.filter_by(email=email).first()
        if user_match:
            flash(f'Username: {username} already exists, try again')
            return redirect('/register')
        elif email_match:
            flash(f'Email: {email} already exists, try again')
            return redirect('/register')
        else:
            u.hash_password(password)
            u.commit()
            flash(f'Login for {username} successful')
            return redirect('/')
    return render_template('register.jinja',title='Register', form=form)

@app.route('/login')
def login():
    form = SignInForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user_match = User.query.filter_by(username=username).first()
        if not user_match or not user_match.check_password(password):
            flash(f'Username or Password was incorrect, try again')
            return redirect('/login')

        flash(f'Username: {username} already exists, try again')
        login_user(user_match)
        return redirect('/')
    return render_template('login.jinja',title='Login', form=form)

@app.route('/blog')
def blog():
    return render_template('blog.jinja',title='Blog')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')