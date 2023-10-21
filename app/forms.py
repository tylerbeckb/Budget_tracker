from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, ValidationError, SubmitField
from wtforms.validators import DataRequired, NumberRange
from app.models import Incomes, Expenditures, Goals


class IncomeForm(FlaskForm):
    name1 = StringField('Name1', validators=[DataRequired()])
    amount1 = DecimalField('Amount1', places=2, rounding=None, 
                           validators=[DataRequired(), NumberRange(min=0, max=None, message='Input must be positive')])
    submit = SubmitField('Submit')    

    def validate_name1(form, field):
        exists = Incomes.query.filter_by(name=field.data).first()
        if exists != None:
            raise ValidationError()

class ExpenditureForm(FlaskForm):
    name2 = StringField('Name2', validators=[DataRequired()])
    amount2 = DecimalField('Amount2', places=2, rounding=None, 
                           validators=[DataRequired(), NumberRange(min=0, max=None, message='Input must be positive')])
    submit3 = SubmitField('Submit')
    
    def validate_name2(form, field):
        exists = Expenditures.query.filter_by(name=field.data).first()
        if exists != None:
            raise ValidationError()

class EditIn(FlaskForm) :
    editName = StringField('editName', validators=[DataRequired()])
    newName = StringField('newName', validators=[DataRequired()])
    newAmount = DecimalField('newAmount', places=2, rounding=None, 
                           validators=[DataRequired(), NumberRange(min=0, max=None, message='Input must be positive')])
    submit2 = SubmitField('Submit') 

class EditEx(FlaskForm) :
    editName2 = StringField('editName2', validators=[DataRequired()])
    newName2 = StringField('newName2', validators=[DataRequired()])
    newAmount2 = DecimalField('newAmount2', places=2, rounding=None, 
                           validators=[DataRequired(), NumberRange(min=0, max=None, message='Input must be positive')])
    submit4 = SubmitField('Submit')
    
class addGoal(FlaskForm) :
    goalName = StringField('goalName')
    goalAmount = DecimalField('goalAmount', places=2, rounding=None, 
                              validators=[DataRequired(), NumberRange(min=0, max=None)])
    
    def validate_goalAmount(form, field):
        exists = Goals.query.filter_by().first()
        if exists != None:
            raise ValidationError()
    
class editGoal(FlaskForm) :
    editGoal = StringField('editGoal')
    editGoalAmount = DecimalField('editGoalAmount', places=2, rounding=None,
                                  validators=[DataRequired(), NumberRange(min=0, max=None)])
    
    def validate_editGoalAmount(form, field):
        exists = Goals.query.filter_by().first()
        if exists == None:
            raise ValidationError()

        