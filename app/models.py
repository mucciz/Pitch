from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

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
    pitch_content = db.Column(db.String(255), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Pitch {self.title}, {self.date_posted}, {self.image_file}"