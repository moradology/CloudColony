#!/usr/bin/env python

from CloudColony import app, db

with app.app_context():
    db.create_all()
