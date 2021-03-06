import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from main import app


app.app.config.from_object(os.environ['APP_SETTINGS'])
app.app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ['SQLALCHEMY_DATABASE_URI']
)

manager = Manager(app)
app.config['DEBUG'] = True
# Ensure debugger will load.


if __name__ == '__main__':
    manager.run()
