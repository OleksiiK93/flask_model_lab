from flask import Blueprint, render_template
from models.order_list import orders

orders_blueprint = Blueprint('orders', __name__)

@orders_blueprint.route('/orders')
def index():
    enumerated_orders = list(enumerate(orders))
    return render_template('index.html', enumerated_orders=enumerated_orders)

@orders_blueprint.route('/orders/<index>')
def one_order(index):
    return render_template('order.html', order = orders[int(index)], index = index)