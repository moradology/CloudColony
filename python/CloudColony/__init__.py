#!/usr/bin/env python
import os.path

from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from flask.ext.sqlalchemy import SQLAlchemy

from .routes import register_routes
from .database import db

from .animal_inventory.models import Mouse


app = Flask(__name__)
app.config.from_object('CloudColony.settings.common.DevelopmentConfig')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://flask_cloud_colony:balrog@localhost/cloud_colony'
db.init_app(app)
register_routes(app)

app.wsgi_app = ProxyFix(app.wsgi_app)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()


