import os
from app import create_app, db
from app.models import Category
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

# app.secret_key = 'dewtech'
config_name = os.getenv('FLASK_CONFIG')
app = create_app(os.getenv(config_name) or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app,db=db,User=User)

manager.add_command('shell', Shell(make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()