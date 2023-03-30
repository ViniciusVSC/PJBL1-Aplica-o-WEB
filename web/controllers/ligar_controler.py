from flask import Blueprint

ligar_bp = Blueprint('ligar', __name__, url_prefix='/ligar')

@ligar_bp.route('/ligar')
def ligar():
    return render_template('templates/ligar.html')
