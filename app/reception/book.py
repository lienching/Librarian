from flask import Blueprint, send_from_directory
from jinja2 import TemplateNotFound
import configs
import os

book_page = Blueprint('book', __name__, url_prefix='/book')

@book_page.route('/<book_name>/<path:filename>', methods=['GET'])
def get_pages(book_name, filename):
    return send_from_directory(os.path.join(configs.BOOK_FOLDER, book_name), filename)