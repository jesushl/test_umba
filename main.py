# internal python
import json
# flask app behavior
from flask import request, make_response, redirect, render_template, url_for
from app import create_app
# Database filler from git_hub
from scripts.seed import Seed
# custom commands
import click
# Config
from flask_migrate import Migrate

app = create_app()

migrate = Migrate(app, app.db)


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
    paginator_index = list(range(per_page))
    _ = zip(coders.items, paginator_index)
    paginator = coders
    return render_template(
        'coders.html',
        coders=_,
        paginator=paginator
    )


@app.route('/hello')
def hellow():
    user_ip = request.cookies.get('user_ip')
    context = {'user_ip': user_ip, 'todos': todos}
    return render_template('hello.html', **context)


@app.errorhandler(404)
def not_foud(error):
    return render_template('404.html', error=error)


# Api
@app.route('/api/users/profiles/')
def profiles():
    pagination = request.args.get('pagination', None, type=int)
    page = request.args.get('page', None, type=int)
    order_by = request.args.get('order_by', None, type=str)
    username = request.args.get('username', None, type=str)
    id = request.args.get('id', None, type=int)
    if (
        (not pagination) and
        (not page) and
        (not order_by) and
        (not username) and
        (not id)
    ):
        page = 1
        pagination = 25
    error_response = []
    if page:
        pagination_iter = Coder.query.paginate(page=page, per_page=pagination)
        return json_reponse(pagination_iter)
    if order_by:
        if order_by == 'id':
            _ = Coder.query.order_by(Coder.id).all()[pagination]
            return json_reponse(_)
        elif order_by == 'type':
            _ = Coder.query.order_by(Coder.type).all()[pagination]
            return json_reponse(_)
        else:
            error_response.append(
                "Only id or type are alowed on order_by filter"
            )
            return json.dups(error_response)
    if username:
        user = Coder.query.filter_by(username=username)
        return json.dumps({user})
    if id:
        user = Coder.query.filter_by(id=id)
        return json.dumps({user})


def json_reponse(pagination):
    list = [item for item in pagination.items]
    return json.dumps(list)


# CUSTOM COMMANDS
@app.cli.command("flask-script")
@click.argument("num_users")
@click.argument("since_id")
def flask_script(num_users=150, since_id=0):
    seed = Seed()
    users = seed.get_users(num_users=int(num_users), since_id=int(since_id))
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
    """
    Run this commant to send first data on database
    if your database is populated use
    flask db init fot a safe instance creation in docker
    """
    app.db.init_app()
    migrate.init_app(app.app, app.db)
    logging("database inits with 250 users")
    flask_script(num_users=250, since_id=0)


class Coder(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    username = app.db.Column(app.db.String(25), unique=True, nullable=False)
    avatar = app.db.Column(app.db.String(120), nullable=False)
    url = app.db.Column(app.db.String(120), unique=True, nullable=False)
    type = app.db.Column(app.db.String(5), nullable=False)

    def __repr__(self):
        return "{self.id}: {self.username}".format(self=self)
