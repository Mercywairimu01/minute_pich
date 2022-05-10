from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField
from wtforms.validators import DataRequired,Email,EqualTo
from app.models import User

class RegisterUserForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired(),EqualTo('confirm_password',message = 'Passwords must match')])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
	submit = SubmitField('Create Account')
 
	def validate_username(self,data_field):
		if User.query.filter_by(username = data_field.data).first():
			raise ValidationError('That username is taken')
 
	def validate_email(self, data_field):
	    if User.query.filter_by(email=data_field.data).first():
     		raise ValidationError('A user with that email address exists')
   	
class LoginUserForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember= BooleanField('Remember Me')
	login = SubmitField('Login In')