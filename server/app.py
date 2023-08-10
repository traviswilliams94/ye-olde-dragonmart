#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, session, make_response
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import Customer, Item, Order, OrderItem

# Views go here!

class Signup(Resource):
    def post(self):
        data = request.get_json()

        try:
            new_customer = Customer(
                name = data['name'],
                username = data['username'],
                wallet = data['wallet'],
                admin = False
            )
            new_customer.password_hash = data['password']
            db.session.add(new_customer)
            db.session.commit()
            session['customer_id'] = new_customer.id

            return make_response(new_customer.to_dict(), 201)

        except:
            return make_response({'error': 'Invalid inputs'}, 400)

class CheckSession(Resource):
    def get(self):
        customer_id =  session.get('customer_id')

        if not customer_id:
            return {'error': 'Unauthorized, please sign in'}, 401

        current_customer = Customer.query.filter(Customer.id == customer_id).first()
        return current_customer.to_dict(), 200

class Login(Resource):
    def post(self):
        data = request.get_json()

        check_customer = Customer.query.filter(Customer.username == data['username']).first()

        if check_customer and check_customer.authenticate(data['password']):
            session['customer_id'] = check_customer.id

            return make_response(check_customer.to_dict(), 200)

        return {'error': 'incorrect credentials'}, 401

class Logout(Resource):
    def delete(self):
        if session.get('customer_id'):
            session['customer_id'] = None
            return {}, 204
        return  {'error': 'Unauthorized'}, 401

class Home(Resource):
    def get(self):
        return '<h1>Phase 4 Project Server</h1>'

class Items(Resource):
    def get(self):
        items = [item.to_dict(rules=('-order_items',)) for item in Item.query.all()]
        return make_response(items, 200)

    def post(self):
        # if session.get('customer_id'):
        #     admin_check = Customer.query.filter(Customer.id == session.get('customer_id')).first()
        #     if admin_check.admin == True:
        data = request.get_json()

        new_item = Item(
            title = data['title'],
            img_url = data['img_url'],
            description = data['description'],
            category = data['category'],
            price = data['price'],
            )

        db.session.add(new_item)
        db.session.commit()

        return make_response(new_item.to_dict(), 201)
        # return {'error': 'Unauthorized Action'}, 401


class ItemsByCategory(Resource):
    def get(self, category):

        category_items = [item.to_dict() for item in Item.query.filter(Item.category == category)]
        return (category_items, 200)

class ItemsByID(Resource):
    def patch(self, id):
        # if session.get('customer_id'):
        #     admin_check = Customer.query.filter(Customer.id == session.get('customer_id')).first()
        #     if admin_check.admin == True:
        item_to_update = Item.query.filter(Item.id == id).first()
        if item_to_update:
            # data = request.get_json()
            for key in request.json:
                setattr(item_to_update, key, request.json[key])

            db.session.add(item_to_update)
            db.session.commit()

            return make_response(item_to_update.to_dict(), 202)
            
        else:
            return {'error': 'Item not found'}, 404
            # else:
            #     return {'error': 'Unauthorized action'}, 401

    def delete(self, id):
        item_to_delete = Item.query.filter(Item.id == id).first()
        if item_to_delete:
            db.session.delete(item_to_delete)
            db.session.commit()

            return make_response({},204)
        else:
            return {'error': 'Item not found'}, 404

  

class Orders(Resource):
    def post(self):
        data = request.get_json()

        new_order = Order(
            customer_id = data['customer_id'],
            total = data['total'],
        )

        db.session.add(new_order)
        db.session.commit()

        return make_response(new_order.to_dict(), 201)

class OrdersByCustomer(Resource):
    def get(self, customer_id):
        pass

class OrdersByID(Resource):
    def delete(self, id):
        order_to_delete = Order.query.filter(Order.id == id).first()

        db.session.delete(order_to_delete)
        db.session.commit()

        return make_response({}, 204)

class OrderItems(Resource):
    def post(self):
        data = request.get_json()

        new_order_item = OrderItem(
            quantity = data['quantity'],
            item_id = data['item_id'],
            order_id = data['order_id'],
        )

        db.session.add(new_order_item)
        db.session.commit()

        return make_response(new_order_item.to_dict(), 201)

class CustomersByID(Resource):
    def patch(self, id):
        if session.get('customer_id'):
            customer_to_update = Customer.query.filter(Customer.id == session.get('customer_id')).first()
            if customer_to_update:
                data = request.get_json()

                setattr(customer_to_update, 'wallet', data['wallet'])
                db.session.add(customer_to_update)
                db.session.commit()

                return make_response(customer_to_update.to_dict(), 202)
     

api.add_resource(Home, '/')
api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(Items, '/items')
api.add_resource(ItemsByCategory, '/items/<category>')
api.add_resource(ItemsByID, '/items/<int:id>')
api.add_resource(Orders, '/orders')
api.add_resource(OrdersByID, '/orders/<int:id>')
api.add_resource(OrderItems, '/orderitems')
api.add_resource(CustomersByID,'/customers/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)

