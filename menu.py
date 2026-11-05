import inputs_validation as Inputs
import orders, prints, storage

def get_menu_choice():
    while True:
        try:        
            choice = Inputs.get_input("Choose option:")
            Inputs.input_validation(choice, "choice", "int")
            return int(choice)
        except ValueError as error:
            print(f"error: {error}")


def find_order_by_id():
    while True:
        try:
            order_id = Inputs.get_input("Enter order ID:")
            Inputs.input_validation(order_id, "Order ID", "positive")
            order_id = int(order_id)
            order = orders.get_order(order_id)
            prints.print_order(order)
        except ValueError as error:
            print(f"error: {error}")


def close_order():
    while True:
        try:
            order_id = Inputs.get_input("Enter order ID:")
            Inputs.input_validation(order_id, "Order ID", "positive")
            order_id = int(order_id)
            order = orders.get_order(order_id)
            if orders.ov.is_closed(order):
                raise ValueError("Order is already closed:")
            orders = storage.load_orders()
            for o in orders:
                if o["id"] == order_id:
                    o["status"] = "CLOSED"
            storage.write_orders(orders)
        except ValueError as error:
            print(f"error: {error}")
