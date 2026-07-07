from flask import Flask, render_template
import main_app

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home_page.html')

@app.route('/ledger')
def ledger():
    return render_template('ledger.html', categories = main_app.categories)

@app.route('/cat-ledger')
def cat_ledge():
    return render_template('ledger_cat.html')


if __name__ == '__main__' :
    app.run(host = '0.0.0.0' , port = 5101 , debug = True)