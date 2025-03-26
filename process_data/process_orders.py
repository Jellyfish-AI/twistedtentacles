import json
from datetime import datetime

from helper_functions.helper_functions import get_orders_for_company
from models.models import Order, OrderItems
from process_data.calculate import calculate_total_order_price
from stored_data.data import products

def process_order_form(companies):

    # Loads in the stored_orders from the stored_data folder
    with open('stored_data/stored_orders.json') as raw_json:
        data = json.load(raw_json)

    orders = []
    # Iterates through the stored_orders and creates Order objects
    for order_data in data:
        order_id = order_data['id']
        company = companies[order_data['company_id']]
        items = []
        # Iterates through the items in the order and creates OrderItem objects
        for item_data in order_data['items']:
            product = products[item_data['product_id']]
            quantity = item_data['quantity']
            total_item_price = product.price * quantity
            items.append(OrderItems(product=product, quantity=quantity, total_item_price=total_item_price))
       
        order_date = datetime.strptime(order_data['order_date'], '%Y-%m-%dT%H:%M:%S')
        total_order_price = calculate_total_order_price(items)
        
        orders.append(Order(order_id, company, items, total_order_price, order_date))
    
    return orders


def print_order_receipts_by_company(companies, orders):

    '''
    Print out each companies receipt information
    ''' 

    all_companies = companies.values()    
    for company in all_companies:
        
        company_orders = get_orders_for_company(orders, company.slug)

        for order in company_orders:
            receipt_info = {
                'company': company.name,
                'order_id': order.id,
                'item_inventory': order.items,
                'amount_due': order.total_order_price,
                'address': company.address,
                'validated': order.validated,
                'order_date': order.order_date,
            }

            print(f"Company: {receipt_info['company']}")
            print(f"Order #: {receipt_info['order_id']}")
            print(f"Date: {receipt_info['order_date']}")
            print(f"Items: {receipt_info['item_inventory']}")
            print(f"Amount Due: {receipt_info['amount_due']}")
            print(f"Address: {receipt_info['address']}")
            print(f"Cost Validated: {receipt_info['validated']}")
            print("\n")