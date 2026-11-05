import inputs_validation as Inputs


def is_enough()->bool:
    while True:
        try:
            choice = Inputs.get_input("Add another product?  Y/N")
            match choice:
                case "Y" | "y":
                    return False
                case "N" | "n":
                    return True
                case _:
                    raise ValueError("Please ensure with 'Y' or 'N' only")
        except ValueError as error:
            print(f"error: {error}")


def is_closed(order):
    return order["status"] == "CLOSED"