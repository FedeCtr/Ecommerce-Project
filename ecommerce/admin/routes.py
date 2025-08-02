from flask import Blueprint

admin_bp = Blueprint('admin', __name__, template_folder='../templates/admin')

# Aquí irán las rutas del panel de administración