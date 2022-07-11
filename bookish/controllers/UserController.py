from flask import request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

from bookish.models.book_edition import BookEdition
from bookish.models.example import Example
from bookish.models import db

class UserController():

    def __init__(self, app):

        @app.route('/register', methods=['POST'])
        def register():
            if request.method == 'POST':
                if request.is_json:
                    data = request.get_json()
                    test = User.query.filter_by(email=email).first()

                    if test:
                        return {"message": "User already exists."}, 409
                    else:
                        new_user = User(data['username'], data['password'])
                        db.session.add(new_user)
                        db.session.commit()
                        return {"message": "New user has been created successfully."}
                else:
                    return {"error": "The request payload is not in JSON format"}

            else:
                return {"error": "Request method must be POST"}


        @app.route('/login', methods=['POST'])
        def login():
            if request.method == 'POST':
                if request.is_json:
                    data = request.get_json()
                    test = User.query.filter_by(username=username).first()

                    if test:
                        username = data["username"]
                        access_token = create_access_token(identity=username)
                        return {"message": "Login successful."
                                   , "access_token": access_token}, 201
                    else:
                        return {"message": "Incorrect email or password."}, 401
                else:
                    return {"error": "The request payload is not in JSON format"}

            else:
                return {"error": "Request method must be POST"}


