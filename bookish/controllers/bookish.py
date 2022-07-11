from flask import request

from bookish.models.book_edition import BookEdition
from bookish.models.example import Example
from bookish.models import db


def bookish_routes(app):
    @app.route('/healthcheck')
    def health_check():
        return {"status": "OK"}

    @app.route('/example', methods=['POST', 'GET'])
    def handle_example():
        if request.method == 'POST':
            if request.is_json:
                data = request.get_json()
                new_example = Example(data['data1'], data['data2'])
                db.session.add(new_example)
                db.session.commit()
                return {"message": "New example has been created successfully."}
            else:
                return {"error": "The request payload is not in JSON format"}

        elif request.method == 'GET':
            examples = Example.query.all()
            results = [
                {
                    'id': example.id,
                    'data1': example.data1,
                    'data2': example.data2
                } for example in examples]
            return {"examples": results}


    @app.route('/book_entry', methods=['POST', 'GET'])
    def handle_book():
        if request.method == 'POST':
            if request.is_json:
                data = request.get_json()
                new_book = BookEdition(data['isbn'], data['title'], data['author'], data['book_copies'] )
                db.session.add(new_book)
                db.session.commit()
                return {"message": "New book has been created successfully."}
            else:
                return {"error": "The request payload is not in JSON format"}

        elif request.method == 'GET':
            books = BookEdition.query.all()
            results = [
                {
                    'isbn': book.isbn,
                    'title': book.title,
                    'author': book.author
                } for book in books]
            return {"books": results}




