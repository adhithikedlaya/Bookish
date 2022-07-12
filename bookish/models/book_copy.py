from bookish.app import db
class BookCopy(db.Model):
    # This sets the name of the table in the database
    __tablename__ = 'BookCopy'

    # Here we outline what columns we want in our database
    book_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.Integer, db.ForeignKey('BookEdition.isbn'))

    def __init__(self, my_isbn):
        self.isbn = my_isbn

    def __repr__(self):
        return '<book_id {}>'.format(self.book_id)