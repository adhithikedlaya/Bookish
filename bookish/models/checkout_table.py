from bookish.app import db

class Checkout(db.Model):
    # This sets the name of the table in the database
    __tablename__ = "Checkout"
    # Here we outline what columns we want in our database
    user_id = db.Column(db.Integer, db.ForeignKey("User.user_id"), primary_key=True)
    book_id = db.Column(db.Integer, primary_key=True)
    due_date = db.Column(db.DateTime())

    def __init__(self, my_user_id, my_book_key, my_due_date):
        self.user_id = my_user_id
        self.book_id = my_book_key
        self.due_date = my_due_date

    def __repr__(self):
        return f'<checkout: {self.user_id} {self.book_id}>'

    def serialize(self):
        return {
            'user_id': self.user_id,
            'book_id': self.book_id,
            'due_date': self.due_date
        }