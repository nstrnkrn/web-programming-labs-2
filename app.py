from flask import Flask, url_for, redirect, render_template, make_response, render_template
app = Flask(__name__)



@app.route("/lab1/web")
def web():
    return """<!doctype html>
        <html>
            <body>
                <h1>web-сервер на flask</h1>
                <a href="/author">author</a>
                <a href="/lab1">lab1</a>
            </body>
        </html>""", 200, {
            'X-Server': 'sample',
            'Content-Type': 'text/plain; charset=utf-8'
            }

@app.route("/lab1/author")
def author():
    name = "Нестеренко Ирина"
    group = "ФБИ-22"
    faculty = "ФБ"

    return"""<!doctype html>
        <html>
            <body>
                <p>Студент: """ + name + """</p>
                <p>Группа: """ + group + """</p>
                <p>Факультет: """ + faculty + """</p>
                <a href="/web">web</a>
                    </body>
                </html>"""

@app.route("/menu")
def menu():
    return """
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Захаров Илья Максимович, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        
        <div>
            <ol>
                <li>
                    <a href="/lab1">Лабораторная работа 1</a>
                </li>
            
            </ol>
        </div>

        <footer>
            &copy; Нестеренко Ирина, ФБИ-22, 3 курс, 2024 
        </footer>
    </body>
</html>
"""


@app.route("/lab1")
def lab1():
    return """
    <!DOCTYPE html>
    <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Захаров Илья Максимович, лабораторная 1</title>
        </head>
        <body>
            <header>
                НГТУ, ФБ, Лабораторная работа 1
            </header>
            <p>Flask — фреймворк для создания веб-приложений на языке программирования Python, 
            использующий набор инструментов Werkzeug, а также шаблонизатор Jinja2. Относится к 
            категории так называемых микрофреймворков — минималистичных каркасов веб-приложений, 
            сознательно предоставляющих лишь самые базовые возможности.</p>

            <a href="/menu">menu</a>
            
            <h2>Реализованные роуты</h2>
            <div>
                <ol>
                    <li>
                        <a href="lab1/oak">Дуб</a>
                    </li>
                    <li>
                        <a href="lab1/counter">Счетчик</a>
                    </li>
                     <li>
                        <a href="lab1/custom">Рецепт брауни</a>
                    </li>
                
                </ol>
            </div>
            
            <footer>
                &copy; Нестеренко Ирина, ФБИ-22, 3 курс, 2024 
            </footer>
        </body>
    </html>
    """

@app.route("/lab1/oak")
def oak():
    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <title>Дуб</title>
</head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
    </body>
</html>
'''


if __name__ == '__main__':
    app.run(debug=True)


count = 0

@app.route('/lab1/counter')
def counter():
    global count
    count += 1
    return f'''
<!doctype html>
<html>
    <body>
        Сколько раз вы заходили: {count}
        <br>
        <a href="{url_for('reset_counter')}">Очистить счетчик</a>
    </footer>
    </body>
</html>
'''

@app.route('/lab1/reset_counter')
def reset_counter():
    global count
    count = 0
    return '''
<!doctype html>
<html>
    <body>
        Счетчик очищен.
    </body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)



@app.route("/lab1/info")
def info():
    return redirect("/author")

@app.route("/lab1/created")
def created():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Создано успешно</h1>
        <div><i>что то создано...</i></div>
    <body>
</html>        
''', 201


@app.errorhandler(404)
def not_found(err):
    return render_template('404.html'), 404



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/error/400')
def error_400():
    return "Bad Request", 400

@app.route('/error/401')
def error_401():
    return "Unauthorized", 401

@app.route('/error/402')
def error_402():
    return "Payment Required", 402

@app.route('/error/403')
def error_403():
    return "Forbidden", 403

@app.route('/error/405')
def error_405():
    return "Method Not Allowed", 405

@app.route('/error/418')
def error_418():
    return "I'm a teapot", 418

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.route('/lab1/custom')
def custom():
    response = make_response(render_template('custom.html'))
    response.headers['Content-Language'] = 'ru'
    response.headers['X-Custom-Header-1'] = 'Custom Value 1'
    response.headers['X-Custom-Header-2'] = 'Custom Value 2'
    return response

if __name__ == '__main__':
    app.run(debug=True)








@app.route('/lab2/a/')
def a():
    return 'ok'



flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']
    
@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return "такого цветка нет", 404
    else:
        return "цветок: " + flower_list[flower_id]

@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name} </p>
    <p>Всего цветов: {len(flower_list)} </p>
    <p>Полный список: {flower_list}</p>
    </body>
</html>
'''


