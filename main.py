import logging
from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import Tutor, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://lucas:@localhost/estudo'
db.init_app(app)


@app.get('/ping')
def ping():
    return 'pong', 200


@app.post('/new_tutor')
def create_new_tutor():
    data = request.get_json()
    if not all(key in data for key in ['name', 'phone', 'city', 'email', 'password']):
        abort(400, 'Missing fields')

    try:
        new = Tutor(name=data['name'], phone=data['phone'],
                    city=data['city'], email=data['email'], password=data['password'])
        db.session.add(new)
        db.session.commit()
        return 'New tutor created', 201

    except Exception as e:
        logging.error(str(e))
        return 'erro', 500


if __name__ == '__main__':
    app.run(debug=True)
