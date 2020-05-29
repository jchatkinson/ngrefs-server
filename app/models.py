from datetime import datetime
from dataclasses import dataclass
from app import db

@dataclass
class Post(db.Model):
    id: str
    body: str
    timestamp: str
    user_id: int

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

@dataclass
class User(db.Model):
    id: int
    username: str
    email: str
    password_hash: str
    posts: Post

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)   

@dataclass
class Form(db.Model):
    id: int
    name: str
    title: str
    subtitle: str
    imageUrl: str
    fields: str
    model: str
    output: str
    notes: str
    calcmethod: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    title = db.Column(db.String(64))
    subtitle = db.Column(db.String(64))
    imageUrl = db.Column(db.String(64))
    fields = db.Column(db.String(1024))
    model = db.Column(db.String(64))
    output = db.Column(db.String(64))
    notes = db.Column(db.String(64))
    calcmethod = db.Column(db.String(64))

    def __repr__(self):
        return '<Form {}>'.format(self.name)