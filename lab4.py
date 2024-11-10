from flask import Blueprint, url_for, redirect, render_template, make_response, request, session
lab4 = Blueprint('lab4',__name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')


@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')


@lab4.route('/lab4/div', methods = ['POST'])
def div():
    if request.method == 'POST':
        x1 = request.form.get('x1')
        x2 = request.form.get('x2')
        
        # Проверка на пустые поля
        if x1 == '' or x2 == '':
            return render_template('lab4/div.html', x1=x1, x2=x2, error='Оба поля должны быть заполнены')
        
        # Преобразование в числа
        try:
            x1 = int(x1)
            x2 = int(x2)
        except ValueError:
            return render_template('lab4/div.html', x1=x1, x2=x2, error='Оба поля должны содержать числа')
        
        # Проверка на деление на ноль
        if x2 == 0:
            return render_template('lab4/div.html', x1=x1, x2=x2, error='Деление на ноль невозможно')
        
        # Выполнение деления
        result = x1 / x2
        return render_template('lab4/div.html', x1=x1, x2=x2, result=result)
    
    return render_template('lab4/div.html')


@lab4.route('/lab4/sum', methods=['GET', 'POST'])
def sum():
    if request.method == 'POST':
        x1 = request.form.get('x1', 0)
        x2 = request.form.get('x2', 0)
        
        try:
            x1 = int(x1)
            x2 = int(x2)
        except ValueError:
            return render_template('lab4/sum.html', x1=x1, x2=x2, error='Оба поля должны содержать числа')
        
        result = x1 + x2
        return render_template('lab4/sum.html', x1=x1, x2=x2, result=result)
    
    return render_template('lab4/sum.html')

@lab4.route('/lab4/mul', methods=['GET', 'POST'])
def mul():
    if request.method == 'POST':
        x1 = request.form.get('x1', 1)
        x2 = request.form.get('x2', 1)
        
        try:
            x1 = int(x1)
            x2 = int(x2)
        except ValueError:
            return render_template('lab4/mul.html', x1=x1, x2=x2, error='Оба поля должны содержать числа')
        
        result = x1 * x2
        return render_template('lab4/mul.html', x1=x1, x2=x2, result=result)
    
    return render_template('lab4/mul.html')

@lab4.route('/lab4/sub', methods=['GET', 'POST'])
def sub():
    if request.method == 'POST':
        x1 = request.form.get('x1')
        x2 = request.form.get('x2')
        
        if x1 == '' or x2 == '':
            return render_template('lab4/sub.html', x1=x1, x2=x2, error='Оба поля должны быть заполнены')
        
        try:
            x1 = int(x1)
            x2 = int(x2)
        except ValueError:
            return render_template('lab4/sub.html', x1=x1, x2=x2, error='Оба поля должны содержать числа')
        
        result = x1 - x2
        return render_template('lab4/sub.html', x1=x1, x2=x2, result=result)
    
    return render_template('lab4/sub.html')

@lab4.route('/lab4/pow', methods=['GET', 'POST'])
def pow():
    if request.method == 'POST':
        x1 = request.form.get('x1')
        x2 = request.form.get('x2')
        
        if x1 == '' or x2 == '':
            return render_template('lab4/pow.html', x1=x1, x2=x2, error='Оба поля должны быть заполнены')
        
        try:
            x1 = int(x1)
            x2 = int(x2)
        except ValueError:
            return render_template('lab4/pow.html', x1=x1, x2=x2, error='Оба поля должны содержать числа')
        
        if x1 == 0 and x2 == 0:
            return render_template('lab4/pow.html', x1=x1, x2=x2, error='Оба поля не могут быть нулями')
        
        result = x1 ** x2
        return render_template('lab4/pow.html', x1=x1, x2=x2, result=result)
    
    return render_template('lab4/pow.html')

@lab4.route('/lab4/division', methods=['GET', 'POST'], endpoint='division')
def division():
    if request.method == 'POST':
        x1 = request.form.get('x1')
        x2 = request.form.get('x2')
        
        if x1 == '' or x2 == '':
            return render_template('lab4/division.html', x1=x1, x2=x2, error='Оба поля должны быть заполнены')
        
        try:
            x1 = int(x1)
            x2 = int(x2)
        except ValueError:
            return render_template('lab4/division.html', x1=x1, x2=x2, error='Оба поля должны содержать числа')
        
        if x2 == 0:
            return render_template('lab4/division.html', x1=x1, x2=x2, error='Деление на ноль невозможно')
        
        result = x1 / x2
        return render_template('lab4/division.html', x1=x1, x2=x2, result=result)
    
    return render_template('lab4/division.html')


tree_count = 0

@lab4.route('/lab4/tree', methods = ['GET', 'POST'])
def tree() :
    global tree_count
    if request.method == 'GET' :
        return render_template('lab4/tree.html', tree_count=tree_count)
    
    operation = request.form.get('operation')

    if operation == 'cut':
        if tree_count > 0:
            tree_count -= 1
    elif operation == 'plant':
        if tree_count < 10:  # Максимальное количество деревьев
            tree_count += 1

    return redirect('/lab4/tree') 


users = [
    {'login': 'Ира', 'password': '123', "name": "Ира Нестеренко", "gender": "female"},
    {'login': 'Боб', 'password': '999' , "name": "Боб", "gender": "male"},
     {'login': 'Юля', 'password': '111', "name": "Юля Ефимова", "gender": "female" },
    {'login': 'Катя', 'password': '222' , "name": "Катя Изотова", "gender": "female"},
]

@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            authorized = True
            login = session['login']
        else:
            authorized = False
            login = ''    
        return render_template('lab4/login.html', authorized=authorized, login=login)

    login_input = request.form.get('login')
    password_input = request.form.get('password')

    # Проверка на пустые значения
    if not login_input:
        return render_template('lab4/login.html', login=login_input, error='Не введён логин')
    if not password_input:
        return render_template('lab4/login.html', login=login_input, error='Не введён пароль')

    for user in users:
        if login_input == user['login'] and password_input == user['password']:
            session['login'] = login_input
            session['name'] = user['name']
            return redirect('/lab4/login')
    
    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', login=login_input, error=error, authorized=False)

@lab4.route('/lab4/logout', methods=['POST'])
def logout():
    session.pop('login', None)
    session.pop('name', None)
    return redirect('/lab4/login')



@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    if request.method == 'POST':
        temperature = request.form.get('temperature')
        
        if not temperature:
            error = 'Ошибка: не задана температура'
            return render_template('lab4/fridge.html', error=error)
        
        try:
            temperature = float(temperature)
        except ValueError:
            error = 'Ошибка: введено некорректное значение температуры'
            return render_template('lab4/fridge.html', error=error)
        
        if temperature < -12:
            error = 'Не удалось установить температуру — слишком низкое значение'
            return render_template('lab4/fridge.html', error=error)
        elif temperature > -1:
            error = 'Не удалось установить температуру — слишком высокое значение'
            return render_template('lab4/fridge.html', error=error)
        elif -12 <= temperature <= -9:
            message = f'Установлена температура: {temperature}°С'
            snowflakes = 3
        elif -8 <= temperature <= -5:
            message = f'Установлена температура: {temperature}°С'
            snowflakes = 2
        elif -4 <= temperature <= -1:
            message = f'Установлена температура: {temperature}°С'
            snowflakes = 1
        
        return render_template('lab4/fridge.html', message=message, snowflakes=snowflakes)
    
    return render_template('lab4/fridge.html')


# Цены на зерно
prices = {
    'ячмень': 12345,
    'овёс': 8522,
    'пшеница': 8722,
    'рожь': 14111
}

@lab4.route('/lab4/grain_order', methods=['GET', 'POST'])
def grain_order():
    if request.method == 'POST':
        grain_type = request.form.get('grain_type')
        weight = request.form.get('weight')
        
        if not weight:
            error = 'Ошибка: не указан вес'
            return render_template('lab4/grain_order.html', error=error)
        
        try:
            weight = float(weight)
        except ValueError:
            error = 'Ошибка: введено некорректное значение веса'
            return render_template('lab4/grain_order.html', error=error)
        
        if weight <= 0:
            error = 'Ошибка: вес должен быть больше 0'
            return render_template('lab4/grain_order.html', error=error)
        
        if weight > 500:
            error = 'Ошибка: такого объёма сейчас нет в наличии'
            return render_template('lab4/grain_order.html', error=error)
        
        price_per_ton = prices[grain_type]
        total_price = weight * price_per_ton
        
        if weight > 50:
            discount = total_price * 0.1
            total_price -= discount
            discount_message = f'Применена скидка за большой объём: {discount} руб'
        else:
            discount_message = ''
        
        message = f'Заказ успешно сформирован. Вы заказали {grain_type}. Вес: {weight} т. Сумма к оплате: {total_price} руб'
        return render_template('lab4/grain_order.html', message=message, discount_message=discount_message)
    
    return render_template('lab4/grain_order.html')