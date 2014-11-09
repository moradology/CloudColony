#!/usr/bin/env python
from sqlalchemy import Column
from sqlalchemy.types import String

from ...database import db

class OrganismMixin(object):
    """A living thing of some sort"""
    name = db.Column(String(length=40))
    bio_domain = db.Column(String(length=40))
    bio_kingdom = db.Column(String(length=40))
    bio_phylum = db.Column(String(length=40))
    bio_class = db.Column(String(length=40))
    bio_order = db.Column(String(length=40))
    bio_family = db.Column(String(length=40))
    bio_genus = db.Column(String(length=40))
    bio_species = db.Column(String(length=40))
    bio_subspecies = db.Column(String(length=40))




