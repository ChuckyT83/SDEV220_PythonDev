from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)



class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(40), unique=False, nullable=False)
    publisher = db.Column(db.String(30), unique=False, nullable=False)

    def __repr__(self):
        return f"{self.book_name} - Author: {self.author} Publisher: {self.publisher}"
    
@app.route("/")
def index():
    return "Welcome to the book list"

#After watching the video, create a CRUD API for a Book instead of a Drink in the video example above.  The Book model should have the following parameters:
# id
# book_name
# author
# publisher

@app.route("/books")
def get_books():
    books = Book.query.all()

    output = []

    for book in books:
        book_data = {"book_name": book.book_name, "author": book.author, "publisher": book.publisher}

        output.append(book_data)

    return {"books": output}

@app.route("/books", methods=["POST"])
def add_book():
    book = Book(book_name=request.json['book_name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route("/books/<id>", methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "book not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "Book deleted."}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return ({"book_name": book.book_name, "author": book.author, "publisher": book.publisher})

