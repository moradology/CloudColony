#!/usr/bin/env python
from uuid import uuid4

from restless.fl import FlaskResource

from lab_resources.database import db
from ..models import Mouse

#from tracked_resources.models import Mouse

def fake_mice(number=1):
    def mouse_instance():
        return {
            'classification': {
                'kingdom': 'Animalia',
                'phylum': 'Chordata',
                'class': 'Mammalia',
                'order': 'Rodentia',
                'family': 'Muridae',
                'genus': 'Mus',
                'subgenus':'Mus'
            },
            'id': uuid4().hex
        }
    return [x() for x in [mouse_instance]*number]


class MouseResource(FlaskResource):
    def __init__(self, *args, **kwargs):
        super(MouseResource, self).__init__(*args, **kwargs)

    def is_authenticated(self):
        return True

    def list(self):
        db.session.add(Mouse())
        db.session.commit()
        return Mouse.query.all()


