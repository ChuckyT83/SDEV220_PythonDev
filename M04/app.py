from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)


#creates Book class for SQLAlchemy entries
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(40), unique=False, nullable=False)
    publisher = db.Column(db.String(30), unique=False, nullable=False)

    def __repr__(self):
        return f"{self.book_name} - Author: {self.author} Publisher: {self.publisher}"

#returns text at index page
@app.route("/")
def index():
    return "Welcome to the book list"

#returns the book list at /books
@app.route("/books")
def get_books():

    #queries the book database
    books = Book.query.all()
    output = []

    #iterates through the book database query and adds each entry to the output list
    for book in books:
        book_data = {"book_name": book.book_name, "author": book.author, "publisher": book.publisher}

        output.append(book_data)

    return {"books": output}


#adds a new book when a JSON is sent with the correct parameters
@app.route("/books", methods=["POST"])
def add_book():
    book = Book(book_name=request.json['book_name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

#deletes a book entry when request to delete is sent to a specific book id
@app.route("/books/<id>", methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "book not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "Book deleted."}

#returns specific book based on book id
@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return ({"book_name": book.book_name, "author": book.author, "publisher": book.publisher})

