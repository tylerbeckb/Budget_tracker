from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField
from wtforms.validators import DataRequired, NumberRange


class IncomeForm(FlaskForm):
    name1 = StringField('Name1', validators=[DataRequired()])
    amount1 = DecimalField('Amount1', places=2, rounding=None, 
                           validators=[DataRequired(), NumberRange(min=0, max=None, message='Input must be positive')])

class ExpenditureForm(FlaskForm):
    name2 = StringField('Name2', validators=[DataRequired()])
    amount2 = DecimalField('Amount2', places=2, rounding=None, 
                           validators=[DataRequired(), NumberRange(min=0, max=None, message='Input must be positive')])

class EditIn(FlaskForm) :
    editName = StringField('editName', validators=[DataRequired()])
    newName = StringField('newName', validators=[DataRequired()])
    newAmount = DecimalField('newAmount', places=2, rounding=None, 
                           validators=[DataRequired(), NumberRange(min=0, max=None, message='Input must be positive')])


    
 