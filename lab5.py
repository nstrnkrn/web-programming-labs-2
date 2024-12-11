from flask import Blueprint, url_for, redirect, render_template, make_response, request, session
lab5 = Blueprint('lab5',__name__)


@lab5.route('/lab5/')
def lab():
    return render_template('lab5/lab5.html')


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
    

from flask import Blueprint, render_templat
import psycorg2

conn = psycorg2.connect(
    host = '127.0.0.1',
    database = 'irinanesterenko',
    user = 'irinanesterenko',
    password = '123'    
)
cur = conn.cursor()

cur.execute(f"SELECT login FROM users WHERE login='{login}';")
if cur.fetchone():
    cur.close()
    conn.close()
        return render_template('lab5/register.html',
                           error="Такой пользователь уже существует")    

cur.execute(f"INSERT INTO users (login, password) VALUES ('{login}','{password}')")
conn.commit()
cur.close()
conn.close()
return render_template('lab5/success.html,login=login')