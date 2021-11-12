"""
Test Eiya
"""
import os

class Config():
    ORIGINS = ['*']
    SECRET_KEY = "0svaldo89!"

class DevelopConfig(Config):
    DEBUG = True
    PORT = 5000
    ENV = 'dev'
    HOST = '0.0.0.0'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@127.0.0.1:5432/eiya'
    SQLALCHEMY_TRACK_MODIFICATIONS = False