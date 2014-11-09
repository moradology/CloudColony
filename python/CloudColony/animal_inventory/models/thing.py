#!/usr/bin/env python
from sqlalchemy import Column, Integer
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.sql import func

from CloudColony.database import db

class Thing(db.Model):
    __abstract__ = True

    id = db.Column(Integer, primary_key=True)
    created_at = db.Column(TIMESTAMP, default=func.now())
    updated_at = db.Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())





