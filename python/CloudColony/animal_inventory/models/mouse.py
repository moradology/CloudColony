#!/usr/bin/env python
from sqlalchemy import Column
from sqlalchemy.types import VARCHAR

from lab_resources.database import db

from .thing import Thing

class Mouse(Thing):
    __tablename__ = 'mice'
    name = db.Column(VARCHAR)




