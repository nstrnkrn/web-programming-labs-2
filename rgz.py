from flask import Flask, Blueprint, render_template, request, redirect, url_for, session
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Создаем Blueprint
rgz = Blueprint('rgz', __name__)

# Подключение к базе данных PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="irinadb",
        user="irina",
        password="123"
    )
    return conn

# Пример отладки в функции входа
@rgz.route('/rgz/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('rgz/login.html')
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not login or not password:
        return render_template('rgz/login.html', error='Логин и пароль обязательны')

    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        cursor.execute('SELECT * FROM users WHERE username = %s', (login,))
        user = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('rgz.index'))
        else:
            return render_template('rgz/login.html', error='Неверный логин или пароль')
    
    except Exception as e:
        return render_template('rgz/login.html', error=f'Ошибка: {e}')

# --- Главная страница с пагинацией ---
@rgz.route('/rgz/', defaults={'page': 1})
@rgz.route('/rgz/page/<int:page>')
def index(page):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        offset = (page - 1) * 20
        cursor.execute('SELECT * FROM initiatives ORDER BY created_at DESC, id DESC LIMIT 20 OFFSET %s', (offset,))
        initiatives = cursor.fetchall()

        cursor.execute('SELECT COUNT(*) FROM initiatives')
        total_initiatives = cursor.fetchone()['count']

        cursor.close()
        conn.close()

        total_pages = (total_initiatives // 20) + (1 if total_initiatives % 20 > 0 else 0)
        
        return render_template('rgz/index.html', initiatives=initiatives, page=page, total_pages=total_pages)

    except Exception as e:
        return render_template('rgz/index.html', error=f"Ошибка при загрузке инициатив: {e}")

# --- Регистрация пользователя ---
@rgz.route('/rgz/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('rgz/register.html')
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not login:
        return render_template('rgz/register.html', error='Не введён логин')
    if not password:
        return render_template('rgz/register.html', error='Не введён пароль')

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM users WHERE username = %s', (login,))
        user = cursor.fetchone()
        
        if user:
            return render_template('rgz/register.html', error='Логин уже занят')
        
        hashed_password = generate_password_hash(password)

        cursor.execute(
            'INSERT INTO users (username, password) VALUES (%s, %s)',
            (login, hashed_password)
        )
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect(url_for('rgz.index'))
    
    except Exception as e:
        return render_template('rgz/register.html', error=f'Ошибка: {e}')

# --- Выход пользователя ---
@rgz.route('/rgz/logout')
def logout():
    session.clear()
    return redirect(url_for('rgz.index'))

# --- Создание инициативы ---
@rgz.route('/rgz/create_initiative', methods=['GET', 'POST'])
def create_initiative():
    if 'user_id' not in session:
        return redirect(url_for('rgz.login'))

    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')

        if not title or not description:
            return render_template('create_initiative.html', error='Заполните все поля')

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            user_id = session['user_id']

            cursor.execute(
                'INSERT INTO initiatives (user_id, title, description) VALUES (%s, %s, %s)',
                (user_id, title, description)
            )
            conn.commit()

            cursor.close()
            conn.close()

            return redirect(url_for('rgz.index'))

        except Exception as e:
            return render_template('rgz/create_initiative.html', error=f'Ошибка при добавлении инициативы: {e}')

    return render_template('rgz/create_initiative.html')

# --- Удаление инициативы ---
@rgz.route('/rgz/initiative/delete/<int:initiative_id>', methods=['POST'])
def delete_initiative(initiative_id):
    if 'user_id' not in session:
        return redirect(url_for('rgz.login'))

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM initiatives WHERE id = %s AND user_id = %s', (initiative_id, session['user_id']))
        initiative = cursor.fetchone()

        if not initiative:
            return redirect(url_for('rgz.index'))

        cursor.execute('DELETE FROM initiatives WHERE id = %s', (initiative_id,))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('rgz.index'))

    except Exception as e:
        return f"Ошибка при удалении инициативы: {e}"

# --- Голосование за инициативу ---
@rgz.route('/rgz/initiative/vote/<int:initiative_id>/<string:vote_type>', methods=['POST'])
def vote_initiative(initiative_id, vote_type):
    if 'user_id' not in session:
        return redirect(url_for('rgz.login'))
    
    if vote_type not in ['up', 'down']:
        return redirect(url_for('rgz.index'))
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        cursor.execute(''' 
            SELECT * FROM votes WHERE initiative_id = %s AND user_id = %s 
        ''', (initiative_id, session['user_id']))
        existing_vote = cursor.fetchone()

        if existing_vote:
            return redirect(url_for('rgz.index'))

        cursor.execute(''' 
            INSERT INTO votes (user_id, initiative_id, vote_type) 
            VALUES (%s, %s, %s)
        ''', (session['user_id'], initiative_id, vote_type))
        conn.commit()

        if vote_type == 'up':
            cursor.execute(''' 
                UPDATE initiatives SET rating = rating + 1 WHERE id = %s 
            ''', (initiative_id,))
        elif vote_type == 'down':
            cursor.execute(''' 
                UPDATE initiatives SET rating = rating - 1 WHERE id = %s 
            ''', (initiative_id,))

        cursor.execute('SELECT rating FROM initiatives WHERE id = %s', (initiative_id,))
        result = cursor.fetchone()

        if result and 'rating' in result:
            rating = result['rating']

            if rating <= -10:
                cursor.execute('DELETE FROM initiatives WHERE id = %s', (initiative_id,))
        
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('rgz.index'))

    except Exception as e:
        return f"Ошибка при голосовании: {e}"

# Регистрация Blueprint в приложении
app.register_blueprint(rgz)

if __name__ == '__main__':
    app.run(debug=True)

