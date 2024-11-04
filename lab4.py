from flask import Blueprint, url_for, redirect, render_template, make_response, request
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


@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab4/login.html', authorized = False)

    login = request.form.get('login')
    password = request.form.get('password')

    if login == 'Ира' and password == '123':
        return render_template('/lab4/login.html', login=login, authorized = True)
    
    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', error=error, authorized = False)
 
 
