from bookish.app import db
from bookish.models.book_copy import BookCopy


class BookEdition(db.Model):
    # This sets the name of the table in the database
    __tablename__ = 'BookEdition'

    # Here we outline what columns we want in our database
    isbn = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    author = db.Column(db.String())
    book_copies = db.relationship('BookCopy', backref='edition', lazy='dynamic')

    def __init__(self, my_isbn, my_title, my_author, my_book_copies):
        self.isbn = my_isbn
        self.title = my_title
        self.author = my_author
        self.book_copies = [BookCopy(my_isbn) for _ in range(my_book_copies)]

    def __repr__(self):
        return '<isbn {}>'.format(self.isbn)

