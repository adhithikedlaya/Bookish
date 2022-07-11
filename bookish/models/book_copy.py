# from bookish.app import db
#
#
# class BookCopy(db.Model):
#     # This sets the name of the table in the database
#
#     # Here we outline what columns we want in our database
#     isbn = db.Column(db.String(), db.ForeignKey('BookEdition.isbn'))
#     book_key = db.Column(db.String(), primary_key=True)
#
#     def __init__(self, my_isbn):
#         self.isbn = my_isbn
#
#     def __repr__(self):
#         return '<book_key {}>'.format(self.book_key)
#
#     def serialize(self):
#         return {
#             'isbn': self.isbn,
#             'title': self.title,
#             'author': self.author
#         }