from flask import Flask, jsonify
from flask_pymongo import PyMongo

USER="admin"
PASSWORD="vital"
DB_NAME="vitalHealthDB"
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@cluster0.8kl8u.mongodb.net/{DB_NAME}?retryWrites=true&w=majority"

app = Flask(__name__)
mongo = PyMongo(app, uri=MONGO_URI)



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/products")
def get_products():
    products = mongo.db.products.find({})
    product_list = [to_json(product) for product in products]
    return jsonify(product_list)
    
def to_json(product):
    product["_id"] = str(product["_id"])
    return product

@app.route('/featuresProduct')
def post_features product():
    features = request.form['features product']
    return features
