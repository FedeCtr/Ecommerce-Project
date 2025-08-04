from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_required, current_user
from models import Product, Order, OrderItem
from run import db

shop_bp = Blueprint('shop', __name__, template_folder='../templates/shop')

# ... (otras rutas previas)

@shop_bp.route('/shop/cart/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
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

    if request.method == 'POST':
        # Crear orden y sus items
        order = Order(user_id=current_user.id, total=total)
        db.session.add(order)
        db.session.flush()  # Para obtener el order.id antes de commit
        for item in items:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item['product'].id,
                quantity=item['quantity'],
                price=item['product'].price
            )
            db.session.add(order_item)
            # Opcional: reducir stock
            item['product'].stock -= item['quantity']
        db.session.commit()
        session['cart'] = {}  # Vaciar carrito
        flash('¡Compra realizada con éxito!', 'success')
        return redirect(url_for('shop.order_detail', order_id=order.id))

    return render_template('shop/checkout.html', items=items, total=total)

@shop_bp.route('/shop/order/<int:order_id>')
@login_required
def order_detail(order_id):
    order = Order.query.get_or_404(order_id)
    return render_template('shop/order_detail.html', order=order)