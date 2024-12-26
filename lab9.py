from flask import Flask, Blueprint, render_template, request, redirect, url_for, session

lab9 = Blueprint('lab9', __name__, template_folder='templates')

@lab9.route('/lab9/', methods=['GET', 'POST'])
def step1_name():
    # Если данные поздравления уже есть, сразу показываем финальную страницу
    if all(session.get(key) for key in ['name9', 'age9', 'gender9', 'preference19', 'preference29']):
        return redirect(url_for('lab9.final'))
    if request.method == 'POST':
        session['name9'] = request.form.get('name')
        return redirect(url_for('lab9.step2_age'))
    return render_template('/lab9/step1_name.html')

@lab9.route('/lab9/age/', methods=['GET', 'POST'])
def step2_age():
    if request.method == 'POST':
        session['age9'] = request.form.get('age')
        return redirect(url_for('lab9.step3_gender'))
    return render_template('/lab9/step2_age.html')

@lab9.route('/lab9/gender/', methods=['GET', 'POST'])
def step3_gender():
    if request.method == 'POST':
        session['gender9'] = request.form.get('gender')
        return redirect(url_for('lab9.step4_preference1'))
    return render_template('/lab9/step3_gender.html')

@lab9.route('/lab9/preference1/', methods=['GET', 'POST'])
def step4_preference1():
    if request.method == 'POST':
        session['preference19'] = request.form.get('preference1')
        return redirect(url_for('lab9.step5_preference2'))
    return render_template('/lab9/step4_preference1.html')

@lab9.route('/lab9/preference2/', methods=['GET', 'POST'])
def step5_preference2():
    preference1 = session.get('preference19', '')
    if request.method == 'POST':
        session['preference29'] = request.form.get('preference2')
        return redirect(url_for('lab9.final'))
    return render_template('/lab9/step5_preference2.html', preference1=preference1)

@lab9.route('/lab9/final/')
def final():
    name = session.get('name9', 'гость')
    age = int(session.get('age9', 0))
    gender = session.get('gender9')
    preference1 = session.get('preference19', '')
    preference2 = session.get('preference29', '')

    if age < 15:
        
        if gender == 'male':
            grown = 'Желаем, чтобы ты рос сильным, умным и уверенным в себе! Пусть впереди будут только победы и успехи, а в жизни всегда будет много верных друзей и ярких моментов! Пусть школа будет местом, где тебя ценят и уважают!'
        else:
            grown = 'Желаем, чтобы ты росла умной, красивой и уверенной в себе! Пусть в жизни будет много ярких событий, а впереди — только счастье и успехи! Чтобы в школе ты всегда была лучшей, а твои мечты сбывались!'

    else:  
        if gender == 'male':
            grown = '''Новый год — это шанс начать все с чистого листа. Пусть в новом году тебе будет легко достигать своих целей и двигаться вперед. Пусть все твои мечты сбудутся, а впереди будут только яркие и радостные дни! С Новым годом!'''
        else:
            grown = '''Ты — воплощение красоты и силы, и пусть наступающий год принесет тебе море счастья и любви. Пусть будет больше радости, а впереди только светлое и успешное будущее! С Новым годом, моя королева!'''



    if preference1 == 'вкусное' and preference2 == 'горькое':
        gift = 'Луковица'
        img = 'onion.jpg'
    elif preference1 == 'вкусное' and preference2 == 'большое':
        gift = 'Бигбургер'
        img = 'bigburger.jpg'
    elif preference1 == 'невероятное' and preference2 == 'милое':
        gift = 'Сус'
        img = 'sus.jpg'
    else:
        gift = 'Глеб'
        img = 'gleb.png'

    return render_template('/lab9/final.html', name=name, age=age, grown=grown, gift=gift, img=img)

@lab9.route('/lab9/restart')
def restart():
    for key in ['name9', 'age9', 'gender9', 'preference19', 'preference29']:
        session.pop(key, None)
    return redirect('/lab9/')