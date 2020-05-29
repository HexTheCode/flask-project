from flask import session, Blueprint, render_template

hello_bp = Blueprint('hello', __name__, url_prefix='/hello')

@hello_bp.route('/')
def hello_world():
    if 'user' in session:
        return render_template('home.html', name=session['user'])
    return render_template('home.html')

@hello_bp.route('/hi')
def hello():
    if 'user' in session:
        return render_template('hello.html', name=session['user'])
    return render_template('hello.html')