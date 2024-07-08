from wtforms import Form
from wtforms.fields import PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import email, DataRequired, equal_to

class LoginForm(Form):
  email = EmailField('Email address', validators=[email(), DataRequired()])
  pwd = PasswordField('Password', validators=[DataRequired()])

class RegisterForm(Form):
  email = EmailField('Email address', validators=[email(), DataRequired()])
  pwd = PasswordField('Password', validators=[DataRequired()])
  pwd_confirm = PasswordField('Confirm password', validators=[equal_to("pwd")])