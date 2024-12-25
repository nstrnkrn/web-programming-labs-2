from flask import Blueprint, render_template, request, session, redirect, url_for
import psycopg2
from psycopg2.extras import RealDictCursor

lab5 = Blueprint('lab5', __name__)

# Подключение к базе данных PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="irinanesterenko",
        user="irinanesterenko",
        password="123"
    )
    cur = conn.cursor(cursor_factory=RealDictCursor)
    return conn, cur

# Функция для закрытия соединения с базой данных
def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

@lab5.route('/lab5/')
def lab():
    return render_template('lab5/lab5.html', login=session.get('login'))

# @lab5.route('/lab5/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'GET':
#         return render_template('lab5/register.html')
    
#     login = request.form.get('login')
#     password = request.form.get('password')

#     if not login:
#         return render_template('lab5/register.html', error='Не введён логин')
#     if not password:
#         return render_template('lab5/register.html', error='Не введён пароль')
    
#     # Проверка на уникальность логина в базе данных
#     conn = get_db_connection()
#     cur = conn.cursor(cursor_factory=RealDictCursor)
    
#     cur.execute("SELECT * FROM users WHERE login = %s;", (login,))
#     existing_user = cur.fetchone()
    
#     if existing_user:
#         cur.close()
#         conn.close()
#         return render_template('lab5/register.html', error='Этот логин уже занят')
    
#     # Если логин уникален, сохраняем пользователя в базу
#     cur.execute("INSERT INTO users (login, password) VALUES (%s, %s);", (login, password))
#     conn.commit()
    
#     cur.close()
#     conn.close()

#     return redirect(url_for('lab5.login'))

@lab5.route('/lab5/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab5/register.html')

    login = request.form.get('login')
    password = request.form.get('password')

    if not (login and password):
        return render_template('lab5/register.html', error='Заполните все поля')

    try:
        conn, cur = db_connect()
        
        # Проверка уникальности логина
        cur.execute("SELECT login FROM users WHERE login = %s;", (login,))
        if cur.fetchone():
            db_close(conn, cur)
            return render_template('lab5/register.html', error='Такой пользователь уже существует')
        
        # Регистрация пользователя
        cur.execute("INSERT INTO users (login, password) VALUES (%s, %s);", (login, password))
        conn.commit()
        
    except Exception as e:
        print(f"Ошибка: {e}")
        return render_template('lab5/register.html', error='Ошибка сервера')
    finally:
        db_close(conn, cur)
    
    return render_template('lab5/success.html', login=login)



@lab5.route('/lab5/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab5/login.html')
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not (login and password):
        return render_template('lab5/login.html', error="Заполните поля")

    # Подключение к базе данных
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("SELECT * FROM users WHERE login = %s;", (login,))
    user = cur.fetchone()

    if not user or user['password'] != password:
        cur.close()
        conn.close()
        return render_template('lab5/login.html', error='Логин и/или пароль неверны')

    # Успешный вход
    session['login'] = login
    cur.close()
    conn.close()

    return render_template('lab5/success_login.html', login=login)

@lab5.route('/lab5/logout')
def logout():
    session.pop('login', None)  # Удаляем логин из сессии
    return redirect(url_for('lab5.lab'))

