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
                    borrowed_dates = [borrowed.due_date for borrowed in borrowed_rows]
                    borrowed_isbns = [BookCopy.query.filter_by(book_id=borrowed.book_id).first() for borrowed in borrowed_rows]
                    borrowed_titles = [BookEdition.query.filter_by(isbn=borrowed.isbn).first().title for borrowed in borrowed_isbns]
                    joined_lists = zip()
                    results = [{
                        "title": title,
                        "due date": due_date
                    } for title, due_date in zip(borrowed_titles, borrowed_dates)]
                    return {"results": results}
                else:
                    return {"error": "The request payload is not in JSON format"}

            else:
                return {"error": "Request method must be POST"}

        @app.route('/num_copies/<int:query_isbn>', methods=['GET'])
        def get_num_copies(query_isbn):
            if request.method == 'GET':
                all_copies = BookCopy.query.filter_by(isbn=query_isbn)
                copy_ids = [copy.book_id for copy in all_copies]
                # print(copy_ids)
                total_num = len(copy_ids)
                borrowed_rows = []

                for each_id in copy_ids:
                    matching_book = Checkout.query.filter_by(book_id=each_id).first()
                    if matching_book:
                        borrowed_rows.append(matching_book)

                # print(borrowed_rows[0].book_id)
                # print(Checkout.query.filter_by(book_id=copy_ids[0]))
                # borrowed_rows = Checkout.query.filter_by(book_id=copy_id)
                print(borrowed_rows)
                borrowers = [User.query.filter_by(user_id=row.user_id).first().username for row in borrowed_rows]
                due_dates = [row.due_date for row in borrowed_rows]
                num_available = total_num - len(borrowed_rows)
                unavailable_books = [(entry[0], entry[1]) for entry in zip(borrowers, due_dates)]
                #print(unavailable_books)


                results = {
                    "total copies": total_num,
                    "available copies": num_available,
                    "unavailable book details": unavailable_books
                }

                # borrowed_info = [ {'username': User.query.filter(User.user_id.ilike(user_id)).username, 'due date': due_date} for (user_id, due_date) in borrowed]


                # return {"total number of copies": total_num, "number of available copies": num_available, "borrowed copies": borrowed_info}
                return results
            else:
                return {"error": "Request method must be GET"}


