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
