#!/usr/bin/env python

from CloudColony import app, db



if __name__ == "__main__":
    for table_name in db.metadata.tables:
        print("Creating table {0}".format(table_name))

    with app.app_context():
        db.create_all()
