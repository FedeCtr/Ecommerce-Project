from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)

    # Importar y registrar blueprints
    from auth.routes import auth_bp
    from admin.routes import admin_bp
    from shop.routes import shop_bp
    from api.routes import api_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(shop_bp)
    app.register_blueprint(api_bp)  # El url_prefix /api ya está en el blueprint

    # Importar modelos aquí si es necesario (por ejemplo, para migraciones)
    with app.app_context():
        from models import User, Product, Order, OrderItem
        db.create_all()

    # Flask-Login: función para cargar usuario
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    login_manager.login_view = 'auth.login'  # Redirige a login si no autenticado

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)