from flask import (Blueprint, request, Response, render_template, jsonify)
from flask import send_from_directory
import os
import sys
import json
models_path = os.path.abspath(os.path.join('models'))
sys.path.append(models_path)

products_blueprint = Blueprint('products_blueprint', __name__,
                          template_folder='templates')

@products_blueprint.route("/products", methods=["GET", "POST"])
def products():
    """
        This is api endpoint for getting all products information in JSON on GET
        request and creating new proudct on post request
    """
    from models.products import Product
    if request.method == "GET":
        products = Product.get_all()
        return json.dumps(products)    
    if request.method == "POST":
        model_name = request.form.get('model-name')
        manufacturer = request.form.get('manufacturer')
        price = request.form.get('price')
        image_file = request.files['image']
        product = Product(model_name,manufacturer ,price, image_file)
        product.save()
        return Response("Created Successfully")

@products_blueprint.route("/products/<int:product_id>", methods=["PUT", "DELETE"])
def edit_products(product_id):
    return Response("Edit/Delete called for product " + str(product_id))
    pass


@products_blueprint.route("/", methods=["GET"])
def home():
    return render_template("products/index.html")

@products_blueprint.route("/new-product", methods=["GET"])
def create_new_product():
    return render_template("products/new_product.html")

@products_blueprint.route("/all-products", methods=["GET"])
def view_all_products():
    return render_template('products/all_products.html')

@products_blueprint.route('/media/images/<filename>')
def uploaded_image_file(filename):
    from app import app
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)