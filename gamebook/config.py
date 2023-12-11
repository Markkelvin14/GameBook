import os
from sqlalchemy import create_engine

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY')
	engine = create_engine('postgresql+psycopg2://postgres:mark@localhost/gamebookdbs')
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('COMP_EMAIL')
	MAIL_PASSWORD = os.environ.get('COMP_PASS')
