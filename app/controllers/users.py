from app import app
from flask_bcrypt import Bcrypt
from flask import Flask, session, render_template, request, redirect, flash
from app.models.user import User

bcrypt = Bcrypt(app)


@app.route('/')
def show_reg_form():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def add_new_user():
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name': request.form['first_name'],
        'email': request.form['email'],
        'password': pw_hash
    }

    user_id = User.add(data)
    session['user_id'] = user_id
    return redirect('/login')


@app.route('/login')
def show_login_form():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    data = {'email': request.form['email']}
    user_in_db = User.get_by_email(data)

    if not user_in_db:
        flash('Invalid Email/Password')
        return redirect('/login')

    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid Email/Password')
        return redirect('/login')

    session['user_id'] = user_in_db.id

    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
