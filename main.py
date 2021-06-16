from flask import request, make_response, redirect, render_template
from app import create_app

todos = ['Comprar Cafe', 'Enviar slicitud de compra', 'Entregar producto']

app = create_app()


@app.route('/')
def index():
    """
    Set a default pagination of 25 people
    """
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    return response


@app.route('/hello')
def hellow():
    user_ip = request.cookies.get('user_ip')
    context = {'user_ip': user_ip, 'todos': todos}
    return render_template('hello.html', **context)


@app.errorhandler(404)
def not_foud(error):
    return render_template('404.html', error=error)
