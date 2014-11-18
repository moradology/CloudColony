#!/usr/bin/env python
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from ....database import db


class CagedMixin(db.Model):
    """Mixin for caged animals"""
    __abstract__ = True

    @declared_attr
    def cage_id(self):
        return db.Column(UUID, ForeignKey('cages.id'))





