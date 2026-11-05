import Products

def get_order_total(order_items:list)->int|float:
    subtotal = 0
    for item in order_items:
        price = Products.get_product_price(item["product_id"])
        item_subtotal = item["quantity"] * price
        subtotal += item_subtotal
    discount = calculate_discount(subtotal)
    return subtotal - discount 

def calculate_discount(subtotal):
    if subtotal < 300:
        return 0
    elif subtotal < 700:
        return subtotal * 0.05
    elif subtotal < 1500:
        return subtotal * 0.1
    return subtotal * 0.15


if __name__ == "__main__":
    print(get_order_total([{"product_id":1, "quantity":2}, {"product_id":3, "quantity":1}]))