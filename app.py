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

@app.route('/cat-ledger')
def cat_ledger():
    name = request.args.get("name")
    chosen = main_app.get_category(name)
    return render_template('ledger_cat.html', chosen = chosen)

if __name__ == '__main__' :
    app.run(host = '0.0.0.0' , port = 5101 , debug = True)