from flask import request, make_response, redirect, render_template, url_for
from app import create_app
# Database filler from git_hub
from scripts.seed import Seed
# custom commands
import click

# Config
from flask_migrate import Migrate

app = create_app()

migrate =Migrate(app, app.db)

@app.route('/')
def index():
    """
    Set a default pagination of 25 people
    """
    return redirect(url_for('users_by_pagination', page=1))


@app.route('/users/<int:page>')
def users_by_pagination(page):
    per_page = request.args.get('pagination', 25, type=int)
    coders = Coder.query.paginate(page=page, per_page=per_page)
    print(coders)
    return render_template(
        'coders.html',
        coders=coders
    )


@app.route('/hello')
def hellow():
    user_ip = request.cookies.get('user_ip')
    context = {'user_ip': user_ip, 'todos': todos}
    return render_template('hello.html', **context)


@app.errorhandler(404)
def not_foud(error):
    return render_template('404.html', error=error)


# CUSTOM COMMANDS
@app.cli.command("flask-script")
@click.argument("num_users")
def flask_script(num_users=150):
    seed = Seed()
    users = seed.get_users(num_users=int(num_users))
    for user in users:
        try:
            app.db.session.add(
                Coder(
                    id=user.get('id'),
                    username=user.get('login', ''),
                    avatar=user.get('avatar_url', ''),
                    type=user.get('type', ''),
                    url=user.get('url', '')
                )
            )
            app.db.session.commit()
        except Exception as error:
            # Integrity safe for ids
            pass


@app.cli.command("init")
def app_init():
    app.db.create_all()


class Coder(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    username = app.db.Column(app.db.String(25), unique=True, nullable=False)
    avatar = app.db.Column(app.db.String(120), nullable=False)
    url = app.db.Column(app.db.String(120), unique=True, nullable=False)
    type = app.db.Column(app.db.String(5), nullable=False)

    def __repr__(self):
        return "{self.username} {self.user}"
