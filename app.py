from flask import Flask, render_template, request,  redirect, url_for
import main_app
from main_app import Master , cash


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home_page.html')

chosen = None

@app.route('/ledger' , methods = ['GET' , 'POST'])
def ledger():
    if request.method == 'POST':
        chosen = request.form.get("category")
        return redirect(url_for('cat_ledger', name=chosen))
    return render_template('ledger.html', categories = main_app.categories)

@app.route('/cat_ledger')
def cat_ledger():
    name = request.args.get("name")
    chosen = main_app.get_category(name)
    return render_template('ledger_cat.html', chosen = chosen)

@app.route('/deposit', methods = ['GET','POST'])
def deposit():
    if request.method == 'POST':
        chosen = request.form.get("category") 
        return redirect(url_for('deposit_cat', name = chosen))
    return render_template('deposit_to.html', categories = main_app.categories)

@app.route('/deposit_cat', methods = ['GET','POST'])
def deposit_cat():
    name = request.args.get("name")
    chosen = main_app.get_category(name)
    if request.method == 'POST':
        amount = request.form.get("amount")
        desc = request.form.get("desc")
        chosen.deposit(float(amount), desc)
        return redirect(url_for('cat_ledger', name=name))
    return render_template('cat_deposit.html' , chosen = chosen)

@app.route('/transaction_from', methods = ['GET','POST'])
def transaction_from():
    if request.method == 'POST':
        chosen = request.form.get("category") 
        return redirect(url_for('withdraw_cat', name = chosen))
    return render_template('transaction_from.html', categories = main_app.categories)

@app.route('/withdraw_cat', methods = ['GET','POST'])
def withdraw_cat():
    name = request.args.get("name")
    chosen = main_app.get_category(name)
    if request.method == 'POST':
        amount = request.form.get("amount")
        desc = request.form.get("desc")
        chosen.withdraw(float(amount), desc)
        return redirect(url_for('cat_ledger', name=name))
    return render_template('withdraw_cat.html' , chosen = chosen)

@app.route('/bal', methods = ['GET','POST'])
def bal():
    return render_template('bal.html', categories = main_app.categories)

@app.route('/master_balance')
def master_balance():
    balance = Master.total_balance()
    return render_template('master_balance.html' , balance = balance)

@app.route('/guide')
def guide():
    return render_template('guide.html')

@app.route('/cash_balance')
def cash_balance() :
    balance = cash.balance
    return render_template('cash_balance.html' , bal = balance)

@app.route('/cash_deposit', methods = ['GET','POST'])
def cash_deposit() :
    if request.method == 'POST' :
        amount = request.form.get('amount')
        desc = request.form.get('desc')
        cash.deposit(float(amount),desc)
        return redirect(url_for('cash_ledger'))
    return render_template('cash_deposit.html')

@app.route('/cash_trans', methods = ['GET','POST'])
def cash_trans():
    if request.method == 'POST' :
        amount = request.form.get('amount')
        desc = request.form.get('desc')
        cash.withdraw(float(amount),desc)
        return redirect(url_for('cash_ledger'))
    return render_template('cash_trans.html')

@app.route('/cash_ledger')
def cash_ledger():
    ledger = cash.ledger
    return render_template('cash_ledger.html' , ledger = ledger)

if __name__ == '__main__' :
    app.run(host = '0.0.0.0' , port = 5101 , debug = True)