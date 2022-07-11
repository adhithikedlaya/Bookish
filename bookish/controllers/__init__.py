# from bookish.controllers.bookish import bookish_routes
from bookish.controllers.HandleBooks import HandleBooks
from bookish.controllers.SearchBooks import SearchBooks
from bookish.controllers.UserController import UserController
#import bookish.controllers.SearchBooks

def register_controllers(app):
    # bookish_routes(app)
    handle_books_controller = HandleBooks(app)
    search_books_controller = SearchBooks(app)
    user_controller = UserController(app)