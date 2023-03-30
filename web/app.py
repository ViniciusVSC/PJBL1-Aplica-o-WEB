from flask import Flask, render_template
from controllers.ligar_controler import ligar_bp
from controllers.login_controler import login_bp
from controllers.usuario_controler import usuario_bp

app = Flask(__name__)

app.register_blueprint(ligar_bp)
app.register_blueprint(login_bp)
app.register_blueprint(usuario_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()