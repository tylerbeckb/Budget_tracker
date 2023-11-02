from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, ValidationError, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length
from app.models import Incomes, Expenditures, Goals

# Add Income Form
class IncomeForm(FlaskForm):
    name1 = StringField('Name1', validators = [DataRequired(), 
                                                Length(min = 0, max = 20)])
    amount1 = DecimalField('Amount1', places = 2, rounding = None, 
                            validators = [DataRequired(), 
                                NumberRange(min = 0, max = 10000000)])
    submit = SubmitField('Submit')    


    def validate_name1(form, field):
        exists = Incomes.query.filter_by(name = field.data).first()
        if exists != None:
            raise ValidationError()

# Add Expenditure form
class ExpenditureForm(FlaskForm):
    name2 = StringField('Name2', validators = [DataRequired(), 
                                                Length(min = 0, max = 20)])
    amount2 = DecimalField('Amount2', places = 2, rounding = None, 
                            validators = [DataRequired(), 
                                NumberRange(min = 0, max = 10000000)])
    submit3 = SubmitField('Submit')


    def validate_name2(form, field):
        exists = Expenditures.query.filter_by(name = field.data).first()
        if exists != None:
            raise ValidationError()

# Edit Income Form
class EditIn(FlaskForm) :
    editName = StringField('editName', validators = [DataRequired(), 
                                                    Length(min = 0, max = 20)])
    newName = StringField('newName', validators = [DataRequired()])
    newAmount = DecimalField('newAmount', places = 2, rounding = None, 
                            validators = [DataRequired(), 
                                NumberRange(min = 0, max = 10000000)])
    submit2 = SubmitField('Submit') 


    def validate_newName(self, field):
        exists = Incomes.query.filter_by(name = field.data).first()
        if field.data != self.editName.data:
            if exists != None:
                raise ValidationError()

# Edit Expenditure Form
class EditEx(FlaskForm) :
    editName2 = StringField('editName2', validators = [DataRequired(), 
                                                    Length(min = 0, max = 20)])
    newName2 = StringField('newName2', validators = [DataRequired()])
    newAmount2 = DecimalField('newAmount2', places = 2, rounding = None, 
                            validators = [DataRequired(), 
                                NumberRange(min = 0, max = 10000000)])
    submit4 = SubmitField('Submit')


    def validate_newName2(self, field):
        exists = Expenditures.query.filter_by(name = field.data).first()
        if field.data != self.editName2.data:
            if exists != None:
                raise ValidationError()

# Add Goal Form
class AddGoal(FlaskForm) :
    goalName = StringField('goalName')
    goalAmount = DecimalField('goalAmount', places = 2, rounding = None, 
                                validators = [DataRequired(), 
                                    NumberRange(min = 0, max = 10000000)])


    def validate_goalAmount(form, field):
        exists = Goals.query.filter_by().first()
        if exists != None:
            raise ValidationError()

# Edit Goal Form  
class EditGoal(FlaskForm) :
    editGoal = StringField('editGoal')
    editGoalAmount = DecimalField('editGoalAmount', places = 2, rounding = None,
                                    validators = [DataRequired(), 
                                        NumberRange(min = 0, max = 10000000)])


    def validate_editGoalAmount(form, field):
        exists = Goals.query.filter_by().first()
        if exists == None:
            raise ValidationError()

        