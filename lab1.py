from flask import Blueprint, url_for, redirect, render_template, make_response, render_template
lab1 = Blueprint('lab1',__name__)




@lab1.route("/lab1/web")
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


@lab1.route("/lab1/author")
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


@lab1.route("/lab1")
def lab():
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

@lab1.route("/lab1/oak")
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


count = 0

@lab1.route('/lab1/counter')
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


@lab1.route('/lab1/reset_counter')
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


@lab1.route("/lab1/info")
def info():
    return redirect("/author")

@lab1.route("/lab1/created")
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


@lab1.route('/lab1/custom')
def custom():
    response = make_response(render_template('custom.html'))
    response.headers['Content-Language'] = 'ru'
    response.headers['X-Custom-Header-1'] = 'Custom Value 1'
    response.headers['X-Custom-Header-2'] = 'Custom Value 2'
    return response

