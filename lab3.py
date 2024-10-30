from flask import Blueprint, url_for, redirect, render_template, make_response, request
lab3 = Blueprint('lab3',__name__)


@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name = name, name_color = name_color)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3'))
    resp.set_cookie('name', 'Ira', max_age=2)
    resp.set_cookie('age', '19')
    resp.set_cookie('name_color', 'magenta')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3'))
    resp.delete_cookie('name', 'Ira')
    resp.delete_cookie('age', '19')
    resp.delete_cookie('name_color')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user = user, age = age, sex = sex, errors = errors)


@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price +=30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('lab3/pay.html', price = price)


@lab3.route('/lab3/success')
def success():
    return render_template('lab3/success.html')


@lab3.route('/lab3/settings')
def settings():
        color = request.args.get('color')
        background_color = request.args.get('background_color')
        font_size = request.args.get('font_size')
        font_weight = request.args.get('font_weight')
        resp = make_response(render_template('/lab3/settings.html', color = color,
                                              background_color=background_color, 
                                              font_size=font_size, 
                                              font_weight=font_weight))
        if color:
            resp.set_cookie('color', color,)
        if background_color:
            resp.set_cookie('background_color', background_color)
        if font_size:
            resp.set_cookie('font_size', font_size)
        if font_weight:
            resp.set_cookie('font_weight', font_weight)   
        return resp


@lab3.route('/lab3/del_settings', methods=['GET'])
def del_cookies():
    resp = make_response(redirect('lab3'))
    resp.delete_cookie('color')
    resp.delete_cookie('background_color')
    resp.delete_cookie('font_size')
    resp.delete_cookie('font_weight')
    return resp





if __name__ == '__main__':
    app.run(debug=True)


@lab3.route('/lab3/ticket', methods=['GET', 'POST'])
def ticket():
    if request.method == 'GET':
        # Передаем пустой словарь errors при GET запросе
        return render_template('lab3/ticket_form.html', errors={})

    errors = {}
    fio = request.form.get('fio')
    if not fio:
        errors['fio'] = 'Заполните поле ФИО'

    shelf = request.form.get('shelf')
    if not shelf:
        errors['shelf'] = 'Выберите полку'

    with_linen = request.form.get('with_linen')
    with_baggage = request.form.get('with_baggage')
    age = request.form.get('age')
    if not age:
        errors['age'] = 'Заполните поле возраста'
    elif not age.isdigit() or not (1 <= int(age) <= 120):
        errors['age'] = 'Возраст должен быть от 1 до 120 лет'

    departure = request.form.get('departure')
    if not departure:
        errors['departure'] = 'Заполните поле пункта выезда'

    destination = request.form.get('destination')
    if not destination:
        errors['destination'] = 'Заполните поле пункта назначения'

    date = request.form.get('date')
    if not date:
        errors['date'] = 'Заполните поле даты поездки'

    insurance = request.form.get('insurance')

    if errors:
        return render_template('lab3/ticket_form.html', errors=errors, fio=fio, shelf=shelf, with_linen=with_linen, with_baggage=with_baggage, age=age, departure=departure, destination=destination, date=date, insurance=insurance)

    # Расчет цены
    price = 1000 if int(age) >= 18 else 700
    if shelf in ['нижняя', 'нижняя боковая']:
        price += 100
    if with_linen:
        price += 75
    if with_baggage:
        price += 250
    if insurance:
        price += 150

    return render_template('lab3/ticket.html', fio=fio, shelf=shelf, with_linen=with_linen, with_baggage=with_baggage, age=age, departure=departure, destination=destination, date=date, insurance=insurance, price=price)
    


