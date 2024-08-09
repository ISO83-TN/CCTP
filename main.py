from flask import Flask
from project.routes import main as main_blueprint

def create_app():
    app = Flask(__name__)

    # Enregistrer le blueprint
    app.register_blueprint(main_blueprint)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
