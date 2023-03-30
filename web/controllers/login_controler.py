from flask import Blueprint

login_bp = Blueprint('login', __name__, url_prefix='/login')
cadastro_bp = Blueprint('cadastro', __name__, url_prefix='/cadastro')

@login_bp.route('/login')
def login():
    return render_template('templates/login.html')


@cadastro_bp.route('/cadastro')
def cadastro():
    return render_template('templates/cadastro.html')
