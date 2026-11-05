products = [
    {"id": 1, "name": "Keyboard", "price": 120},
    {"id": 2, "name": "Mouse", "price": 80},
    {"id": 3, "name": "Monitor", "price": 900},
    {"id": 4, "name": "Headphones", "price": 200},
    {"id": 5, "name": "USB Cable", "price": 30}
]


def get_product_price(product_id):
    for p in products:
        if p["id"] == product_id:
            return p["price"]

def is_in_products(product_id: int) ->bool:
    for p in products:
        if p["id"] == product_id:
            return True
    return False