from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from models import User, Product, Order, OrderItem
from run import db
from sqlalchemy import func, desc
import datetime

admin_bp = Blueprint('admin', __name__, template_folder='../templates/admin')

def admin_required(func):
    from functools import wraps
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin():
            flash('Acceso solo para administradores.', 'danger')
            return redirect(url_for('auth.login'))
        return func(*args, **kwargs)
    return decorated_view

@admin_bp.route('/admin/dashboard')
@login_required
@admin_required
def dashboard():
    # Ventas totales
    total_sales = db.session.query(func.sum(Order.total)).scalar() or 0

    # Ventas del mes
    first_day = datetime.date.today().replace(day=1)
    monthly_sales = db.session.query(func.sum(Order.total)).filter(Order.created_at >= first_day).scalar() or 0

    # Órdenes recientes
    recent_orders = Order.query.order_by(Order.created_at.desc()).limit(5).all()

    # Productos más vendidos
    top_products = db.session.query(
        Product.name,
        func.sum(OrderItem.quantity).label('total_qty')
    ).join(OrderItem).group_by(Product.id).order_by(desc('total_qty')).limit(5).all()

    # Usuarios registrados
    user_count = User.query.count()

    return render_template('admin/dashboard.html',
        total_sales=total_sales,
        monthly_sales=monthly_sales,
        recent_orders=recent_orders,
        top_products=top_products,
        user_count=user_count
    )