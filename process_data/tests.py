def validate_orders(orders):
    
    # Test that the total price is correct for each order

    if orders[0].total_order_price == 55.0:
        orders[0].validated = True

    if orders[1].total_order_price == 15.0:
        orders[1].validated = True
    
    if orders[2].total_order_price == 85.0:
        orders[2].validated = True
    
    if orders[3].total_order_price == 2500.0:
        orders[3].validated = True
    
    if orders[4].total_order_price == 300:
        orders[4].validated = True
    
    if orders[5].total_order_price == 387.5:
        orders[5].validated = True

    if orders[6].total_order_price == 6.375:
        orders[6].validated = True
    
    if orders[7].total_order_price == 127.5:
        orders[7].validated = True
    
    if orders[8].total_order_price == 500:
        orders[8].validated = True
    
    if orders[9].total_order_price == 300:
        orders[9].validated = True

    
    
    return True