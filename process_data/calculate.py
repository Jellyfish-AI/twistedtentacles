def calculate_total_price(items):
        total_price = 0
        for item in items:
            total_price += item.item_price

        return total_price