from os.path import dirname, abspath, join

from single_mod_app import db

_cwd = dirname(abspath(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(_cwd, 'flask_temp.db')

db.create_all()