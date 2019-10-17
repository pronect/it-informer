from flask import Flask
from flask import request, jsonify

from src.app.model import db, Release

app = Flask(__name__)


@app.route('/')
def start_page():
    return 'WELCOME'


@app.route('/add', methods=['POST'])
def take_fields():
    """Принимает поля из слака"""
    data = request.get_json()
    try:
        #id = data['id']
        date = data['date']
        service = data['service']
        theme = data['theme']
        stand = data['stand']
        responsible = data['responsible']
        sender = data['sender']
        row = Release(#id=id,
                      date=date,
                      service=service,
                      theme=theme,
                      stand=stand,
                      responsible=responsible,
                      sender=sender)
        db.session.add(row)
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        return 'ok?'
            #jsonify(Release.query.all()), 200


