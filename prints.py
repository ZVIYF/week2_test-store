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



    def print_order(order):
        print(f"order id: {order["id"]}\n", "")