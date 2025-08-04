from flask import Blueprint, jsonify, request, abort
from flask_login import login_required, current_user
from models import Product, Order, OrderItem, User
from run import db

api_bp = Blueprint('api', __name__, url_prefix='/api')

# --- Productos ---

@api_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'description': p.description,
        'price': p.price,
        'stock': p.stock,
        'image_url': p.image_url
    } for p in products])

@api_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    p = Product.query.get_or_404(product_id)
    return jsonify({
        'id': p.id,
        'name': p.name,
        'description': p.description,
        'price': p.price,
        'stock': p.stock,
        'image_url': p.image_url
    })

@api_bp.route('/products', methods=['POST'])
@login_required
def create_product():
    if not current_user.is_admin():
        abort(403)
    data = request.json
    p = Product(
        name=data['name'],
        description=data.get('description', ''),
        price=float(data['price']),
        stock=int(data.get('stock', 0)),
        image_url=data.get('image_url', '')
    )
    db.session.add(p)
    db.session.commit()
    return jsonify({'message': 'Producto creado', 'id': p.id}), 201

@api_bp.route('/products/<int:product_id>', methods=['PUT'])
@login_required
def update_product(product_id):
    if not current_user.is_admin():
        abort(403)
    p = Product.query.get_or_404(product_id)
    data = request.json
    p.name = data.get('name', p.name)
    p.description = data.get('description', p.description)
    p.price = float(data.get('price', p.price))
    p.stock = int(data.get('stock', p.stock))
    p.image_url = data.get('image_url', p.image_url)
    db.session.commit()
    return jsonify({'message': 'Producto actualizado'})

@api_bp.route('/products/<int:product_id>', methods=['DELETE'])
@login_required
def delete_product(product_id):
    if not current_user.is_admin():
        abort(403)
    p = Product.query.get_or_404(product_id)
    db.session.delete(p)
    db.session.commit()
    return jsonify({'message': 'Producto eliminado'})

# --- Órdenes ---

@api_bp.route('/orders', methods=['GET'])
@login_required
def get_orders():
    # Admin ve todas, cliente solo las suyas
    if current_user.is_admin():
        orders = Order.query.order_by(Order.created_at.desc()).all()
    else:
        orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.created_at.desc()).all()
    return jsonify([{
        'id': o.id,
        'user_id': o.user_id,
        'total': o.total,
        'created_at': o.created_at,
        'items': [{
            'product_id': oi.product_id,
            'quantity': oi.quantity,
            'price': oi.price
        } for oi in o.items]
    } for o in orders])

@api_bp.route('/orders', methods=['POST'])
@login_required
def create_order():
    data = request.json
    items = data.get('items', [])
    total = 0
    order = Order(user_id=current_user.id, total=0)
    db.session.add(order)
    db.session.flush()
    for i in items:
        product = Product.query.get(i['product_id'])
        if not product or product.stock < i['quantity']:
            abort(400, 'Producto no disponible')
        subtotal = product.price * i['quantity']
        total += subtotal
        order_item = OrderItem(
            order_id=order.id,
            product_id=product.id,
            quantity=i['quantity'],
            price=product.price
        )
        product.stock -= i['quantity']
        db.session.add(order_item)
    order.total = total
    db.session.commit()
    return jsonify({'message': 'Orden creada', 'id': order.id}), 201

# --- Usuarios (solo admin) ---

@api_bp.route('/users', methods=['GET'])
@login_required
def get_users():
    if not current_user.is_admin():
        abort(403)
    users = User.query.all()
    return jsonify([{
        'id': u.id,
        'username': u.username,
        'email': u.email,
        'role': u.role
    } for u in users])