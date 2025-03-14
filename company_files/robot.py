# Migrated to robot_cloud as of 2/1/2025. All data past this date is under the slug robot_cloud. Pls migrate any functions to robot_cloud.py.
    
from process_data.process_orders import get_orders_for_company
from utils import company_specific_function


@company_specific_function('robot')
def apply_robot_discount(orders):
    """
    Robot Inc. gets half off all orders
    """
    robot_orders = get_orders_for_company(orders, 'robot')
    order_discount = 0.5
    for order in robot_orders:
        order.total_price *= 1 - order_discount

    return orders