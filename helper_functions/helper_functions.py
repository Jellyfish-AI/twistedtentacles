def get_company_by_slug(slug):
    from stored_data.data import companies

    for company in companies.values():
        if company.slug == slug:
            return company
    return None

def get_orders_for_company(orders, company_slug):
    company_orders = []
    for order in orders:
        if order.company.slug == company_slug:
            company_orders.append(order)
    return company_orders


def get_order_items_for_company(orders, company_slug):
    order_items = []
    for order in orders:
        if order.company.slug == company_slug:
            order_items.extend(order.items)
    return order_items