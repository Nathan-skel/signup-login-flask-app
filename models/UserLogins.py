from db import db 

class UserLoginsModel(db.Model):
    __tablename__ = "userlogins"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)