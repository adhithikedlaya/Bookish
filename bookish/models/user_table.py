from bookish.app import db


class User(db.Model):
    # This sets the name of the table in the database
    __tablename__ = 'User'
    # Here we outline what columns we want in our database
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    user_checkouts = db.relationship("Checkout", backref="user", lazy="dynamic")

    def __init__(self, my_username, my_password):
        self.username = my_username
        self.password = my_password

    def __repr__(self):
        return '<user_id {}>'.format(self.user_id)

    def serialize(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'password': self.password
        }