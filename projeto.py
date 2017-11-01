from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/tables')
def tables():
    return render_template('tables.html')

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/recuperar')
def recuperar():
    return render_template('recuperar.html')

if __name__ == '__main__':
    app.run()

