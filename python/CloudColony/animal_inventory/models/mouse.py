#!/usr/bin/env python
from sqlalchemy import Column
from sqlalchemy.types import VARCHAR

from CloudColony.database import db

from .base_model import BaseModel

class Mouse(BaseModel):
    __tablename__ = 'mice'
    name = db.Column(VARCHAR)




