from flask import Blueprint

usuario_bp = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_bp.route('/usuario')
def usuario():
    return render_template('templates/usuario.html')
