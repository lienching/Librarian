# Port to listen on
PORT=39433

# Define the application directory
import os
BASE_DIR = "/opt/librarian"
DATABASE_PATH = os.path.join(BASE_DIR, "db")

# Database URI
DATABASE_URI = 'sqlite:///' + os.path.join(DATABASE_PATH, 'books.db')

# Allowed Extensions
ALLOWED_EXTENSIONS = ['.tar', '.zip', '.tar.xz', '.tar.gz', '.tar.bz', '.html']

# Upload Directory
UPLOAD_FOLDER = "/opt/librarian/uploads"

# Book Directory
BOOK_FOLDER = "/opt/librarian/books"