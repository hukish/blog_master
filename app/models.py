from . import db



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'





































































class Quote:

    def __init__(self, id, author, quote):
        self.id = id
        self.author = author
        self.quote = quote