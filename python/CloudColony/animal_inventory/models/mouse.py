#!/usr/bin/env python
from sqlalchemy import Column
from sqlalchemy.types import VARCHAR

from ...database import db
from ...abstract.models import BaseModel, OrganismMixin

class Mouse(OrganismMixin, BaseModel):
    __tablename__ = 'mice'




