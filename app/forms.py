from flask_wtf import FlaskForm
from wtforms import DecimalField
from wtforms.validators import DataRequired

class IncomeForm(FlaskForm):
    number1 = DecimalField('number1', places=2, rounding=None, validators=[DataRequired()])