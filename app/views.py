from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template("index.html", title='Home')

@app.route('/incomeExpeniture')
def incomeEx():
    return render_template('incomeEx.html', title='Income & Expentitures')
