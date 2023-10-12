from flask import render_template
from app import app
from .forms import IncomeForm

@app.route('/')
def index():
    return render_template("index.html", title='Home')

@app.route('/incomeExpeniture', methods=['GET', 'POST'])
def incomeEx():
    form = IncomeForm()
    return render_template('incomeEx.html', 
                           title='Income & Expentitures', 
                           form=form)
