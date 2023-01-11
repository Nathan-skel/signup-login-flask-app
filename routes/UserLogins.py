from flask_smorest import Blueprint
from flask import render_template, redirect, url_for, request
from flask.views import MethodView
from models import UserLoginsModel
from schemas import UserLoginsSchema, UpdateUserLoginsSchema
from db import db

blp = Blueprint("UserLogins", __name__, description="Gets Login Data")

@blp.route("/user/<string:UserID>")
class UserLogin(MethodView):
    
    @blp.response(200, UserLoginsSchema)
    def get(self, UserID):
        return UserLoginsModel.query.get_or_404(UserID)
    
    @blp.arguments(UpdateUserLoginsSchema)
    @blp.response(200, UserLoginsSchema)
    def put(self,  UpdateUserData, UserID):
        User = UserLoginsModel.query.get(UserID)
        if User:
            User.username = UpdateUserData['username']
            User.password_hash = UpdateUserData['password_hash']
            User.email = UpdateUserData['email']
        else:
            User = UserLoginsModel(id=UserID, **UpdateUserData)
        
        db.session.add(User)
        db.session.commit()
        
        return User


@blp.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        User = UserLoginsModel.query.filter_by(username=request.form['username']).first()
        if User:
            if User.password_hash == request.form['password']:
                print("Logged In")
        
    return render_template('login.html', error=error)



@blp.route("/signup", methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        if len(request.form['username']) != 0 and len(request.form['password']) != 0 and len(request.form['email']) != 0:
            User = UserLoginsModel(username=request.form['username'], password_hash=request.form['password'], email=request.form['email'])
            db.session.add(User)
            db.session.commit()
            
        
    return render_template('signup.html', error=error)