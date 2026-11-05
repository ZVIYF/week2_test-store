import Products, calcs, storage, orders


def print_main_menu():
    print(
    """
    ========== ORDER MANAGER ==========
    1. Create order
    2. Show all orders
    3. Find order by ID
    4. Close order
    5. Show sales report
    0. Exit
 
    """
    )


def print_items(items):
    for item in items:
        print(f"item id: {item["product_id"]}")
        print(f"item name: {Products.products[item["product_id"]]["name"]}")
        print(f"quantity: {item["quantity"]}")
        print()
    

def print_order(order):
    print(f"order id: {order["id"]}\n", "items: ")
    print_items(order["items"])
    print(f"subtotal: {calcs.get_order_subtotal(order["items"])}")
    print(f"discount percent: {(calcs.calculate_discount(calcs.get_order_subtotal(order["items"])) * 100)} percent")
    print(f"total: {calcs.get_order_total(order)}")


def print_orders():
    order_list = storage.load_orders()
    for order in order_list:
        print_order(order)
        print()
        
    if not order_list:
        print("no order yet")


def print_most_expensive():
    try:
        closed_orders = orders.get_closed_orders()
        if not closed_orders:
            raise ValueError("No closed orders yet")
        high_to_low = orders.sort_orders(closed_orders)
        print(f"most expensive order: {high_to_low[0]["id"]}")
    except ValueError as error:
        print(f"error: {error}")

def print_3_expensive():
    try:
        closed_orders = orders.get_closed_orders()
        if not closed_orders:
            raise ValueError("No closed orders yet")
        high_to_low = orders.sort_orders(closed_orders)
        print("most expensive order:")
        print(
            high_to_low[0]["id"],
            high_to_low[1]["id"],
            high_to_low[2]["id"]
            )
    except ValueError as error:
        print(f"error: {error}")
    except IndexError:
        print("there are less then 3 orders")

def print_report():
    print(f"total orders: {len(storage.load_orders())}")
    print(f"closed orders total: {orders.sum_of_order(orders.get_closed_orders())}")
    print_most_expensive()
    print_3_expensive()
