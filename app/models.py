from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20),nullable=False, default='default.jpg')
    hash_pass = db.Column(db.String(255),nullable=False)

    def __repr__(self):
        return f"User ('{self.username}','{self.email}','{self.image_file}')"

class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    pitch_title = db.Column(db.String(100),nullable=False)
    pitch_category = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime)

    def __repr__(self):
        return f'User {self.username}'