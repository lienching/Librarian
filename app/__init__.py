from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.reception.index import index_page
from app.reception.book import book_page
import configs
import os

app = Flask(__name__, static_url_path='', static_folder='static/')
app.config['UPLOAD_FOLDER'] = configs.UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = configs.ALLOWED_EXTENSIONS

# Build required directory if needed
if not os.path.exists(configs.UPLOAD_FOLDER):
    os.makedirs(configs.UPLOAD_FOLDER)

if not os.path.exists(configs.BOOK_FOLDER):
    os.makedirs(configs.BOOK_FOLDER)

if not os.path.exists(configs.DATABASE_PATH):
    os.makedirs(configs.DATABASE_PATH)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = configs.DATABASE_URI
db = SQLAlchemy(app)

from app.model.books import *
db.create_all()

app.register_blueprint(index_page)
app.register_blueprint(book_page)
