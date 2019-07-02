from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20, unique=True, nullable=False))
    image_file = db.Column(db.String(20),nullable=False, default='default.jpg')
    hash_pass = db.Column(db.String(255),nullable=False)

    def __repr__(self):
        return f"User ('{self.username}','{self.email}','{self.image_file}')"

class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    pitch_content = db.Column(db.String())
    pitch_category = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'