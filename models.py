from app import db


class User(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    password = db.Column(db.String(60))

    def __init__(self, name, password):
        self.name = name
        self.password = password
