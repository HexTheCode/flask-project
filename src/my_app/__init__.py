from flask import Flask, url_for, redirect, flash
import os

app = Flask(__name__, instance_relative_config=True)
app.config['SECRET_KEY'] = os.urandom(6) or 'you-will-never-guess'



from .views import hello, login, sum

app.register_blueprint(hello.hello_bp)
app.register_blueprint(login.login_bp)
app.register_blueprint(sum.sum_bp)

@app.route('/')
def index():
    return redirect(url_for('hello.hello_world'))

