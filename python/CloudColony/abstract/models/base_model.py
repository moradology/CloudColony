#!/usr/bin/env python
import uuid

from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import DateTime
from sqlalchemy.sql import func

from ...database import db


class BaseModel(db.Model):
    """Base model which uses UUID for id column"""
    __abstract__ = True

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = db.Column(DateTime(timezone=True), default=func.now())
    updated_at = db.Column(DateTime(timezone=True), default=func.now(),
                           onupdate=func.current_timestamp())





