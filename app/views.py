from app.models import Incomes, Expenditures
from flask import render_template, request, redirect, url_for
from app import app, db
from .forms import IncomeForm, ExpenditureForm, EditIn, EditEx


@app.route('/')
def index():
    return render_template("index.html", title='Home')

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

    # Writes income data to Incomes db
    if inForm.validate_on_submit():
        name1 = request.form['name1']
        amount1 = request.form['amount1']
        record = Incomes(name=name1, amount=amount1)
        db.session.add(record)
        db.session.commit()
        return redirect(url_for('incomeEx'))
    
    # Writes expenditure data to Expenditures db
    if exForm.validate_on_submit():
        name2 = request.form['name2']
        amount2 = request.form['amount2']
        record = Expenditures(name=name2, amount=amount2)
        db.session.add(record)
        db.session.commit()
        return redirect(url_for('incomeEx'))
    
    # Edits income db
    if editIn.validate_on_submit():
        editName = request.form['editName']
        # Validates if name exists
        missing = Incomes.query.filter_by(name=editName).first()
        if missing != None:
            missing.name = request.form['newName']
            missing.amount = request.form['newAmount']
            db.session.commit()

    # Edits expenditure db
    if editEx.validate_on_submit():
        editName2 = request.form['editName2']
        # Validates if name exists
        missingEx = Expenditures.query.filter_by(name=editName2).first()
        if missingEx != None:
            missingEx.name = request.form['newName2']
            missingEx.amount = request.form['newAmount2']
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
                           missingEx = missingEx)
