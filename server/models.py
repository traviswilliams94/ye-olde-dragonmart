from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db

# Models go here!

class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    # serialize_rules = 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    # username = db.Column(db.String, unique=True, nullable=False)
    # _password_hash = db.Column(db.String)
    # created_at = db.Column(db.DateTime, server_default=db.func.now())
    # updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    orders = db.relationship('Order', backref='customer')
    order_items = association_proxy('orders', 'order_items')

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError('Customer must have a name')
        return name

class Item(db.Model, SerializerMixin):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    img_url = db.Column(db.String)
    description = db.Column(db.String)
    category = db.Column(db.String, nullable=False)
    price = db.column(db.Integer, nullable=False)

    orders = db.relationship('OrderItem', backref='item')

    #serilize_rules = 

    @validates('category')
    def validate_category(self, key, category):
        if not category:
            raise ValueError('Category cannot be empty. Must be Weapons, Armor, Tools, or Magic Items.')
        return category

    @validates('price')
    def validate_price(self, key, price):
        if not price and 1 <= price:
            raise ValueError('Must have a price of 1 or more')
        return price

class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.integer, ForeignKey('customers.id'))
    total = db.Column(db.Float)

    order_items = db.relationship('OrderItem', backref='order')
    items = association_proxy('order_items', 'item')


class OrderItem(db.Model, SerializerMixin):
    __tablename__ = 'orderitems'

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    order_id = db.Column(db.Integer, ForeignKey('orders.id'))
    item_id = db.Column(db.Integer, ForeignKey('items.id'))

    @validates('quantity')
    def validate_quantity(self, key, quantity)

    if quantity > 0:
        return quantity
    else:
        raise ValueError('Quantity must be greater than 0')

    # serialize_rules = 


