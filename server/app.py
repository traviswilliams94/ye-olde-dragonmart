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

@app.route('/')
def index():
    return '<h1>Phase 4 Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

