#!/usr/bin/env python
from uuid import uuid4

from restless.fl import FlaskResource
from restless.preparers import FieldsPreparer

from CloudColony.database import db
from ..models import Mouse


class BaseResource(FlaskResource):
    """Base resource for any models which use the UUID for column: id"""

    model = None

    def prepare(self, data):
        prepped = super(BaseResource, self).prepare(data)
        prepped['id'] = str(prepped['id'])
        return prepped

    def is_authenticated(self):
        return True

    def list(self):
        """Base list to be overridden for non-standard list management"""
        return self.model.query.all()

    def detail(self, pk):
        """Base detail to be overridden for non-standard list management"""
        return self.model.query.get(pk)

    def create(self):
        db.session.add(self.model())
        db.session.commit()
        return
