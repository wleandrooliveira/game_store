import os
import sys
import click

from app import create_app, db
# app.secret_key = 'dewtech'

config_name = os.getenv('FLASK_CONFIG')
app = create_app(os.getenv(config_name) or 'default')

if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)



