from run import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    in_stock = db.Column(db.Boolean, default=True)