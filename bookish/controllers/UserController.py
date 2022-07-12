from flask import request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

import datetime

from bookish.models.user_table import User
from bookish.models.example import Example
from bookish.models.book_edition import BookCopy, BookEdition
from bookish.models import db
from bookish.models.checkout_table import Checkout

class UserController():

    def __init__(self, app):

        @app.route('/register', methods=['POST'])
        def register():
            # Takes 'username', 'password'
            if request.method == 'POST':
                if request.is_json:
                    data = request.get_json()
                    username = data['username']
                    test_user = User.query.filter_by(username=username).first()

                    if test_user:
                        return {"message": "User already exists."}, 409
                    else:
                        new_user = User(username, data['password'])
                        db.session.add(new_user)
                        db.session.commit()
                        return {"message": "New user has been created successfully."}
                else:
                    return {"error": "The request payload is not in JSON format"}

            else:
                return {"error": "Request method must be POST"}


        @app.route('/login', methods=['POST'])
        def login():
            # Takes 'username', 'password'
            if request.method == 'POST':
                if request.is_json:
                    data = request.get_json()
                    username = data['username']
                    test_user = User.query.filter_by(username=username).first()
                    password = data['password']
                    if test_user and test_user.password == password:
                        access_token = create_access_token(identity=username)
                        return {"message": "Login successful."
                                   , "access_token": access_token}, 201
                    else:
                        return {"message": "Incorrect username or password."}, 401
                else:
                    return {"error": "The request payload is not in JSON format"}

            else:
                return {"error": "Request method must be POST"}


        @app.route('/borrow_book', methods=['POST'])
        def borrow_book():
            # Takes 'username', 'isbn'
            if request.method == 'POST':
                if request.is_json:
                    data = request.get_json()
                    user_id = User.query.filter_by(username=data["username"]).first().user_id
                    due_date = datetime.datetime.now() + datetime.timedelta(days=28)

                    copies = BookEdition.query.filter_by(isbn=data["isbn"]).first().book_copies
                    potential_keys = [copy.book_id for copy in copies]

                    first_available = False
                    for i in range(0, len(potential_keys)):
                        if not Checkout.query.filter_by(book_id=potential_keys[i]).first():
                            first_available = True
                            break

                    if first_available:
                        book_key = potential_keys[i]
                    else:
                        return {"message": "No available copies."}

                    borrow_entry = Checkout(user_id, book_key, due_date)
                    db.session.add(borrow_entry)
                    db.session.commit()
                    return {"message": "Book was borrowed successfully."}
                else:
                    return {"error": "The request payload is not in JSON format"}

            else:
                return {"error": "Request method must be POST"}




