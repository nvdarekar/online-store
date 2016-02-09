import os
from flask import url_for
from werkzeug import secure_filename
from app import app, db
from .meta.base import Base

class Product(db.Model, Base):

	""" 
		This model is used to store information of products 
	"""
	
	__tablename__ = 'products'

	id = db.Column(db.Integer, primary_key=True)
	model_name = db.Column(db.Unicode(200), nullable=False)
	manufacturer = db.Column(db.Unicode(200), nullable=False)
	price = db.Column(db.Float, nullable=False)
	image_url = db.Column(db.Unicode(200), nullable=True)
	

	def __init__(self, model_name, manufacturer, price, image_file):
		self.model_name = model_name
		self.manufacturer = manufacturer
		self.price = price
		if image_file and allowed_file(image_file.filename):
			filename = secure_filename(image_file.filename)
			image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			self.image_url = "/media/images/" + filename
	
	@classmethod
	def get_all(cls):
	 	products = Product.query.all()
	 	products_json = [product._asdict() for product in products]
	 	return products_json 


ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS