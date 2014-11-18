#!/usr/bin/env python
from sqlalchemy import Column
from sqlalchemy.types import VARCHAR

from ...database import db
from ...abstract.models import BaseModel
from ...abstract.models.mixins import LitterMixin, LivingMixin
from ...cages.models.mixins import CagedMixin

class Mouse(CagedMixin, LivingMixin, BaseModel):
    __tablename__ = 'mice'




