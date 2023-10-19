from app import db

class Incomes(db.Model):
    name = db.Column(db.String(500), index=True, unique=True, primary_key=True)
    amount = db.Column(db.Float)

class Expenditures(db.Model):
    name = db.Column(db.String(500), index=True, unique=True, primary_key=True)
    amount = db.Column(db.Float)

class Goals(db.Model):
    name = db.Column(db.String(500), index=True)
    amount = db.Column(db.Float, primary_key=True)
   
