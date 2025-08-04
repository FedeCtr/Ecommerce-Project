from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_required, current_user
from models import Product

shop_bp = Blueprint('shop', __name__, template_folder='../templates/shop')

# ... (product_list, product_detail, add_to_cart ya implementados antes)

@shop_bp.route('/shop/cart')
@login_required
def cart():
    cart = session.get('cart', {})
    items = []
    total = 0
    for product_id, quantity in cart.items():
        product = Product.query.get(int(product_id))
        if product:
            subtotal = product.price * quantity
            items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal
            })
            total += subtotal
    return render_template('shop/cart.html', items=items, total=total)

@shop_bp.route('/shop/cart/update/<int:product_id>', methods=['POST'])
@login_required
def update_cart(product_id):
    quantity = int(request.form.get('quantity', 1))
    cart = session.get('cart', {})
    if quantity > 0:
        cart[str(product_id)] = quantity
    else:
        cart.pop(str(product_id), None)
    session['cart'] = cart
    flash('Carrito actualizado.', 'success')
    return redirect(url_for('shop.cart'))

@shop_bp.route('/shop/cart/remove/<int:product_id>', methods=['POST'])
@login_required
def remove_from_cart(product_id):
    cart = session.get('cart', {})
    cart.pop(str(product_id), None)
    session['cart'] = cart
    flash('Producto eliminado del carrito.', 'success')
    return redirect(url_for('shop.cart'))