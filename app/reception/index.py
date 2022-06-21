from flask import Blueprint, request, render_template, abort, redirect
import os
import configs
import shutil
import hashlib
import uuid

index_page = Blueprint('index', __name__, template_folder='templates')

@index_page.route('/')
def index():
    return render_template('index.html', books=getBooksInfo())

@index_page.route('/uploads', methods=['POST'])
def upload_file():
    books_tarball = request.files
    for book_tarball in books_tarball:
        uploaded_tarball = books_tarball.get(book_tarball)
        book_name = request.form['BookName']
        author_name =  request.form['Author']
        if uploaded_tarball.filename != '':
            file_ext = os.path.splitext(uploaded_tarball.filename)[1]
        if file_ext not in configs.ALLOWED_EXTENSIONS:
            abort(400)
        upload_destination = os.path.join(configs.UPLOAD_FOLDER, uploaded_tarball.filename)
        uploaded_tarball.save(upload_destination)
        extract_destination = os.path.join(configs.BOOK_FOLDER, book_name.lower().replace(' ', '-'))
        if not os.path.exists(extract_destination):
            os.makedirs(extract_destination)
        if file_ext == '.html':
            shutil.copy2(upload_destination, os.path.join(extract_destination, "index.html"))
        else:
            shutil.unpack_archive(upload_destination, extract_destination)
        file_checksum = hashlib.sha256(open(upload_destination, 'rb').read()).hexdigest()
        os.remove(upload_destination)

        from app.model.books import Books
        from app import db

        query_book = Books.query.filter(Books.checksum == file_checksum).first()
        if query_book is not None:
            abort(409)

        new_book = Books(str(uuid.uuid4()), book_name, author_name, extract_destination, file_checksum)
        db.session.add(new_book)
        db.session.commit()

    
    return render_template('index.html', books=getBooksInfo())

@index_page.route('/delete', methods=['GET'])
def delete_book():
    book_id = request.args.get('id')

    from app.model.books import Books
    from app import db

    query_book = Books.query.filter(Books.book_id == book_id).first()
    if query_book is None:
        abort(404)

    shutil.rmtree(query_book.book_path)
    db.session.delete(query_book)
    db.session.commit()
    
    return redirect("/")



def getBooksInfo():
    books = []

    from app.model.books import Books
    from app import db

    query_books = Books.query.all()

    for book in query_books:
        book_info = {}
        book_info['id'] = book.book_id
        book_info['name'] = book.book_name
        book_info['create-date'] = book.create_datetime.strftime("%Y-%m-%d %H:%M")
        book_info['folder-name'] = book.book_name.lower().replace(' ', '-')
        book_info['author'] = book.book_author
        books.append(book_info)

    return books