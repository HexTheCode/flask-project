from flask import Blueprint

sum_bp = Blueprint('sum', __name__, url_prefix='/sum')

@sum_bp.route('/<int:num1>/<int:num2>')
def sum(num1, num2):
    return str(num1 + num2)