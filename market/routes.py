from werkzeug.utils import redirect
from market import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from market import db

@app.route("/")
@app.route("/home")
def home_page():
  return render_template("home.html")


@app.route("/market")
def market_page():
  items = Item.query.all() # returns all objects in items we created in shell

  return render_template("market.html", items = items) # flask understands templates directory

@app.route("/register", methods=["GET", "POST"])
def register_page():
  form = RegisterForm()
  if form.validate_on_submit(): # Call validate only if the form is submitted
    user_to_create = User(
      username=form.username.data,
      email_address=form.email_address.data,
      password=form.password1.data # from @password.setter
    )
    db.session.add(user_to_create)
    db.session.commit()
    return redirect(url_for("market_page")) # after registration, redirect to market page
  if form.errors != {}: # if there are no errors fom the validations
    for err_msg in form.errors.values():
      flash(f"There was an error with creating user{err_msg}", category="danger") # to display info
  return render_template("register.html", form = form)
# gather all the flash messages with get_flashed_messages

@app.route("/login", methods=["GET", "POST"])
def login_page():
  form = LoginForm()
  return render_template("login.html", form=form)