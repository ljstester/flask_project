from datetime import datetime

from exts import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(20), nullable=True)
    phone = db.Column(db.String(11), nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.now())
