# from bookish.controllers.bookish import bookish_routes
from bookish.controllers.HandleBooks import HandleBooks
from bookish.controllers.SearchBooks import SearchBooks
from bookish.controllers.UserController import UserController
from bookish.controllers.BookQueryController import BookQueryController
from flask_jwt_extended import JWTManager, jwt_required, create_access_token


def register_controllers(app):
    # bookish_routes(app)
    jwt = JWTManager(app)
    handle_books_controller = HandleBooks(app)
    search_books_controller = SearchBooks(app)
    book_query_controller = BookQueryController(app)
    user_controller = UserController(app)