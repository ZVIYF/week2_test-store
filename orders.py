import inputs_validation as Inputs
import Products
import order_validations as ov
import storage
import calcs


"""
order = {
    "id": 1,
    "items": [{"product_id": 1, "quantity": 2},
              {"product_id": 3, "quantity": 1}],
    "total": 1026.0,
    "status": "OPEN"
}
"""

def generate_order_id() -> int:
    return len(storage.load_orders()) + 1


def add_item():
    while True:
        try:
            product_id = Inputs.get_input("Enter product ID:")
            Inputs.input_validation(product_id, "product ID", "positive")
            product_id = int(product_id)
            if not Products.is_in_products(product_id):
                raise ValueError("Product ID is invalid")
            
            quantity = Inputs.get_input("Enter quantity:")
            Inputs.input_validation(quantity, "quantity", "positive")
            quantity = int(quantity)

            return {"product_id": product_id, "quantity": quantity}
        
        except ValueError as error:
            print(f"error: {error}")
        


def add_items_to_order():
    enough = False
    order_items = []
    while not enough:
        new_item = add_item()
        order_items.append(new_item)
        enough = ov.is_enough()
    if not order_items:
        raise ValueError("Cant create order without any products")
    return order_items




def create_order_object():
    order_id = generate_order_id()
    while True:
        try:
            order_items = add_items_to_order()
            break
        except ValueError as error:
            print(f"error: {error}")
    order = {
    "id": order_id,
    "items": order_items,
    "total": calcs.get_order_total(order_items),
    "status": "OPEN"
}    
    return order

def add_new_order():
    new_order = create_order_object() 
    orders = storage.load_orders()    
    orders.append(new_order)
    storage.write_orders(orders)


