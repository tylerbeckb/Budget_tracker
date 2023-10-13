from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired, ValidationError, NumberRange


class IncomeForm(FlaskForm):
    number1 = DecimalField('number1', places=2, rounding=None, 
                           validators=[DataRequired(), NumberRange(min=0, max=None, message='Input must be positive')])
    submit = SubmitField('Submit')
    
 