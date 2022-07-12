from flask import request

from bookish.models.book_edition import BookEdition
from bookish.models.example import Example
from bookish.models import db

class SearchBooksController():

    def __init__(self, app):

        @app.route('/search_title/<query_title>', methods=['GET'])
        def get_by_title(query_title):
            if request.method == 'GET':
                books = BookEdition.query.filter(BookEdition.title.ilike(query_title))
                results = [
                {
                    'isbn': book.isbn,
                    'title': book.title,
                    'author': book.author
                } for book in books]
                return {"books": results}

            else:
                return {"error": "Request method must be GET"}

        @app.route('/search_author/<query_author>', methods=['GET'])
        def get_by_author(query_author):
            if request.method == 'GET':
                books = BookEdition.query.filter(BookEdition.author.ilike(query_author))
                results = [
                {
                    'isbn': book.isbn,
                    'title': book.title,
                    'author': book.author
                } for book in books]
                return {"books": results}

            else:
                return {"error": "Request method must be GET"}



