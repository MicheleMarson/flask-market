from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from market.models import User



class RegisterForm(FlaskForm): # inherit from FlaskForm
  def validate_username(self, username_to_check): # flaskform understand that username is being validated by setting name to validate_username
    user = User.query.filter_by(username=username_to_check.data).first() # .data to reffr o data not object
    if user:
      raise ValidationError("Username already exists!")

  def validate_email_address(self, email_address_to_check):
    email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
    if email_address:
      raise ValidationError("Email address already exists!")
    

  username = StringField(label="Username:", validators=[Length(min=2, max=30), DataRequired()]) # label displayed using form.username.label()
  email_address = StringField(label="Email address:", validators=[Email(), DataRequired()])
  password1 = PasswordField(label="Password:", validators=[Length(min=6), DataRequired()])
  password2 = PasswordField(label="Confirm password:", validators=[EqualTo("password1"), DataRequired()])
  submit = SubmitField(label="Create Account")

class LoginForm(FlaskForm):
  username = StringField(label="User Name:", validators=[DataRequired()])
  password = StringField(label="Password:", validators=[DataRequired()])
  submit = SubmitField(label="Sign in")
