from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models import Product
from run import db

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

@admin_bp.route('/admin/products')
@login_required
@admin_required
def product_list():
    products = Product.query.all()
    return render_template('admin/product_list.html', products=products)

@admin_bp.route('/admin/products/create', methods=['GET', 'POST'])
@login_required
@admin_required
def product_create():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        stock = int(request.form['stock'])
        image_url = request.form['image_url']
        product = Product(name=name, description=description, price=price, stock=stock, image_url=image_url)
        db.session.add(product)
        db.session.commit()
        flash('Producto creado correctamente.', 'success')
        return redirect(url_for('admin.product_list'))
    return render_template('admin/product_form.html', product=None)

@admin_bp.route('/admin/products/<int:product_id>/edit', methods=['GET', 'POST'])
@login_required
@admin_required
def product_edit(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.description = request.form['description']
        product.price = float(request.form['price'])
        product.stock = int(request.form['stock'])
        product.image_url = request.form['image_url']
        db.session.commit()
        flash('Producto actualizado correctamente.', 'success')
        return redirect(url_for('admin.product_list'))
    return render_template('admin/product_form.html', product=product)

@admin_bp.route('/admin/products/<int:product_id>/delete', methods=['POST'])
@login_required
@admin_required
def product_delete(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Producto eliminado correctamente.', 'success')
    return redirect(url_for('admin.product_list'))