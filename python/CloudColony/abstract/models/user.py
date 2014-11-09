#!/usr/bin/env python
from sqlalchemy import Column
from sqlalchemy.types import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_utils.types.timezone import TimezoneType


from .base_model import BaseModel
from ...database import db

class AbstractUser(BaseModel):
    """A living thing of some sort"""
    __abstract__ = True
    username = db.Column(db.String(80), unique=True)
    password = db.Column(PasswordType(max_length=150, schemes=['pbkdf2_sha512', 'md5_crypt'],
                          deprecated=['md5_crypt']))

    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class TZMixin(object):
    """A mixin to give permissions"""
    timezone = db.Column(TimezoneType(backend='pytz'))

class PermsMixin(object):
    """A mixin to give permissions"""
    pass



