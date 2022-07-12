from flask import request

from bookish.models.book_edition import BookEdition, BookCopy
from bookish.models.checkout_table import Checkout
from bookish.models.user_table import User
from bookish.models.example import Example
from bookish.models import db

class BookQueryController():

    def __init__(self, app):

        @app.route('/checked_out', methods=['GET'])
        def checked_out():
            # Takes 'username'
            if request.method == 'GET':
                if request.is_json:
                    data = request.get_json()
                    user_id = User.query.filter_by(username=data["username"]).first().user_id
                    borrowed_rows = Checkout.query.filter_by(user_id=user_id).all()
                    query = db.session.query(Checkout, BookCopy, BookEdition).select_from(Checkout)\
                        .join(BookCopy, BookCopy.book_id==Checkout.book_id)\
                        .join(BookEdition, BookEdition.isbn==BookCopy.isbn)\
                        .add_columns(Checkout.due_date, BookEdition.title)\
                        .filter(Checkout.user_id==user_id).all()
                    borrowed_books = [(row.due_date, row.title) for row in query]
                    results = [{
                        "title": title,
                        "due date": str(due_date)
                    } for title, due_date in borrowed_books]
                    return {"results": results}
                else:
                    return {"error": "The request payload is not in JSON format"}

            else:
                return {"error": "Request method must be POST"}


        @app.route('/num_copies/<int:query_isbn>', methods=['GET'])
        def get_num_copies(query_isbn):
            if request.method == 'GET':

                total_num = BookCopy.query.filter_by(isbn=query_isbn).count()

                query = db.session.query(Checkout, BookCopy, User).select_from(Checkout) \
                    .join(BookCopy, BookCopy.book_id == Checkout.book_id) \
                    .join(User, Checkout.user_id == User.user_id)\
                    .add_columns(Checkout.due_date, User.username) \
                    .all()

                num_available = total_num - len(query)
                borrowed_books = [(row.username, row.due_date) for row in query]

                results = {
                    "total copies": total_num,
                    "available copies": num_available,
                    "unavailable book details": borrowed_books
                }

                return results
            else:
                return {"error": "Request method must be GET"}


