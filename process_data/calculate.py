def calculate_total_order_price(items_list):
        total_order_price = 0
        for items in items_list:
            total_order_price += items.total_item_price

        return total_order_price