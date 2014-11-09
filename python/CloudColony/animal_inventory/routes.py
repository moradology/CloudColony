#!/usr/bin/env python

from CloudColony import app

from .resources import MouseResource


MouseResource.add_url_rules(app, rule_prefix='/api/mice/')


