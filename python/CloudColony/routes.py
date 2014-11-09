#!/usr/bin/env python

from .animal_inventory.api import MouseResource

def register_routes(app):
    """Register routes below to provided app"""
    MouseResource.add_url_rules(app, rule_prefix='/api/mice/')


