from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tutor(db.Model):
 
  id = db.Column(db.Integer,nullable=False, primary_key=True,)
  name= db.Column(db.String(100), nullable=False)
  phone =db.Column(db.String(14), nullable=False)
  city = db.Column(db.String(100), nullable=False)
  email= db.Column(db.String, nullable=False)
  password = db.Column(db.String, nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

