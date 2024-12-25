from flask import Blueprint, url_for, redirect, render_template, make_response, request, session
lab5 = Blueprint('lab5',__name__)

import psycorg2
from psycopg2.extras import RealDictCursor

@lab5.route('/lab5/')
def lab():
    return render_template('lab5/lab5.html', login=session.get('login'))


@lab5.route('/lab5/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab5/register.html')
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not login:
        return render_template('lab5/register.html', error='Не введён логин')
    if not password:
        return render_template('lab5/register.html', error='Не введён пароль')
    

@lab5.route('/lab5/login', methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('lab5/login.html')
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not (login or password):
        return render_template('lab5/login.html, error="Заполните поля')
    
    conn = psycorg2.connect(
        host = '127.0.0.1',
        database = 'irinanesterenko'
        user = 'irinanesterenko'
        password = '123'
    )
    cur = conn.cursor(cursor_factory = RealDictCursor)

    cur.execute(f"SELECT * FROM users WHERE login='{login}';")
    user = cur.fetchone()

    if not user:
        cur.close()
        conn.close()
        return render_template('lab5/login.html',
                               error='Логин и/или пароль неверны')
    
    if user ['password'] !=password:
        cur.close()
        conn.close()
        return render_template('lab5/login.html',
                               error='Логин и/или пароль неверны')
    session['login'] = login
    cur.close()
    conn.close()
    return render_template('lab5/success_login.html', login=login)

