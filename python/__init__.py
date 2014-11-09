#!/usr/bin/env python
from CloudColony import app
from CloudColony.database import db




if __name__ == "__main__":
    db.init_app(app)
    db.create_all()
    app.run(port=81)

