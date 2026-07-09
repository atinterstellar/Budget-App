from flask import Flask, render_template, request,  redirect, url_for
import main_app

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


if __name__ == '__main__' :
    app.run(host = '0.0.0.0' , port = 5101 , debug = True)