@app.route('/lab2/example')
def example():
    name = 'Нестеренко Ирина'
    group = 'ФБИ-22'
    number = '2'
    fruits =[
        {'name': 'яблоки', 'price': 100}, 
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 200},
        {'name': 'манго', 'price': 320},
        ]
    return render_template('example.html', name = name, group = group, number = number, fruits=fruits)

@app.route('/lab2/')
def lab2() :
    return render_template('lab2.html')

@app.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filters.html', phrase = phrase)


@app.route('/lab2/calc/')
def calc_default():
    return redirect(url_for('calc', a=1, b=1))

@app.route('/lab2/calc/<int:a>')
def calc_single_number(a):
    return redirect(url_for('calc', a=a, b=1))

@app.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    sum_result = a + b
    sub_result = a - b
    mul_result = a * b
    div_result = a / b if b != 0 else "Деление на ноль!"
    pow_result = a ** b
    return render_template('calc.html', sum_result=sum_result, sub_result=sub_result,
                           mul_result=mul_result, div_result=div_result, pow_result=pow_result, a=a, b=b)


books = [
    {"author": "Джордж Оруэлл", "title": "1984", "genre": "Научная фантастика", "pages": 328},
    {"author": "Рэй Брэдбери", "title": "451 градус по Фаренгейту", "genre": "Научная фантастика", "pages": 158},
    {"author": "Федор Достоевский", "title": "Преступление и наказание", "genre": "Роман", "pages": 671},
    {"author": "Джейн Остин", "title": "Гордость и предубеждение", "genre": "Роман", "pages": 432},
    {"author": "Михаил Булгаков", "title": "Мастер и Маргарита", "genre": "Фантастика", "pages": 480},
    {"author": "Эрих Мария Ремарк", "title": "Три товарища", "genre": "Роман", "pages": 480},
    {"author": "Габриэль Гарсиа Маркес", "title": "Сто лет одиночества", "genre": "Магический реализм", "pages": 448},
    {"author": "Антуан де Сент-Экзюпери", "title": "Маленький принц", "genre": "Философская сказка", "pages": 96},
    {"author": "Лев Толстой", "title": "Война и мир", "genre": "Роман", "pages": 1440},
    {"author": "Джоан Роулинг", "title": "Гарри Поттер и философский камень", "genre": "Фэнтези", "pages": 309}
]

@app.route('/lab2/books/')
def books_list():
    return render_template('books.html', books=books)


objects = [
    {
        "name": "Новосибирск",
        "description": "Новосибирск — третий по численности населения город России, крупнейший город её азиатской части, административный центр Сибирского федерального округа, Новосибирской области и Новосибирского района, центр Западно-Сибирского экономического района.",
        "image": "novosib.jpg"
    },
    {
        "name": "Томск",
        "description": "Томск — город в России, административный центр одноимённых области и района, расположенный на востоке Западной Сибири на берегу реки Томи.",
        "image": "tomsk.jpg"
    },
    {
        "name": "Москва",
        "description": "Москва — самый большой город в России по численности населения. Там проживают больше 12 миллионов человек. Полюбоваться столицей каждый год приезжают туристы из других городов и стран.",
        "image": "moskow.jpg"
    },
    {
        "name": "Сочи",
        "description": "Сочи – курортный город, расположенный на Черноморском побережье Краснодарского края. Большим Сочи называют также курортную зону федерального значения, которая объединяет сам город Сочи и несколько прибрежных поселений. Эта курортная местность протянулась на 145 км вдоль берега моря – от поселка Магри до границы с Абхазией.",
        "image": "sochi.jpg"
    },
    {
        "name": "Санк-Петербург",
        "description": "Основан в 1703 году Петром I, с 1712 по 1918 год был столицей Российской империи. В 1914―1924 годах переименован в Петроград, потом ― в Ленинград (до 1991 года). Находится на северо-западе России, на берегу Финского залива. По морю граничит с Финляндией и Эстонией. Город называют колыбелью трёх революций ― 1905―1907 годов, Февральской и Октябрьской 1917 года. Сегодня Санкт-Петербург ― важнейший экономический, научный и культурный центр РФ.",
        "image": "peter.jpg"
    }
]

@app.route('/lab2/objects/')
def objects_list():
    return render_template('objects.html', objects=objects)
