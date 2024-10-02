from flask import Flask, url_for, redirect
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
                        <a href="lab1/python">Python</a>
                    </li>
                    <li>
                        <a href="lab1/crypto">Криптовалюта</a>
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
    return "Нет такой страницы", 404



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

    

