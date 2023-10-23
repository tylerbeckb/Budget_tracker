from app.models import Incomes, Expenditures, Goals
from flask import render_template, request, redirect, url_for
from app import app, db
from .forms import IncomeForm, ExpenditureForm, EditIn, EditEx, addGoal, editGoal


@app.route('/')
def index():
    #Databases and variables
    incomes = Incomes.query.all() 
    expenditures = Expenditures.query.all()
    goal = Goals.query.first()
    inTotal = 0
    exTotal = 0
    total = 0
    needZero = False
    needZeroEx = False
    needZeroTot = False

    # Adds both the totals
    for income in incomes:
        inTotal += income.amount
    for expenditure in expenditures:
        exTotal += expenditure.amount

    # Calculates overall total
    total = round(inTotal - exTotal,2)

    # Checks if the total needs an extra 0
    strinTotal = str(inTotal)
    if strinTotal.find('.') != len(strinTotal) - 2:
        needZero = False
    else:
        needZero = True

    strexTotal = str(exTotal)
    if strexTotal.find('.') != len(strexTotal) - 2:
        needZeroEx = False
    else:
        needZeroEx = True
    
    strTotal = str(total)
    if strTotal.find('.') != len(strTotal) - 2:
        needZeroTot = False
    else:
        needZeroTot = True


    if total < 0:
        barWidth = 0
    else:
        barWidth = round((total / goal.amount) * 100, 2)

    if barWidth > 100:
        barWidth = 100


    return render_template("index.html", title='Home',
                           inTotal=inTotal,
                           exTotal=exTotal,
                           needZero=needZero,
                           needZeroEx=needZeroEx,
                           total=total,
                           needZeroTot=needZeroTot,
                           barWidth=barWidth)

@app.route('/deleteData<name>/<type>', methods=["POST"])
def deleteData(name, type):
    if type == "ex":
        Expenditures.query.filter_by(name=name).delete()
    elif type == "in":
        Incomes.query.filter_by(name=name).delete()
    else:
        Goals.query.filter_by().delete()
        db.session.commit()
        return redirect('/goals')
    db.session.commit()
    return redirect('/incomeExpenditure')

@app.route('/incomeExpenditure', methods=['GET', 'POST'])
def incomeEx():
    # Forms
    inForm = IncomeForm()
    exForm = ExpenditureForm()
    editIn = EditIn()
    editEx = EditEx()

    # Error variables
    missing = not None
    missingEx = not None

    # Databases
    incomes = Incomes.query.all() 
    expenditures = Expenditures.query.all()
    inData = False
    exData = False

    existInFormError = True
    existExFormError = True

    if incomes:
        inData = True

    if expenditures:
        exData = True

    # Writes income data to Incomes db
    if inForm.validate_on_submit() and inForm.submit.data:
        existExFormError = False
        name1 = request.form['name1']
        amount1 = request.form['amount1']
        amount1 = round(float(amount1), 2)
        record = Incomes(name=name1, amount=amount1)
        db.session.add(record)
        db.session.commit()
        return redirect(url_for('incomeEx'))

    # Writes expenditure data to Expenditures db
    if exForm.validate_on_submit() and exForm.submit3.data:
        existInFormError = False
        name2 = request.form['name2']
        amount2 = request.form['amount2']
        amount2 = round(float(amount2), 2)
        record = Expenditures(name=name2, amount=amount2)
        db.session.add(record)
        db.session.commit()
        return redirect(url_for('incomeEx'))
    
    # Edits income db
    if editIn.validate_on_submit() and editIn.submit2.data:
        existInFormError = False
        existExFormError = False
        editName = request.form['editName']
        # Validates if name exists
        missing = Incomes.query.filter_by(name=editName).first()
        if missing != None:
            missing.name = request.form['newName']
            newAmount = request.form['newAmount']
            newAmount = round(float(newAmount), 2)
            missing.amount = newAmount
            db.session.commit()

    # Edits expenditure db
    if editEx.validate_on_submit() and editEx.submit4.data:
        existExFormError = False
        existInFormError = False
        editName2 = request.form['editName2']
        # Validates if name exists
        missingEx = Expenditures.query.filter_by(name=editName2).first()
        if missingEx != None:
            missingEx.name = request.form['newName2']
            newAmount2 = request.form['newAmount2']
            newAmount2 = round(float(newAmount2), 2)
            missingEx.amount = newAmount2
            db.session.commit()
    # Renders Page
    return render_template('incomeEx.html', 
                           title='Income & Expentitures', 
                           inForm=inForm,
                           exForm=exForm,
                           editIn=editIn,
                           editEx=editEx,
                           incomes=incomes,
                           expenditures=expenditures,
                           missing = missing,
                           missingEx = missingEx,
                           inData = inData,
                           exData = exData,
                           existInFormError=existInFormError,
                           existExFormError=existExFormError)

@app.route('/goals', methods=['GET', 'POST'])
def goals():

    needZero = False

    goalForm = addGoal()
    editGoalForm = editGoal()
    goals = Goals.query.all()
    goalRecord = Goals.query.filter_by().first()
    if goalForm.validate_on_submit():
        goalName = request.form['goalName']
        goalAmount = request.form['goalAmount']
        goalAmount = round(float(goalAmount),2)
        record = Goals(name=goalName, amount=goalAmount)
        db.session.add(record)
        db.session.commit()
        return redirect(url_for('goals'))
    
    if editGoalForm.validate_on_submit():
        goalRecord = Goals.query.filter_by().first()
        goalRecord.name = request.form['editGoal']
        goalRecord.amount = request.form['editGoalAmount']
        goalRecord.amount = round(float(goalRecord.amount),2)
        db.session.commit()
        return redirect(url_for('goals'))
    
    # Checks if the display needs to add a zero on the end
    if goalRecord != None:
        addError = True
        editError = False
        strGoalAmount = str(goalRecord.amount)
        if strGoalAmount.find('.') != len(strGoalAmount) - 2:
            needZero = False
        else:
            needZero = True
    else:
        editError = True
        addError = False

    return render_template('goals.html', 
                           title='Goals',
                           goalForm=goalForm,
                           goals=goals,
                           editGoalForm=editGoalForm,
                           needZero = needZero,
                           editError=editError,
                           addError=addError)