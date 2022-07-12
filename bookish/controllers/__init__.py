from bookish.controllers.HandleBooksController import HandleBooksController
from bookish.controllers.SearchBooksController import SearchBooksController
from bookish.controllers.UserController import UserController
from bookish.controllers.BookQueryController import BookQueryController
from flask_jwt_extended import JWTManager, jwt_required, create_access_token


def register_controllers(app):
    jwt = JWTManager(app)
    handle_books_controller = HandleBooksController(app)
    search_books_controller = SearchBooksController(app)
    book_query_controller = BookQueryController(app)
    user_controller = UserController(app)