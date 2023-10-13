from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField, StringField
from wtforms.validators import DataRequired, NumberRange


class IncomeForm(FlaskForm):
    name = StringField('Name')
    amount = DecimalField('Amount', places=2, rounding=None, 
                           validators=[DataRequired(), NumberRange(min=0, max=None, message='Input must be positive')])
    submit = SubmitField('Submit')

class ExpenditureForm(FlaskForm):
    name = StringField('Name')
    amount = DecimalField('Amount', places=2, rounding=None, 
                           validators=[DataRequired(), NumberRange(min=0, max=None, message='Input must be positive')])
    submit = SubmitField('Submit')

    
 