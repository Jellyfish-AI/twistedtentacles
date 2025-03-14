from process_data.process_orders import get_orders_for_company
from utils import company_specific_function


@company_specific_function('ai_innovation')
def apply_ai_innovation_discount(orders):
    """
    AI Innovation get a 25% discount on all items
    """
    ai_innovation_orders = get_orders_for_company(orders, 'ai_innovation')
    for order in ai_innovation_orders:
        for item in order.items:
            item.discount = 0.25
            item.item_price *= (1 - item.discount)
            order.total_price = sum([item.item_price for item in order.items])
    return orders

@company_specific_function('ai_innovation')
def apply_usd_to_eur_conversion(orders):
    """
    AI Innovation is a european company so all prices should be converted to Euros
    """
    ai_innovation_orders = get_orders_for_company(orders, 'ai_innovation')
    for order in ai_innovation_orders:
        for item in order.items:
            item.item_price *= 0.85
        order.total_price = sum([item.item_price for item in order.items])
    return orders