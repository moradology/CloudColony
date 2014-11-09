#!/usr/bin/env python
from uuid import uuid4

from restless.fl import FlaskResource
from restless.preparers import FieldsPreparer

from CloudColony.database import db
from ..models import Mouse

from .base_resource import BaseResource


class MouseResource(BaseResource):
    model = Mouse
    preparer=FieldsPreparer(fields={
        'id': 'id',
        'name': 'name',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    })

    def create(self):
        db.session.add(self.model(name="TestMouse"))
        db.session.commit()
        return




