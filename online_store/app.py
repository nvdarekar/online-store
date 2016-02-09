"""
	This is an application entry point.
	This file contains code for creating flask app and creating sqlalchemy of
	connection with postgres database.
"""

from flask import (Flask, request, render_template, jsonify)
from flask.ext.sqlalchemy import SQLAlchemy
from views.products import products_blueprint


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://online_store:password@localhost:5432/online_store"                                                      
app.config['SQLALCHEMY_ECHO'] = True 
app.config['UPLOAD_FOLDER'] = app.root_path + "/media"
db = SQLAlchemy(app)
app.register_blueprint(products_blueprint)


if __name__ == "__main__":
	app.run(threaded=True, debug=True)
    # app.run(threaded=True)
