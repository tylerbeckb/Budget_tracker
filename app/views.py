from app.models import Incomes, Expenditures
from flask import render_template, request, redirect, url_for
from app import app, db
from .forms import IncomeForm, ExpenditureForm


@app.route('/')
def index():
    return render_template("index.html", title='Home')

@app.route('/incomeExpenditure', methods=['GET', 'POST'])
def incomeEx():
    inForm = IncomeForm()
    exForm = ExpenditureForm()

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
    # Renders Page
    return render_template('incomeEx.html', 
                           title='Income & Expentitures', 
                           inForm=inForm,
                           exForm=exForm,
                           incomes=incomes,
                           expenditures=expenditures)
