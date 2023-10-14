from app.models import Incomes
from flask import render_template, request
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

    if inForm.validate_on_submit():
        name1 = request.form['name1']
        amount1 = request.form['amount1']
        record = Incomes(name=name1, amount=amount1)
        db.session.add(record)
        db.session.commit()
    return render_template('incomeEx.html', 
                           title='Income & Expentitures', 
                           inForm=inForm,
                           exForm=exForm,
                           incomes=incomes)
