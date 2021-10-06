from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class RegisterForm(FlaskForm): # inherit from FlaskForm
  username = StringField(label="Username:", validators=[Length(min=2, max=30), DataRequired()]) # label displayed using form.username.label()
  email_address = StringField(label="Email address:", validators=[Email(), DataRequired()])
  password1 = PasswordField(label="Password:", validators=[Length(min=6), DataRequired()])
  password2 = PasswordField(label="Confirm password:", validators=[EqualTo("password1"), DataRequired()])
  submit = SubmitField(label="Create Account")