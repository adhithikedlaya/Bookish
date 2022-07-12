from flask import request

from bookish.models.book_edition import BookEdition
from bookish.models.example import Example
from bookish.models import db

class HandleBooksController():

    def __init__(self, app):

        @app.route('/add_book', methods=['POST'])
        def add_book():
            if request.method == 'POST':
                if request.is_json:
                    data = request.get_json()
                    new_book = BookEdition(data['isbn'], data['title'], data['author'], data['book_copies'] )
                    db.session.add(new_book)
                    db.session.commit()
                    return {"message": "New book has been created successfully."}
                else:
                    return {"error": "The request payload is not in JSON format"}

            else:
                return {"error": "Request method must be POST"}


        @app.route('/catalogue', methods=['GET'])
        def get_catalogue():
            if request.method == 'GET':
                books = BookEdition.query.all()
                results = [
                    {
                        'isbn': book.isbn,
                        'title': book.title,
                        'author': book.author
                    } for book in books]
                return {"books": results}
            else:
                return {"error": "Request method must be GET"}




