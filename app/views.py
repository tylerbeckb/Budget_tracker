from flask import render_template
from app import app
from .forms import IncomeForm, ExpenditureForm

@app.route('/')
def index():
    return render_template("index.html", title='Home')

@app.route('/incomeExpenditure', methods=['GET', 'POST'])
def incomeEx():
    inForm = IncomeForm()
    exForm = ExpenditureForm()
    return render_template('incomeEx.html', 
                           title='Income & Expentitures', 
                           inForm=inForm,
                           exForm=exForm)
