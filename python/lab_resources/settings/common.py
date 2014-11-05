#!/usr/bin/env python
import os

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True


class ProductionConfig(BaseConfig):
    DEBUG = False


class StagingConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True

