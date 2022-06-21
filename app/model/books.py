from app import db
import datetime

class Books(db.Model):
    index = db.Column(db.Integer, primary_key = True, autoincrement=True)
    book_id = db.Column(db.Text, unique = True, nullable = False)
    book_name = db.Column(db.Text, unique = True, nullable = False)
    book_author = db.Column(db.Text, nullable = False)
    book_path = db.Column(db.Text, unique = True, nullable = False)
    checksum = db.Column(db.Text, unique = True, nullable = False)
    create_datetime = db.Column(db.DateTime, nullable = False, default = datetime.datetime.now)

    def __init__(self, book_id, book_name, book_author, book_path, checksum):
        self.book_id = book_id
        self.book_name = book_name
        self.book_author = book_author
        self.book_path = book_path
        self.checksum = checksum