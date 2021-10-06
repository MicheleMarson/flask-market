from market import db

class User(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  username = db.Column(db.String(length=50), unique=True, nullable=False)
  email_address = db.Column(db.String(length=50), unique=True, nullable=False)
  password_hash = db.Column(db.String(length=60), nullable=False)
  budget = db.Column(db.Integer(), nullable=False, default=1000)
  items = db.relationship("Item", backref='owned_user', lazy=True) 


class Item(db.Model): # db table
  id = db.Column(db.Integer(), primary_key=True)
  price = db.Column(db.Integer(), nullable=False)
  name = db.Column(db.String(length=30), nullable=False, unique=True)
  barcode = db.Column(db.String(length=12), nullable=False, unique=True)
  description = db.Column(db.String(length=1000), nullable=False, unique=True)
  owner = db.Column(db.Integer(), db.ForeignKey('user.id')) # related to id
  
  def __repr__(self): # special method used to represent a class's objects as a string
    return f'Item {self.name}'