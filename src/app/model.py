from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.config import Config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://informer:def@localhost/it_info'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Release(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(), nullable=False)
    service = db.Column(db.String(), nullable=False)
    theme = db.Column(db.String(), nullable=False)
    stand = db.Column(db.String(), nullable=False)
    responsible = db.Column(db.String(), nullable=False)
    sender = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'Row: |{self.id}|{self.date}|{self.service}|{self.theme}|{self.stand}|{self.responsible}|{self.sender}|'
