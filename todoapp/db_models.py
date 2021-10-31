from sqlalchemy.orm import backref
from todoapp import db
from todoapp import UserMixin

class User(UserMixin ,db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(65), nullable=False)
    list = db.relationship('AddToList', backref='author', lazy=True)

    def __repr__(self):
        return f"{self.username}, {self.password}"


class AddToList(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    string = db.Column(db.String(1000000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"{self.string}, {self.user_id}"

