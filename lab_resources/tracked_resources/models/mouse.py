#!/usr/bin/env python
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel(Base):
    id = Column(Integer, primary_key=True)





