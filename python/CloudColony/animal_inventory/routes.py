#!/usr/bin/env python

from CloudColony import app

from .api import MouseResource


MouseResource.add_url_rules(app, rule_prefix='/api/mice/')


