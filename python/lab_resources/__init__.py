#!/usr/bin/env python
import os.path

from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from flask.ext.sqlalchemy import SQLAlchemy

from .routes import register_routes
from .database import db

from .animal_inventory.models import Mouse


app = Flask(__name__)
app.config.from_object('lab_resources.settings.common.DevelopmentConfig')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)
register_routes(app)

app.wsgi_app = ProxyFix(app.wsgi_app)


def setup_database(app):
    with app.app_context():
        db.create_all()
        mouse = Mouse()
        mouse.name = "X11"
        db.session.add(mouse)
        db.session.commit()

if __name__ == "__main__":
    app = initiate_labapp()
    setup_database(app)
    app.run()


