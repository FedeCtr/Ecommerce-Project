from flask import Blueprint

shop_bp = Blueprint('shop', __name__, template_folder='../templates/shop')

# Aquí irán las rutas de la tienda para clientes