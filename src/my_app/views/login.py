from flask import Blueprint, redirect, request, session, url_for

login_bp = Blueprint('login', __name__, url_prefix='/login')

@login_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
                    <form method="post">
                        <input type="text" name="user">
                        <input type="submit" value="login">
                    </form>
               '''
    if request.method == 'POST':
        session['user'] = request.form['user']
        return redirect(url_for('hello.hello_world'))