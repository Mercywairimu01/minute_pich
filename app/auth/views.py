from flask import  render_template,url_for,flash,redirect,request
from . import auth
from ..email import mail_message
from .forms import LoginUserForm,RegisterUserForm
from ..models import User
from flask_login import login_user,login_required,logout_user
from .. import db

@auth.route('/login', methods =['GET','POST'])
def login():
    login_form = LoginUserForm()
    
    if login_form.validate_on_submit():
        user=User.query.filter_by(username =login_form.username.data).first()
        
        if user != None and user.verify_password(login_form.password.data):
           login_user(user,login_form.remember.data)
           return redirect(request.args.get('next') or url_for('main.index'))
       
        flash('Invalid username or Password')
    
    return render_template('auth/login.html', login_form = login_form)

@auth.route('/registration', methods =['GET','POST'])
def registration():
    registration_form = RegisterUserForm()
    if registration_form.validate_on_submit():
        user = User(email = registration_form.email.data, username = registration_form.username.data,password = registration_form.password.data)
        user.save_user()
        # db.session.add(user)
        # db.session.commit()

        mail_message("Welcome to Minute Pitch","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))
        
    return render_template('auth/reg.html', registration_form = registration_form)
    
    
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

