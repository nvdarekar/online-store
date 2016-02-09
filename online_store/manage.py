""" 
This file is contains the code for database schema migration using 
Flask-Migrate extension. Flask-Migrate uses alembic. 
"""


from flask.ext.sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models.products import Product
from app import app, db

if __name__ == "__main__":
	migrate = Migrate(app, db)
	manager = Manager(app)
	manager.add_command('db', MigrateCommand)
	manager.run()