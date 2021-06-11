from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

todos = ['Comprar Cafe', 'Enviar slicitud de compra', 'Entregar producto']

@app.route('/')
def index():
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