from flask import Flask, url_for, redirect, render_template, make_response, render_template
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from rgz import rgz

app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(rgz)


app.secret_key = 'секретно-секретный секрет'

@app.route("/menu")
def menu():
    return """
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Нестеренко Ирина, лабораторная 1</title>
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

                 <li>
                    <a href="/lab2">Лабораторная работа 2</a>
                </li>

                 <li>
                    <a href="/lab3">Лабораторная работа 3</a>
                </li>

                 <li>
                    <a href="/lab4">Лабораторная работа 4</a>
                </li>

                 <li>
                    <a href="/lab5">Лабораторная работа 5</a>
                </li>

                <li>
                    <a href="/rgz">РГЗ</a>
                </li>

            
            </ol>
        </div>

        <footer>
            &copy; Нестеренко Ирина, ФБИ-22, 3 курс, 2024 
        </footer>
    </body>
</html>
"""
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
