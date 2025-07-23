from flask import Flask
from app.database.db import db

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos (ajusta los valores a tu entorno)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mysecretpassword@localhost:5432/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Importar y registrar blueprints
    from app.controllers.hola_controller import hola_bp
    from app.controllers.segundo_controller import segundo_bp
    from app.controllers.ejemplo_bd_controller import ejemplo_bp
    app.register_blueprint(hola_bp)
    app.register_blueprint(segundo_bp)
    app.register_blueprint(ejemplo_bp)

    return app 